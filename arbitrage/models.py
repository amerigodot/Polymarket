from dataclasses import dataclass
from fetching.models import StandardizedMarket

@dataclass
class ArbitrageOpportunity:
    market_1: StandardizedMarket
    market_2: StandardizedMarket
    buy_on_1: str  # Outcome to buy on Market 1 (e.g. "Yes")
    buy_on_2: str  # Outcome to buy on Market 2 (e.g. "No")
    price_1: float
    price_2: float
    spread: float
    profit_pct: float
    timestamp: float
