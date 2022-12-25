import tests

WIN = 3
HOME_TEAM_WON = 1


# Time O(n) where n is number of competitions
# Space O(k) where k is number of teams
def tournament_winner(competitions, results):
    best_team = ''
    match_results = {best_team: 0}
    for i, result in enumerate(results):
        home_team, away_team = competitions[i]
        winning_team = home_team if result == HOME_TEAM_WON else away_team
        match_results[winning_team] = match_results.get(winning_team, 0) + WIN
        if match_results[winning_team] > match_results[best_team]:
            best_team = winning_team
    return best_team


tests.test(tournament_winner)
