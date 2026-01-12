# Prediction Market Arbitrage Bot 📈
A modular Python-based tool designed to find **Risk-Free Binary Arbitrage** opportunities between prediction markets like **Polymarket** and **Manifold Markets**.

## 🌟 Overview
This project detects arbitrage opportunities where the combined cost of purchasing opposite outcomes across different exchanges is less than $1.00. 

For example:
- **Polymarket:** "Will it rain?" -> YES costs $0.60
- **Manifold:** "Will it rain?" -> NO costs $0.35
- **Total Cost:** $0.95
- **Guaranteed Payout:** $1.00
- **Risk-Free Profit:** $0.05 (5.2% ROI)

## ✨ Features
- **True Binary Arbitrage:** Calculates `Cost(YES_ExchangeA) + Cost(NO_ExchangeB)` to find guaranteed profit.
- **Liquidity Filtering:** Automatically ignores "dead" markets with low liquidity (< $100) to ensure tradeability.
- **Smart Matching:** Uses fuzzy string matching to link market events across platforms (e.g., matching "Will Trump win?" with "Trump 2024 Election").
- **Actionable Reporting:** Outputs specific trade instructions with direct deep-links to the markets.
- **Profit Calculation:** Displays the exact ROI spread for every opportunity found.

## 🚀 Getting Started

### Prerequisites
- [Python 3.8+](https://www.python.org/downloads/)
- `pip` (Python package manager)

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/polymarket-arbitrage.git
   cd polymarket-arbitrage
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🛠 Usage
To start the bot and begin scanning:

```bash
python3 main.py
```

### Sample Output
When an opportunity is found, the bot provides a clear action plan:

```text
----------------------------------------------------------------
MATCH: Will Bitcoin hit $100k in 2024?
  PROFIT: 5.26% | Spread: 0.05
  ACTION:
    1. Polymarket: Buy Yes @ 0.60 (https://polymarket.com/event/btc-100k)
    2. Manifold: Buy No @ 0.35 (https://manifold.markets/...)
----------------------------------------------------------------
```

## 📂 Project Structure
- `fetching/`: API integrations (Polymarket, Manifold) that normalize data into a standard format.
- `arbitrage/`: Core logic for fuzzy matching, liquidity filtering, and profit calculation.
- `main.py`: The orchestrator that runs the scan loop.

## 🤝 Contributing
Contributions are welcome! Please ensure any new exchange integrations inherit from `BaseDataProvider` and populate `liquidity` fields.

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.

## ⚠️ Disclaimer
Trading involves risk. While the math may show a profit, execution risks (slippage, API downtime, withdrawal fees) exist. This software is for educational purposes only.

