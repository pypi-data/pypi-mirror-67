from pbpstats.resources.enhanced_pbp.stats_nba.enhanced_pbp_item import StatsEnhancedPbpItem
from pbpstats.resources.enhanced_pbp.timeout import Timeout


class StatsTimeout(Timeout, StatsEnhancedPbpItem):
    def __init__(self, *args):
        super().__init__(*args)
