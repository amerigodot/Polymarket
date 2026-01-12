from dataclasses import dataclass
from typing import List, Dict

@dataclass
class StandardizedMarket:
    """A standardized market format for cross-exchange comparison."""
    id: str
    question: str
    slug: str
    outcomes: List[str]
    platform: str
    prices: Dict[str, float] # outcome -> price
    volume: float = 0.0
    liquidity: float = 0.0
    url: str = ""
