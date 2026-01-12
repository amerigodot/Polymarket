# Project Context: Prediction Market Arbitrage

## Project Overview
This project is a multi-exchange prediction market monitoring and arbitrage tool. It integrates multiple platforms to identify risk-free binary arbitrage opportunities (where Cost(Yes) + Cost(No) < 1.0) and simulates trade execution instructions.

**Core Components:**
- `main.py`: The application entry point and orchestrator.
- `fetching/`: Data Acquisition Layer.
    - `interface.py`: Defines the `BaseDataProvider` contract.
    - `models.py`: Defines `StandardizedMarket` (includes `volume`, `liquidity`, `url` for filtering and access).
    - `polymarket.py` & `manifold.py`: Concrete implementations extracting price, volume, and deep-linking URLs.
- `arbitrage/`: Strategy Layer.
    - `interface.py`: Defines the `ArbitrageStrategy` contract.
    - `simple_strategy.py`: Implements fuzzy matching and **True Binary Arbitrage** logic.
        - Filters out low-liquidity markets (< $100).
        - Identifies opportunities where purchasing opposite outcomes across exchanges guarantees profit.
    - `models.py`: Defines `ArbitrageOpportunity` with actionable "Buy X on Platform Y" instructions and Profit %.

## Project Structure
```
/
├── main.py                # Entry point
├── fetching/              # Data Providers
│   ├── interface.py       # Provider Contract
│   ├── models.py          # Data Models (StandardizedMarket)
│   ├── polymarket.py
│   └── manifold.py
├── arbitrage/             # Strategies
│   ├── interface.py       # Strategy Contract
│   ├── models.py          # Opportunity Models (ArbitrageOpportunity)
│   └── simple_strategy.py # Logic: Fuzzy Match + Binary Arb + Liquidity Filter
├── requirements.txt
└── GEMINI.md
```

## Building and Running

### Prerequisites
- Python 3.x
- Dependencies: `requests`

### Installation
```bash
pip install -r requirements.txt
```

### Running the Arbitrage Bot
To start scanning for opportunities:
```bash
python3 main.py
```

### Running Tests
```bash
python3 -m unittest discover
```

## Development Conventions
- **Modular Design:** New exchanges must inherit from `BaseDataProvider` in `fetching/interface.py`.
- **Data Integrity:** All providers must populate `liquidity` and `volume` to ensure strategy safety.
- **Logging:** Use the standard `logging` library. Output must be actionable (include URLs and Buy instructions).
- **Safety:** Trade execution is currently simulated. Real execution requires strict API key management and slippage protection.