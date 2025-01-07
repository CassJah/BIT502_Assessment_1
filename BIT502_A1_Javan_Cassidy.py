# BIT502 - Application Development
# Name: Javan Cassidy
# Student ID: 5054294
# Assessment Number: 1
# This program is a City Gym Administration system that allows users to select membership plans,
# optional extras, record gym challenge times, and view a summary of their selections.

import os  # Module for clearing the console (cross-platform support).
import time  # Module for adding delays (used for smoother user experience).

# Persistent state to store user data throughout the app session.
user_data = {
    "membership_plan": None,  # Stores the chosen membership plan (Basic, Regular, Premium).
    "optional_extras": [],  # Stores selected optional extras (e.g., 24/7 access, personal training).
    "gym_challenge_score": None,  # Stores the total gym challenge time.
}

# Clears the console for a cleaner user interface.
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')  # Uses 'cls' for Windows and 'clear' for Linux/Mac.

# Prints a divider line for better visual separation in the UI.
def print_divider():
    print("=" * 40)

# Displays the main menu and handles user input for navigation.
def main_menu():
    while True:  # Loop keeps displaying the menu until the user selects 'Exit'.
        clear_console()
        print_divider()
        print("🏋️‍♂️  Welcome to City Gym Administration 🏋️‍♀️")
        print_divider()
        print("1. Membership Plans")  # Navigate to membership plan selection.
        print("2. Optional Extras")  # Navigate to optional extras menu.
        print("3. Gym Challenge")  # Record times for fitness activities.
        print("4. View Summary")  # Show a summary of the user’s selections.
        print("5. Exit")  # Exit the application.
        print_divider()
        choice = input("Enter your selection (0 for Help): ").strip()

        # Navigation options based on user input.
        if choice == '1':
            membership_menu()
        elif choice == '2':
            optional_extras()
        elif choice == '3':
            gym_challenge()
        elif choice == '4':
            display_summary()
        elif choice == '5':
            exit_program()
        elif choice == '0':
            display_help("Main Menu")
        else:
            print("❌ Invalid choice. Please try again.")
            time.sleep(2)  # Adds a delay before reloading the menu.

# Displays the membership plans and allows user to select a plan.
def membership_menu():
    while True:
        clear_console()
        print_divider()
        print("📋 Membership Plans")
        print_divider()
        print("1. Basic - $10/week (Beginner plan)")
        print("2. Regular - $15/week (Popular choice)")
        print("3. Premium - $20/week (All-inclusive)")
        print("4. Return to Main Menu")  # Return to the main menu.
        print("5. Exit")  # Exit the application.
        print_divider()
        choice = input("Enter your selection (0 for Help): ").strip()

        if choice in ['1', '2', '3']:
            set_membership_plan(choice)  # Calls function to set the membership plan.
        elif choice == '4':
            break  # Breaks out of the loop to return to the main menu.
        elif choice == '5':
            exit_program()
        elif choice == '0':
            display_help("Membership Menu")
        else:
            print("❌ Invalid choice. Please try again.")
            time.sleep(2)

# Sets the selected membership plan and displays a confirmation message.
def set_membership_plan(choice):
    membership_types = {
        '1': ("Basic", 10),  # Basic plan: $10/week.
        '2': ("Regular", 15),  # Regular plan: $15/week.
        '3': ("Premium", 20)  # Premium plan: $20/week.
    }
    user_data["membership_plan"] = membership_types[choice]
    membership, cost = membership_types[choice]
    print(f"✔️  You selected the {membership} plan, costing ${cost}/week.")
    input("Press Enter to return to the Membership Plans menu.")

# Handles selection and calculation of optional extras.
def optional_extras():
    clear_console()
    print_divider()
    print("🛠️ Optional Extras")
    print_divider()
    extras = {
        "24/7 Gym Access": 1,  # $1 for 24/7 access.
        "Personal Training": 20,  # $20 for personal training sessions.
        "Diet Consultation": 20,  # $20 for diet consultation.
        "Online Video Access": 2  # $2 for video tutorials and workout plans.
    }
    user_data["optional_extras"] = []  # Reset extras for each session.

    for extra, price in extras.items():  # Iterates over each extra feature.
        while True:
            choice = input(f"Would you like {extra} (${price})? (yes/no): ").strip().lower()
            if choice in ['yes', 'y']:
                user_data["optional_extras"].append(extra)  # Adds the selected extra to the list.
                break
            elif choice in ['no', 'n']:
                break
            else:
                print("❌ Invalid input. Please enter 'yes' or 'no'.")

    print_divider()
    total_cost = sum([extras[extra] for extra in user_data["optional_extras"]])  # Calculate total cost.
    print(f"✔️  Total cost for optional extras: ${total_cost}")
    input("Press Enter to return to the Main Menu.")

