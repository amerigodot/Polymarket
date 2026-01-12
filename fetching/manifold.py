import requests
import logging
from typing import List, Dict
from .interface import BaseDataProvider
from .models import StandardizedMarket

logger = logging.getLogger(__name__)

class ManifoldProvider(BaseDataProvider):
    API_URL = "https://api.manifold.markets/v0"

    def __init__(self):
        self.session = requests.Session()

    def get_markets(self, limit: int = 10) -> List[StandardizedMarket]:
        params = {"limit": limit}
        url = f"{self.API_URL}/markets"
        try:
            logger.info(f"Fetching data from: {url}")
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            markets = []
            for item in data:
                if item.get('outcomeType') == 'BINARY':
                    outcomes = ["YES", "NO"]
                    prob = item.get('probability', 0)
                    prices = {
                        "YES": float(prob),
                        "NO": 1.0 - float(prob)
                    }
                    
                    m = StandardizedMarket(
                        id=item.get('id'),
                        question=item.get('question'),
                        slug=item.get('slug', ''),
                        outcomes=outcomes,
                        platform="Manifold",
                        prices=prices
                    )
                    markets.append(m)
            return markets

        except Exception as e:
            logger.error(f"Failed to get Manifold markets: {e}")
            return []

    def get_market_price(self, market_id: str) -> Dict[str, float]:
        return {}
