def calculate_standings(teams: list, fixtures: list):

    standings = []

    for team in teams:
        team_stats = {
            "team_id": team["id"],
            "played": 0,
            "wins": 0,
            "draws": 0,
            "losses": 0,
            "gf": 0,
            "ga": 0,
            "gd": 0,
            "points": 0
        }

        standings.append(team_stats)

    for fixture in fixtures:

        if fixture["status"] != "completed":
            continue

        home_team = next(
            stats for stats in standings
            if stats["team_id"] == fixture["home_id"]
        )

        home_score = fixture["home_score"]
        away_score = fixture["away_score"]

        away_team = next(
            stats for stats in standings
            if stats["team_id"] == fixture["away_id"]
        )

        home_team["played"] += 1
        away_team["played"] += 1

        home_team["gf"] += home_score
        home_team["ga"] += away_score

        away_team["gf"] += away_score
        away_team["ga"] += home_score

        if home_score > away_score:
            home_team["wins"] += 1
            home_team["points"] += 3

            away_team["losses"] += 1

        elif home_score < away_score:
            away_team["wins"] += 1
            away_team["points"] += 3

            home_team["losses"] += 1

        else:
            home_team["draws"] += 1
            away_team["draws"] += 1

            home_team["points"] += 1
            away_team["points"] += 1

    for team in standings:
        team["gd"] = team["gf"] - team["ga"]

    standings.sort(key=lambda team: team["points"], reverse=True)


    return standings

def display_standings(teams: list, standings: list):

    if not standings:
        print("No standings found")
        return

    print("\n<><><><><><><><><><>\n LEAGUE TABLE ⚽\n<><><><><><><><><><>\n")

    print(
        f"{'POS':<5}"
        f"{'TEAM':<15}"
        f"{'P':<5}"
        f"{'W':<5}"
        f"{'D':<5}"
        f"{'L':<5}"
        f"{'GF':<5}"
        f"{'GA':<5}"
        f"{'GD':<6}"
        f"{'PTS':<5}"
    )

    for position, stats in enumerate(standings, start=1):

        team = next(
            team for team in teams
            if team["id"] == stats["team_id"]
        )

        print(
            f"{position:<5}"
            f"{team['name']:<15}"
            f"{stats['played']:<5}"
            f"{stats['wins']:<5}"
            f"{stats['draws']:<5}"
            f"{stats['losses']:<5}"
            f"{stats['gf']:<5}"
            f"{stats['ga']:<5}"
            f"{stats['gd']:<6}"
            f"{stats['points']:<5}"
        )

    print("⚽===================================================⚽")