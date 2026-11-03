from teams import register_team, list_teams
from fixtures import generate_fixtures, list_fixtures
from results import record_results
from standing import calculate_standings, display_standings

teams = []
fixtures = []

while True:
    print("\n--------------------\nTOURNAMENTLAB\n--------------------\n")
    print("1. Register a team")
    print("2. View registered teams")
    print("3. Generate fixtures")
    print("4. View fixtures")
    print("5. Record match results")
    print("6. View League Table")
    print("7. Exit")

    choice = input("Pick an option: ")

    if choice == "1":
        name = input("Enter the name of the team: ")
        message = register_team(teams, name)
        print(message)

    elif choice == "2":
        list_teams(teams)

    elif choice == "3":
        message = generate_fixtures(teams, fixtures)
        print(message)

    elif choice == "4":
        list_fixtures(fixtures, teams)

    elif choice == "5":
        fixture_id = input("Enter fixture ID: ")
        home_score = int(input("Enter home score: "))
        away_score = int(input("Enter away score: "))

        record_results(fixtures, fixture_id, home_score, away_score)

    elif choice == "6":
        standings = calculate_standings(teams, fixtures)
        display_standings(teams, standings)
    
    elif choice == "7":
        print("Goodbye Soccer fan")
        break
    
    else:
        print("Invalid option. Please choose between 1 and 7")



    