# Handles the gym challenge and records the time taken for each activity.
def gym_challenge():
    clear_console()
    print_divider()
    print("🏆 Gym Challenge")
    print_divider()
    print("Record your time for the following activities:")
    activities = [
        "50 skips with a skipping rope",
        "20 push-ups",
        "10 squats",
        "100m run"
    ]
    total_time = 0

    for activity in activities:  # Collects time for each activity.
        while True:
            try:
                time_taken = int(input(f"Time for {activity} (in seconds): "))
                if time_taken < 0:
                    raise ValueError  # Prevents negative times.
                total_time += time_taken
                break
            except ValueError:
                print("❌ Invalid input. Please enter a valid time in seconds.")

    total_time += 15 * (len(activities) - 1)  # Add 15-second breaks between activities.
    user_data["gym_challenge_score"] = total_time
    display_challenge_results(total_time)

# Displays the gym challenge results and rankings based on the total time.
def display_challenge_results(total_time):
    clear_console()
    print_divider()
    print(f"⏱️  Total time (including breaks): {total_time} seconds")
    print_divider()

    # Rank based on the total time taken.
    if total_time < 300:
        rank = "Gold"
    elif total_time < 360:
        rank = "Silver"
    elif total_time < 480:
        rank = "Bronze"
    else:
        rank = "Steel"

    print(f"🎖️ Congratulations, you are ranked {rank}!")
    if total_time < 264:  # Gym record is 4:24 minutes (264 seconds).
        print("🌟 You broke the gym record! Amazing job!")
    else:
        print(f"🏅 You need {total_time - 264} seconds less to break the gym record.")

    input("Press Enter to return to the Main Menu.")

# Displays a summary of the user’s selections.
def display_summary():
    clear_console()
    print_divider()
    print("📝 Summary of Your Selections")
    print_divider()
    if user_data["membership_plan"]:
        membership, cost = user_data["membership_plan"]
        print(f"Membership Plan: {membership} (${cost}/week)")
    else:
        print("Membership Plan: Not selected")

    if user_data["optional_extras"]:
        print(f"Optional Extras: {', '.join(user_data['optional_extras'])}")
    else:
        print("Optional Extras: None")

    if user_data["gym_challenge_score"] is not None:
        print(f"Gym Challenge Total Time: {user_data['gym_challenge_score']} seconds")
    else:
        print("Gym Challenge Total Time: Not completed")

    input("Press Enter to return to the Main Menu.")

# Displays help information for the current section.
def display_help(section):
    clear_console()
    print_divider()
    print(f"ℹ️ Help - {section}")
    print_divider()
    if section == "Main Menu":
        print("Navigate through the following options to access City Gym features:")
        print("1. Membership Plans - View and select a membership plan.")
        print("2. Optional Extras - Add extra features to your plan.")
        print("3. Gym Challenge - Record your fitness times and get ranked.")
        print("4. View Summary - See your current selections.")
        print("5. Exit - Quit the application.")
    elif section == "Membership Menu":
        print("Select a membership plan to suit your needs:")
        print("1. Basic - Basic access.")
        print("2. Regular - Includes group classes.")
        print("3. Premium - All-inclusive.")
    input("Press Enter to return to the menu.")

# Exits the program with a confirmation prompt.
def exit_program():
    while True:
        confirm = input("Are you sure you want to exit? (yes/no): ").strip().lower()
        if confirm in ['yes', 'y']:
            print("🛑 Thank you for using City Gym Admin! Goodbye!")
            time.sleep(2)  # Adds a delay before exiting.
            exit()
        elif confirm in ['no', 'n']:
            break  # Return to the previous menu.
        else:
            print("❌ Invalid input. Please enter 'yes' or 'no'.")

# Entry point of the program.
if __name__ == "__main__":
    main_menu()  # Starts the main menu loop.
