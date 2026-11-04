import json

def validate_data(data):
    if not isinstance(data, dict):
        return False

    if "teams" not in data or "fixture" not in data:
        return False

    if not isinstance(data["teams"], list):
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
        
        return data["teams"], data["fixtures"]

    except FileNotFoundError:
        return [], []
