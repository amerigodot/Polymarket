from dataclasses import dataclass
from fetching.models import StandardizedMarket

@dataclass
class ArbitrageOpportunity:
    market_1: StandardizedMarket
    market_2: StandardizedMarket
    outcome: str
    price_1: float
    price_2: float
    spread: float
    timestamp: float
