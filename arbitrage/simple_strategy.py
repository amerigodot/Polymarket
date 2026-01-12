import time
import logging
from typing import List
from difflib import SequenceMatcher
from fetching.models import StandardizedMarket
from .interface import ArbitrageStrategy
from .models import ArbitrageOpportunity

logger = logging.getLogger(__name__)

class FuzzyMatchStrategy(ArbitrageStrategy):
    def __init__(self, threshold: float = 0.05, match_similarity: float = 0.8):
        self.threshold = threshold
        self.match_similarity = match_similarity

    def find_opportunities(self, markets: List[StandardizedMarket]) -> List[ArbitrageOpportunity]:
        opportunities = []
        
        # Group by platform
        platforms = {}
        for m in markets:
            if m.platform not in platforms:
                platforms[m.platform] = []
            platforms[m.platform].append(m)
            
        platform_names = list(platforms.keys())
        if len(platform_names) < 2:
            logger.warning("Not enough platforms to compare.")
            return []

        # Compare pair-wise (simplified for 2 platforms: Poly vs Mani)
        # Ideally, we compare every platform against every other
        
        # Taking the first two for this implementation
        p1_name = platform_names[0]
        p2_name = platform_names[1]
        
        markets_1 = platforms[p1_name]
        markets_2 = platforms[p2_name]
        
        for m1 in markets_1:
            for m2 in markets_2:
                similarity = SequenceMatcher(None, m1.question, m2.question).ratio()
                
                if similarity > self.match_similarity:
                    opp = self._compare_prices(m1, m2)
                    if opp:
                        opportunities.append(opp)
                        
        return opportunities

    def _compare_prices(self, m1: StandardizedMarket, m2: StandardizedMarket):
        # Check 'Yes' outcome
        def get_price(m, label):
            for k, v in m.prices.items():
                if k.lower() == label.lower():
                    return v
            return None

        p1 = get_price(m1, 'Yes')
        p2 = get_price(m2, 'Yes')

        if p1 is not None and p2 is not None:
            spread = abs(p1 - p2)
            if spread > self.threshold:
                return ArbitrageOpportunity(
                    market_1=m1,
                    market_2=m2,
                    outcome='Yes',
                    price_1=p1,
                    price_2=p2,
                    spread=spread,
                    timestamp=time.time()
                )
        return None
