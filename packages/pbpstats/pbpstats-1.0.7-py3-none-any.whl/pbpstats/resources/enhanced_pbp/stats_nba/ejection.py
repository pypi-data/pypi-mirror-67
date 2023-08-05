from pbpstats.resources.enhanced_pbp.stats_nba.enhanced_pbp_item import StatsEnhancedPbpItem
from pbpstats.resources.enhanced_pbp.ejection import Ejection


class StatsEjection(Ejection, StatsEnhancedPbpItem):
    def __init__(self, *args):
        super().__init__(*args)
