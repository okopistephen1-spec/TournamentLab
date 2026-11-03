def generate_fixtures(teams: list, fixtures: list):

    if len(teams) < 4:
        return "You need at least 4 teams to generate a fixture"

    if len(teams) > 8:
        return "The teams cannot be more than 8 teams"

    if fixtures:
        return "Fixtures have already been generated"

    new_fixtures = []

    for i in range(len(teams)):
        for j in range(i + 1, len(teams)):

            fixture_id = f"M{len(new_fixtures) + 1:03d}"

            new_fixture = {
                "id": fixture_id,
                "home_id": teams[i]["id"],
                "away_id": teams[j]["id"],
                "status": "pending",
                "home_score": None,
                "away_score": None
            }

            new_fixtures.append(new_fixture)

    fixtures.extend(new_fixtures)

    return f"Successfully generated {len(fixtures)} fixtures!"



def list_fixtures(fixtures: list, teams: list):

    if not fixtures:
        print("No fixtures have been generated yet.")
        return

    print("\n############ TOURNAMENT FIXTURES ############")

    for fixture in fixtures:

        home = next(
            team["name"] for team in teams
            if team["id"] == fixture["home_id"]
        )

        away = next(
            team["name"] for team in teams
            if team["id"] == fixture["away_id"]
        )

        print(
            f"{fixture['id']}: {home} vs {away} | "
            f"Status: {fixture['status']}"
        )

    print("####################################")