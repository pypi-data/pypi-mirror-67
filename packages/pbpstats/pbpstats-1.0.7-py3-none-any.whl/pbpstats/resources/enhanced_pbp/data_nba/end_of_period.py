from pbpstats.resources.enhanced_pbp.data_nba.enhanced_pbp_item import DataEnhancedPbpItem
from pbpstats.resources.enhanced_pbp.end_of_period import EndOfPeriod


class DataEndOfPeriod(EndOfPeriod, DataEnhancedPbpItem):
    def __init__(self, *args):
        super().__init__(*args)
