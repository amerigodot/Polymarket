# Prediction Market Arbitrage Bot 📈

A modular Python-based tool designed to find price discrepancies between different prediction markets like **Polymarket** and **Manifold Markets**.

## 🌟 Overview
This project helps you identify "arbitrage" opportunities—situations where the same event is priced differently on different platforms. By buying an outcome where it is cheap and selling (or betting against) it where it is expensive, one can theoretically lock in a profit.

**Note:** This tool is currently for **educational and simulation purposes**. No real trades are executed.

## ✨ Features
- **Multi-Exchange Support:** Integrated with Polymarket and Manifold Markets.
- **Smart Matching:** Uses fuzzy string matching to find identical events across platforms even if they are worded differently.
- **Modular Design:** Easily add new exchanges or strategy logic without breaking existing code.
- **Real-time Monitoring:** Fetches current market probabilities and prices.
- **Detailed Logging:** Clear terminal output showing matches and calculated spreads.

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
To start the bot and begin scanning for arbitrage opportunities, simply run:

```bash
python3 main.py
```

### What happens when you run it?
1. The bot connects to **Polymarket** and **Manifold Markets**.
2. It fetches the latest active markets.
3. It compares the market titles. If it finds two that look the same (e.g., "Will it rain in NYC?" vs "NYC Rain Probability"), it checks their prices.
4. If the price difference is greater than 5%, it flags it as an **Arbitrage Opportunity** in your terminal.

## 📂 Project Structure
- `fetching/`: Handles all the "talking" to the different market APIs.
- `arbitrage/`: Contains the "brain" that compares prices and finds deals.
- `main.py`: The control center that starts everything.

## 🤝 Contributing
Contributions are welcome! If you'd like to add a new exchange or improve the matching algorithm:
1. Fork the project.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.

## ⚠️ Disclaimer
Trading involves risk. This software is provided "as is" without any guarantees. Always do your own research before committing funds to any platform.
