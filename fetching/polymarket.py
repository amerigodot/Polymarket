import requests
import logging
from typing import List, Dict, Any, Optional
from .interface import BaseDataProvider
from .models import StandardizedMarket

logger = logging.getLogger(__name__)

class PolymarketProvider(BaseDataProvider):
    GAMMA_API_URL = "https://gamma-api.polymarket.com"

    def __init__(self):
        self.session = requests.Session()
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

    def _get(self, url: str, params: Optional[Dict] = None) -> Any:
        try:
            logger.info(f"Fetching data from: {url}")
            response = self.session.get(url, headers=self.headers, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching data from {url}: {e}")
            raise

    def get_markets(self, limit: int = 10) -> List[StandardizedMarket]:
        params = {"limit": limit, "closed": False}
        try:
            data = self._get(f"{self.GAMMA_API_URL}/markets", params=params)
            
            markets = []
            items = data if isinstance(data, list) else data.get('data', [])
            
            for item in items:
                outcomes = item.get('outcomes')
                if not isinstance(outcomes, list):
                     outcomes = ["Yes", "No"] 

                raw_prices = item.get('outcomePrices')
                prices = {}
                if raw_prices and isinstance(raw_prices, list) and len(raw_prices) == len(outcomes):
                     try:
                        prices = {str(o): float(p) for o, p in zip(outcomes, raw_prices)}
                     except (ValueError, TypeError):
                         pass
                
                m = StandardizedMarket(
                    id=str(item.get('id')),
                    question=item.get('question', 'Unknown'),
                    slug=item.get('slug', ''),
                    outcomes=outcomes,
                    platform="Polymarket",
                    prices=prices,
                    volume=float(item.get('volume', 0) or 0),
                    liquidity=float(item.get('liquidity', 0) or 0),
                    url=f"https://polymarket.com/event/{item.get('slug', '')}"
                )
                markets.append(m)
            return markets
        except Exception as e:
            logger.error(f"Failed to get Polymarket markets: {e}")
            return []

    def get_market_price(self, market_id: str) -> Dict[str, float]:
        return {}
