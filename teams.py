def register_team(teams: list, name: str):
    name = name.strip()

    # Validate team name
    if name == "":
        return "Team name cannot be empty!"

    if len(name) < 2:
        return "Team name must contain at least 2 characters!"

    if len(name) > 30:
        return "Team name cannot exceed 30 characters!"

    # Check for duplicate names
    for team in teams:
        if team["name"].casefold() == name.casefold():
            return "A team with that name already exists!"

    # Generate team ID
    team_id = f"TM{len(teams) + 1:03d}"

    # Create team record
    new_team = {
        "id": team_id,
        "name": name
    }

    teams.append(new_team)

    return f"Team is registered successfully! ID: {team_id}"

def list_teams(teams: list):
    if not teams:
        print("No teams have been registered yet.")
        return

    print("\n--------------------\n REGISTERED TEAMS \n--------------------------\n")

    for index, team in enumerate(teams, start=1):
        print(f"{index}. {team['name']} | ID: {team['id']}")

    print("======================================")