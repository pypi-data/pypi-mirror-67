import abc

import pbpstats
from pbpstats.resources.enhanced_pbp.foul import Foul


class FreeThrow(metaclass=abc.ABCMeta):
    event_type = 3
    shot_type = pbpstats.FREE_THROW_STRING

    @abc.abstractproperty
    def made(self):
        pass

    @property
    def ft_1_of_1(self):
        return self.event_action_type == 10

    @property
    def ft_1_of_2(self):
        return self.event_action_type == 11

    @property
    def ft_2_of_2(self):
        return self.event_action_type == 12

    @property
    def ft_1_of_3(self):
        return self.event_action_type == 13

    @property
    def ft_2_of_3(self):
        return self.event_action_type == 14

    @property
    def ft_3_of_3(self):
        return self.event_action_type == 15

    @property
    def first_ft(self):
        return '1 of' in self.description or self.ft_1pt or self.ft_2pt or self.ft_3pt

    @property
    def end_ft(self):
        return self.ft_1_of_1 or self.ft_2_of_2 or self.ft_3_of_3 or self.ft_1pt or self.ft_2pt or self.ft_3pt

    @property
    def technical_ft(self):
        return ' Technical' in self.description

    @property
    def ft_1pt(self):
        """
        only used in g-league, starting in 2019-20 season
        """
        return self.event_action_type == 30 or self.event_action_type == 35

    @property
    def ft_2pt(self):
        """
        only used in g-league, starting in 2019-20 season
        """
        return self.event_action_type == 31 or self.event_action_type == 36

    @property
    def ft_3pt(self):
        """
        only used in g-league, starting in 2019-20 season
        """
        return self.event_action_type == 32 or self.event_action_type == 37

    @property
    def shot_value(self):
        if self.ft_2pt:
            return 2
        if self.ft_3pt:
            return 3
        return 1

    @property
    def is_away_from_play_ft(self):
        foul = self.foul_that_led_to_ft
        if ((self.ft_1_of_1 or self.ft_1pt) or (self.ft_2_of_2 or self.ft_2pt)) and foul is not None and foul.is_away_from_play_foul:
            made_shots_at_event_time = []
            fts_by_other_player_at_event_time = []
            events_at_event_time = self.get_all_events_at_current_time()
            for event in events_at_event_time:
                if hasattr(event, 'made') and event.made:
                    if not isinstance(event, FreeThrow):
                        made_shots_at_event_time.append(event)
                    if isinstance(event, FreeThrow) and event.player1_id != self.player1_id:
                        fts_by_other_player_at_event_time.append(event)

            if len(made_shots_at_event_time) == 0:
                # check for made free throw by other player - this is where player is fouled going for rebound on made FT
                if len(fts_by_other_player_at_event_time) == 0:
                    return True
                for ft in fts_by_other_player_at_event_time:
                    if ft.team_id != self.team_id:
                        return True
            else:
                made_shots_at_event_time = sorted(made_shots_at_event_time, key=lambda k: k.order)
                if (made_shots_at_event_time[0].team_id == foul.team_id) and (self.player1_id != made_shots_at_event_time[0].player1_id):
                    # make sure player who made shot is not player who shot FT
                    return True

        return False

    @property
    def is_inbound_foul_ft(self):
        if self.ft_1_of_1 or self.ft_1pt:
            events_at_event_time = self.get_all_events_at_current_time()
            for event in events_at_event_time:
                if isinstance(event, Foul) and event.is_inbound_foul:
                    return True

        return False

    @property
    def foul_that_led_to_ft(self):
        clock = self.clock
        # foul should be before FT so start by going backwards
        event = self
        while event is not None and event.clock == clock and not (isinstance(event, Foul) and not event.is_technical and not event.is_double_technical):
            event = event.previous_event

        if isinstance(event, Foul) and not event.is_technical and not event.is_double_technical and event.clock == clock:
            return event

        # bug in pbp where foul is after FT
        event = self
        while event is not None and event.clock == clock and not (isinstance(event, Foul) and not event.is_technical and not event.is_double_technical):
            event = event.next_event

        if isinstance(event, Foul) and not event.is_technical and not event.is_double_technical and event.clock == clock:
            return event
        return None

    @property
    def num_ft_for_trip(self):
        if 'of 1' in self.description:
            return 1
        elif 'of 2' in self.description:
            return 2
        elif 'of 3' in self.description:
            return 3

    @property
    def free_throw_type(self):
        if self.technical_ft:
            return 'Technical'
        num_fts = self.num_ft_for_trip

        if num_fts == 1:
            # check for shot before FT at same time as FT
            previous_event = self
            while previous_event is not None and previous_event.clock == self.clock and not (hasattr(previous_event, 'made') and previous_event.made and not isinstance(previous_event, FreeThrow)):
                previous_event = previous_event.previous_event
            if previous_event is not None and previous_event.clock == self.clock and (hasattr(previous_event, 'made') and previous_event.made and not isinstance(previous_event, FreeThrow)):
                and1_shot = previous_event
                if self.player1_id == and1_shot.player1_id:
                    return f'{and1_shot.shot_value}pt And 1'
                else:
                    return '1 Shot Away From Play'
            else:
                return '1 Shot Away From Play'
        foul_event = self.foul_that_led_to_ft
        if foul_event.is_shooting_foul or foul_event.is_shooting_block_foul:
            return f'{num_fts}pt Shooting Foul'
        elif foul_event.is_flagrant:
            if num_fts is None:
                # assume 2 shot flagrant if num_fts is None
                num_fts = 2
            return f'{num_fts} Shot Flagrant'
        elif foul_event.is_away_from_play_foul:
            return f'{num_fts} Shot Away From Play'
        elif foul_event.is_inbound_foul:
            return f'{num_fts} Shot Inbound Foul'
        elif foul_event.is_clear_path_foul:
            return f'{num_fts} Shot Clear Path'
        elif num_fts == 3:
            return '3pt Shooting Foul'
        else:
            return 'Penalty'

    @property
    def event_for_efficiency_stats(self):
        clock = self.clock
        # foul should be before FT so start by going backwards
        event = self
        while event is not None and event.clock == clock and not isinstance(event, Foul):
            event = event.previous_event

        if isinstance(event, Foul) and event.clock == clock:
            return event

        # bug in pbp where foul is after FT
        event = self
        while event is not None and event.clock == clock and not isinstance(event, Foul):
            event = event.next_event

        if isinstance(event, Foul) and event.clock == clock:
            return event
        return self

    @property
    def event_stats(self):
        stats = []
        team_ids = list(self.current_players.keys())
        is_penalty_event = self.is_penalty_event()
        is_second_chance_event = self.is_second_chance_event()
        lineup_ids = self.event_for_efficiency_stats.lineup_ids
        if self.made:
            if self.ft_3pt:
                free_throw_key = pbpstats.FT_3_PT_MADE_STRING
            elif self.ft_2pt:
                free_throw_key = pbpstats.FT_2_PT_MADE_STRING
            elif self.ft_1pt:
                free_throw_key = pbpstats.FT_1_PT_MADE_STRING
            elif self.technical_ft:
                free_throw_key = pbpstats.TECHNICAL_FTS_MADE_STRING
            else:
                free_throw_key = pbpstats.FTS_MADE_STRING
            points = self.shot_value
            stats.append({'player_id': self.player1_id, 'team_id': self.team_id, 'stat_key': free_throw_key, 'stat_value': 1})
            if is_second_chance_event:
                second_chance_stat_key = f'{pbpstats.SECOND_CHANCE_STRING}{free_throw_key}'
                stats.append({'player_id': self.player1_id, 'team_id': self.team_id, 'stat_key': second_chance_stat_key, 'stat_value': 1})
            if is_penalty_event:
                penalty_stat_key = f'{pbpstats.PENALTY_STRING}{free_throw_key}'
                stats.append({'player_id': self.player1_id, 'team_id': self.team_id, 'stat_key': penalty_stat_key, 'stat_value': 1})
                foul_event = self.foul_that_led_to_ft
                if foul_event is not None and foul_event.is_personal_take_foul and self.seconds_remaining < 60 and self.period >= 4:
                    final_minute_take_foul_stat_key = f'{pbpstats.FINAL_MINUTE_PENALTY_TAKE_FOUL_STRING}{free_throw_key}'
                    stats.append({'player_id': self.player1_id, 'team_id': self.team_id, 'stat_key': final_minute_take_foul_stat_key, 'stat_value': 1})

            # add plus minus and opponent points - used for lineup/wowy stats to get net rating
            for team_id, players in self.event_for_efficiency_stats.current_players.items():
                multiplier = 1 if team_id == self.team_id else -1
                opponent_team_id = team_ids[0] if team_id == team_ids[1] else team_ids[1]
                for player_id in players:
                    stat_item = {
                        'player_id': player_id,
                        'team_id': team_id,
                        'opponent_team_id': opponent_team_id,
                        'lineup_id': lineup_ids[team_id],
                        'opponent_lineup_id': lineup_ids[opponent_team_id],
                        'stat_key': pbpstats.PLUS_MINUS_STRING,
                        'stat_value': points * multiplier,
                    }
                    stats.append(stat_item)
                    if multiplier == -1:
                        opponent_points_stat_item = {
                            'player_id': player_id,
                            'team_id': team_id,
                            'opponent_team_id': opponent_team_id,
                            'lineup_id': lineup_ids[team_id],
                            'opponent_lineup_id': lineup_ids[opponent_team_id],
                            'stat_key': pbpstats.OPPONENT_POINTS,
                            'stat_value': points,
                        }
                        stats.append(opponent_points_stat_item)
        if self.first_ft or self.technical_ft:
            free_throw_trip_key = self.free_throw_type + ' Free Throw Trips'
            stats.append({'player_id': self.player1_id, 'team_id': self.team_id, 'stat_key': free_throw_trip_key, 'stat_value': 1})
            if is_second_chance_event:
                second_chance_stat_key = f'{pbpstats.SECOND_CHANCE_STRING}{free_throw_trip_key}'
                stats.append({'player_id': self.player1_id, 'team_id': self.team_id, 'stat_key': second_chance_stat_key, 'stat_value': 1})
            if is_penalty_event:
                penalty_stat_key = f'{pbpstats.PENALTY_STRING}{free_throw_trip_key}'
                stats.append({'player_id': self.player1_id, 'team_id': self.team_id, 'stat_key': penalty_stat_key, 'stat_value': 1})
                foul_event = self.foul_that_led_to_ft
                if foul_event is not None and foul_event.is_personal_take_foul and self.seconds_remaining < 60 and self.period >= 4:
                    current_players = self.event_for_efficiency_stats.current_players
                    offense_team_id = self.get_offense_team_id()
                    for team_id, players in current_players.items():
                        final_minute_take_foul_possessions_stat_key = (
                            f'{pbpstats.FINAL_MINUTE_PENALTY_TAKE_FOUL_STRING}{pbpstats.OFFENSIVE_POSSESSION_STRING}'
                            if team_id == offense_team_id
                            else f'{pbpstats.FINAL_MINUTE_PENALTY_TAKE_FOUL_STRING}{pbpstats.DEFENSIVE_POSSESSION_STRING}'
                        )
                        for player_id in players:
                            stat_item = {
                                'player_id': player_id,
                                'team_id': team_id,
                                'stat_key': final_minute_take_foul_possessions_stat_key,
                                'stat_value': 1,
                            }
                            stats.append(stat_item)

        if not self.made:
            if self.ft_3pt:
                free_throw_key = pbpstats.FT_3_PT_MISSED_STRING
            elif self.ft_2pt:
                free_throw_key = pbpstats.FT_2_PT_MISSED_STRING
            elif self.ft_1pt:
                free_throw_key = pbpstats.FT_1_PT_MISSED_STRING
            else:
                free_throw_key = pbpstats.FTS_MISSED_STRING
            stats.append({'player_id': self.player1_id, 'team_id': self.team_id, 'stat_key': free_throw_key, 'stat_value': 1})
            if is_second_chance_event:
                second_chance_stat_key = f'{pbpstats.SECOND_CHANCE_STRING}{free_throw_key}'
                stats.append({'player_id': self.player1_id, 'team_id': self.team_id, 'stat_key': second_chance_stat_key, 'stat_value': 1})
            if is_penalty_event:
                penalty_stat_key = f'{pbpstats.PENALTY_STRING}{free_throw_key}'
                stats.append({'player_id': self.player1_id, 'team_id': self.team_id, 'stat_key': penalty_stat_key, 'stat_value': 1})
                foul_event = self.foul_that_led_to_ft
                if foul_event is not None and foul_event.is_personal_take_foul and self.seconds_remaining < 60 and self.period >= 4:
                    final_minute_take_foul_stat_key = f'{pbpstats.FINAL_MINUTE_PENALTY_TAKE_FOUL_STRING}{free_throw_key}'
                    stats.append({'player_id': self.player1_id, 'team_id': self.team_id, 'stat_key': final_minute_take_foul_stat_key, 'stat_value': 1})

        opponent_team_id = team_ids[0] if self.team_id == team_ids[1] else team_ids[1]
        for stat in stats:
            if 'lineup_id' not in stat.keys():
                opponent_team_id = team_ids[0] if stat['team_id'] == team_ids[1] else team_ids[1]
                stat['lineup_id'] = lineup_ids[stat['team_id']]
                stat['opponent_team_id'] = opponent_team_id
                stat['opponent_lineup_id'] = lineup_ids[opponent_team_id]

        return self.base_stats + stats
