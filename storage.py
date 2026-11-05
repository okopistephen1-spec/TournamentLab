import json

def validate_data(data):
    if not isinstance(data, dict):
        return False

    if "teams" not in data or "fixtures" not in data:
        return False

    if type(data.get("schema_version")) is not int:
        return False

    if data["schema_version"] != 1:
        return False

    if not isinstance(data["teams"], list):
        return False

    if not isinstance(data["fixtures"], list):
        return False

    if not validate_teams(data["teams"]):
        return False

    if not validate_fixtures(data["fixtures"], data["teams"]):
        return False

    return True

def validate_teams(teams):
    team_ids = set()
    team_names = set()

    for team in teams:
        if not isinstance(team, dict):
            return False

        if "id" not in team or "name" not in team:
            return False

        team_id = team["id"]
        team_name = team["name"]

        if not isinstance(team_id, str):
            return False

        if not isinstance(team_name, str):
            return False

        if not team_id.strip():
            return False

        if not 2 <= len(team_name.strip()) <= 30:
            return False

        correct_name = team_name.strip().casefold()

        if team_id in team_ids:
            return False

        if correct_name in team_names:
            return False

        team_ids.add(team_id)
        team_names.add(correct_name)

    return True

def validate_fixtures(fixtures, teams):
    team_ids = {team["id"] for team in teams}
    fixture_ids = set()
    fixture_pairs = set()

    for fixture in fixtures:

        if not isinstance(fixture, dict):
            return False

        required_keys = [
            "id",
            "home_id",
            "away_id",
            "status",
            "home_score",
            "away_score"
        ]

        for key in required_keys:
            if key not in fixture:
                return False

        fixture_id = fixture["id"]
        home_id = fixture["home_id"]
        away_id = fixture["away_id"]
        pair = frozenset((home_id, away_id))

        if pair in fixture_pairs:
            return False

        fixture_pairs.add(pair)

       
        if not isinstance(fixture_id, str) or not fixture_id.strip():
            return False

        if fixture_id in fixture_ids:
            return False

        fixture_ids.add(fixture_id)

        
        if home_id not in team_ids or away_id not in team_ids:
            return False

        
        if home_id == away_id:
            return False

        
        if fixture["status"] not in ["pending", "completed"]:
            return False

       
        if fixture["status"] == "pending":
            if fixture["home_score"] is not None:
                return False

            if fixture["away_score"] is not None:
                return False

        
        elif fixture["status"] == "completed":
            home_score = fixture["home_score"]
            away_score = fixture["away_score"]

            if type(home_score) is not int or type(away_score) is not int:
                return False

            if home_score < 0 or away_score < 0:
                return False

    return True

def save_data(teams, fixtures):
    data = {
        "schema_version": 1,
        "teams": teams,
        "fixtures": fixtures,
    }

    with open("tournament.json", "w") as file:
        json.dump(data, file, indent=4)



def load_data():
    try:
        with open("tournament.json", "r") as file:
            data = json.load(file)
        
        if not validate_data(data):
            print("Invalid tournament data")
            return [], [], False

        return data["teams"], data["fixtures"], True

    except FileNotFoundError:
        return [], [], True

    except json.JSONDecodeError:
        print("Error: tournament.json contains invalid json")
        return [], [], False
