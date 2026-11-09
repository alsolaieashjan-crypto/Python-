# AI300_HW0_AshjanAlsolaie.py
# Description: Interactive menu-driven system for a gaming system framework.

# Global variables to maintain game statistics
game1_count = 0
game1_avg = 0.0

game2_count = 0
game2_avg = 0.0

game3_count = 0
game3_avg = 0.0

def game1():
    # Placeholder for Game 1 - Requirement: adds 1 point
    global game1_count, game1_avg
    print("This is a placeholder for game 1.")
    game1_count += 1
    game1_avg = ((game1_avg * (game1_count - 1)) + 1.0) / game1_count

def game2():
    # Placeholder for Game 2 - Requirement: adds 2 points
    global game2_count, game2_avg
    print("This is a placeholder for game 2.")
    game2_count += 1
    game2_avg = ((game2_avg * (game2_count - 1)) + 2.0) / game2_count

def game3():
    # Placeholder for Game 3 - Requirement: adds 3 points
    global game3_count, game3_avg
    print("This is a placeholder for game 3.")
    game3_count += 1
    game3_avg = ((game3_avg * (game3_count - 1)) + 3.0) / game3_count

def display_info():
    # Displays total score and individual stats as per requirement
    total_score = (game1_avg * game1_count) + (game2_avg * game2_count) + (game3_avg * game3_count)
    print(f"Total score: {total_score}")
    print(f"Game1: played {game1_count} times, with an average score of {game1_avg}")
    print(f"Game2: played {game2_count} times, with an average score of {game2_avg}")
    print(f"Game3: played {game3_count} times, with an average score of {game3_avg}")

def print_menu():
    # Displays the menu options 1 through 5
    print("1. Game 1")
    print("2. Game 2")
    print("3. Game 3")
    print("4. Display info")
    print("5. Exit")

def main():
    # Main execution loop
    print("Select the option you want by typing its number")
    print_menu()
    
    while True:
        choice = input("Select the option you want, or 0 to redisplay menu ")
        
        if not choice.isdigit():
            print("Invalid input. Please enter a number.")
            continue
            
        choice = int(choice)

        if choice == 1:
            game1()
        elif choice == 2:
            game2()
        elif choice == 3:
            game3()
        elif choice == 4:
            display_info()
        elif choice == 5:
            break
        elif choice == 0:
            print_menu()
        else:
            print("Invalid input. Please try again.")
            print_menu()

if __name__ == "__main__":
    main()