from teams import register_team, list_teams
from fixtures import generate_fixtures, list_fixtures
from results import record_results
from standing import calculate_standings, display_standings
from storage import save_data, load_data


teams, fixtures,data_loaded = load_data()

if not data_loaded:
    print("Tournament data couldn't be loaded")
    print("Please check your json file(tournament.json)")
    exit()

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
        name = input("Enter the name of the team: ").title()
        message = register_team(teams, name)
        print(message)


        if message.startswith("Team registered successfully"):
            save_data(teams, fixtures)

    elif choice == "2":
        list_teams(teams)

    elif choice == "3":
        message = generate_fixtures(teams, fixtures)
        print(message)

        if message.startswith("Successfully generated"):
            save_data(teams, fixtures)

    elif choice == "4":
        list_fixtures(fixtures, teams)

    elif choice == "5":
        fixture_id = input("Enter fixture ID: ")

        while True:
            try:
                home_score = int(input("Enter home score: "))
                away_score = int(input("Enter away score: "))

                break
            
            except ValueError:
                print("Invalid input! Enter a score('numbers only')")
                    

        success = record_results(fixtures, fixture_id, home_score, away_score)

        if success:
            save_data(teams, fixtures)

    elif choice == "6":
        standings = calculate_standings(teams, fixtures)
        display_standings(teams, standings)
    
    elif choice == "7":
        print("Goodbye Soccer fan")
        break
    
    else:
        print("Invalid option. Please choose between 1 and 7")



    