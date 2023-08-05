from pbpstats.resources.enhanced_pbp.data_nba.enhanced_pbp_item import DataEnhancedPbpItem
from pbpstats.resources.enhanced_pbp.free_throw import FreeThrow


class DataFreeThrow(FreeThrow, DataEnhancedPbpItem):
    def __init__(self, *args):
        super().__init__(*args)

    @property
    def made(self):
        return ' Missed' not in self.description
