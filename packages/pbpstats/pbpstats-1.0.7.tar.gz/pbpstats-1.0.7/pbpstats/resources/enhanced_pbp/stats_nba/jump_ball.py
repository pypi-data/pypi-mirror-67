from pbpstats.resources.enhanced_pbp.stats_nba.enhanced_pbp_item import StatsEnhancedPbpItem
from pbpstats.resources.enhanced_pbp.jump_ball import JumpBall
from pbpstats.resources.enhanced_pbp.turnover import Turnover
from pbpstats.resources.enhanced_pbp.foul import Foul


class StatsJumpBall(JumpBall, StatsEnhancedPbpItem):
    def __init__(self, *args):
        super().__init__(*args)

    def get_offense_team_id(self):
        """
        overrides method inherited from StatsEnhancedPbpItem
        """
        if self.next_event.clock == self.clock and isinstance(self.next_event, Turnover):
            return self.next_event.team_id
        if isinstance(self.next_event, Foul) and self.next_event.clock == self.clock:
            next_event = self.next_event.next_event
            if isinstance(next_event, Turnover) and not next_event.is_no_turnover and next_event.clock == self.clock:
                return next_event.team_id
        if self.count_as_possession:
            team_ids = list(self.current_players.keys())
            return team_ids[0] if team_ids[1] == self.team_id else team_ids[1]
        return self.team_id
