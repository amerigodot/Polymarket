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
        # Filter dead markets
        min_liquidity = 100.0
        if m1.liquidity < min_liquidity or m2.liquidity < min_liquidity:
            return None

        # Helper to get price
        def get_price(m, outcome):
            # Normalize outcome keys (case insensitive)
            for k, v in m.prices.items():
                if k.lower() == outcome.lower():
                    return v
            return None

        p1_yes = get_price(m1, 'Yes')
        p1_no = get_price(m1, 'No')
        p2_yes = get_price(m2, 'Yes')
        p2_no = get_price(m2, 'No')
        
        # If 'No' prices are missing (e.g. Polymarket sometimes only gives one side if not fully expanded), 
        # assume Binary 1 - Yes if highly liquid? No, safer to rely on explicit data or 1-p if valid.
        # Polymarket usually provides all outcome prices in API, but code above extracts them.
        # Manifold provides both.
        
        # Strategy 1: Buy YES on M1, Buy NO on M2
        if p1_yes and p2_no:
            cost = p1_yes + p2_no
            if cost < (1.0 - self.threshold):
                return ArbitrageOpportunity(
                    market_1=m1,
                    market_2=m2,
                    buy_on_1='Yes',
                    buy_on_2='No',
                    price_1=p1_yes,
                    price_2=p2_no,
                    spread=1.0 - cost,
                    profit_pct=(1.0 - cost) / cost * 100,
                    timestamp=time.time()
                )

        # Strategy 2: Buy NO on M1, Buy YES on M2
        if p1_no and p2_yes:
            cost = p1_no + p2_yes
            if cost < (1.0 - self.threshold):
                return ArbitrageOpportunity(
                    market_1=m1,
                    market_2=m2,
                    buy_on_1='No',
                    buy_on_2='Yes',
                    price_1=p1_no,
                    price_2=p2_yes,
                    spread=1.0 - cost,
                    profit_pct=(1.0 - cost) / cost * 100,
                    timestamp=time.time()
                )
                
        return None
