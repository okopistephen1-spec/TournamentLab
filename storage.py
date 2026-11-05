import json

def validate_data(data):
    if not isinstance(data, dict):
        return False

    if "teams" not in data or "fixtures" not in data:
        return False

    if not isinstance(data["teams"], list):
        return False

    if not isinstance(data["fixtures"], list):
        return False

    if not validate_teams(data["teams"]):
        return False

    if not validate_fixtures(data["fixtures"]):
        return False

    return True

def validate_teams(teams):
    for team in teams:
        if not isinstance(team, dict):
            return False

        if "id" not in team or "name" not in team:
            return False

        if not isinstance(team["id"], str):
            return False

        if not isinstance(team["name"], str):
            return False
        

    return True

def validate_fixtures(fixtures):

    for fixture in fixtures:

        if not isinstance(fixture, dict):
            return False

        required_keys = [
            "id",
            "home_id",
            "away_id",
            "status",
            "home_score",
            "away_score",
        ]

        for key in required_keys:
            if key not in fixture:
                return False

            if not isinstance(fixture["id"], str):
                return False

            if not isinstance(fixture["home_id"], str):
                return False

            if not isinstance(fixture["away_id"], str):
                return False

            if fixture["status"] not in ["pending", "completed"]:
                return False

            if fixture["status"] == "pending":
                if fixture["home_score"] is not None or fixture["away_score"] is not None:
                    return False

            if fixture["status"] == "completed":
                if not isinstance(fixture["home_score"], int):
                    return False

                if not isinstance(fixture["away_score"], int):
                    return False

                if fixture["home_score"] < 0 or fixture["away_score"] < 0:
                    return False

        return True

def save_data(teams, fixtures):
    data = {
        "teams": teams,
        "fixtures": fixtures
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
