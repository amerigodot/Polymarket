from abc import ABC, abstractmethod
from typing import List
from fetching.models import StandardizedMarket
from .models import ArbitrageOpportunity

class ArbitrageStrategy(ABC):
    @abstractmethod
    def find_opportunities(self, markets: List[StandardizedMarket]) -> List[ArbitrageOpportunity]:
        """Analyze markets and return a list of opportunities."""
        pass
