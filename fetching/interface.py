from abc import ABC, abstractmethod
from typing import List, Dict
from .models import StandardizedMarket

class BaseDataProvider(ABC):
    """Interface for data providers."""

    @abstractmethod
    def get_markets(self, limit: int = 10) -> List[StandardizedMarket]:
        """Fetch a list of markets in a standardized format."""
        pass

    @abstractmethod
    def get_market_price(self, market_id: str) -> Dict[str, float]:
        """Get current prices for a specific market."""
        pass
