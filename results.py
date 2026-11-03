def record_results(fixtures: list, fixture_id: str, home_score: int, away_score: int):

    found = False

    fixture_id = fixture_id.strip().upper()
    
    for fixture in fixtures:
        if fixture_id == fixture["id"]:
            print("Found fixture")
            found = True

            if fixture["status"] == "completed":
                print("This fixture has already been recorded")
                return
            
            if home_score < 0 or away_score < 0:
                print("Score cannot be a negative number or less than 0")
                return

            fixture["home_score"] = home_score
            fixture["away_score"] = away_score
            fixture["status"] = "completed"

            print("The match result is successfully recorded")
            
            break

    if not found:
        print("Fixture not found")
        return

    