# Project Context: Prediction Market Arbitrage

## Project Overview
This project is a multi-exchange prediction market monitoring and arbitrage tool. It integrates multiple platforms to identify price discrepancies and simulate trade execution.

**Core Components:**
- `main.py`: The application entry point and orchestrator.
- `fetching/`: Data Acquisition Layer.
    - `interface.py`: Defines the `BaseDataProvider` contract.
    - `models.py`: Defines `StandardizedMarket`.
    - `polymarket.py` & `manifold.py`: Concrete implementations.
- `arbitrage/`: Strategy Layer.
    - `interface.py`: Defines the `ArbitrageStrategy` contract.
    - `simple_strategy.py`: Implements fuzzy matching logic.
    - `models.py`: Defines `ArbitrageOpportunity`.

## Project Structure
```
/
├── main.py                # Entry point
├── fetching/              # Data Providers
│   ├── interface.py       # Provider Contract
│   ├── models.py          # Data Models
│   ├── polymarket.py
│   └── manifold.py
├── arbitrage/             # Strategies
│   ├── interface.py       # Strategy Contract
│   ├── models.py          # Opportunity Models
│   └── simple_strategy.py
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
- **Modular Design:** New exchanges must inherit from `BaseExchange` in `exchanges/base.py`.
- **Logging:** Use the standard `logging` library. All API interactions and opportunity detections should be logged.
- **Testing:** New features should include unit tests (standard `unittest`).
- **Safety:** Trade execution is currently simulated. Any move to real execution requires strict risk management and API key handling.