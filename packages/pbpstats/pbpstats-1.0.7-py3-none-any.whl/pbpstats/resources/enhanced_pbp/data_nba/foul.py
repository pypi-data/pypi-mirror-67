from pbpstats.resources.enhanced_pbp.data_nba.enhanced_pbp_item import DataEnhancedPbpItem
from pbpstats.resources.enhanced_pbp.foul import Foul


class DataFoul(Foul, DataEnhancedPbpItem):
    def __init__(self, *args):
        super().__init__(*args)

    @property
    def number_of_fta_for_foul(self):
        if '(1 FTA)' in self.description:
            return 1
        elif '(2 FTA)' in self.description:
            return 2
        elif '(3 FTA)' in self.description:
            return 3
