from pbpstats.resources.enhanced_pbp.data_nba.enhanced_pbp_item import DataEnhancedPbpItem
from pbpstats.resources.enhanced_pbp.substitution import Substitution


class DataSubstitution(Substitution, DataEnhancedPbpItem):
    def __init__(self, *args):
        super().__init__(*args)
