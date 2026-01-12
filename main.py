import logging
import sys
from fetching.polymarket import PolymarketProvider
from fetching.manifold import ManifoldProvider
from arbitrage.simple_strategy import FuzzyMatchStrategy

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

def main():
    logger.info("Initializing Arbitrage Bot...")
    
    # 1. Initialize Providers
    providers = [
        PolymarketProvider(),
        ManifoldProvider()
    ]
    
    # 2. Initialize Strategy
    strategy = FuzzyMatchStrategy(threshold=0.05)
    
    # 3. Fetch Data
    all_markets = []
    for provider in providers:
        try:
            markets = provider.get_markets(limit=500)
            logger.info(f"Fetched {len(markets)} markets from {provider.__class__.__name__}")
            all_markets.extend(markets)
        except Exception as e:
            logger.error(f"Error fetching from provider: {e}")

    # 4. Execute Strategy
    logger.info("Analyzing markets for opportunities...")
    opportunities = strategy.find_opportunities(all_markets)
    
    # 5. Report
    if not opportunities:
        logger.info("No arbitrage opportunities found.")
    else:
        logger.info(f"Found {len(opportunities)} opportunities:")
        for opp in opportunities:
            logger.info("----------------------------------------------------------------")
            logger.info(f"MATCH: {opp.market_1.question}")
            logger.info(f"  PROFIT: {opp.profit_pct:.2f}% | Spread: {opp.spread:.2f}")
            logger.info(f"  ACTION:")
            logger.info(f"    1. {opp.market_1.platform}: Buy {opp.buy_on_1} @ {opp.price_1:.2f} ({opp.market_1.url})")
            logger.info(f"    2. {opp.market_2.platform}: Buy {opp.buy_on_2} @ {opp.price_2:.2f} ({opp.market_2.url})")
            logger.info("----------------------------------------------------------------")

if __name__ == "__main__":
    main()
