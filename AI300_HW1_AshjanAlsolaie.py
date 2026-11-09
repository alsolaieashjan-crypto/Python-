import random

# Global variables for tracking statistics as required by the HW0 integration
game1_count = 0
game1_avg = 0.0

game2_count = 0
game2_avg = 0.0

game3_count = 0
game3_avg = 0.0

# REQUIRED FUNCTIONS FOR HANGMAN 

def select_word():
    # Selects and returns the word the player will try to guess
    # Words are predefined in a list as per assignment description
    words = ["BANANA", "PYTHON", "COMPUTER", "ALGORITHM", "SCIENCE", "STUDENT"]
    return random.choice(words)

def is_valid_guess(guess, guessed_letters):
    # Checks whether the user's guess is valid and displays appropriate messages
    # Requirement: Validate input and allow letters only
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
        return False
    # Requirement: Check if the letter has already been guessed
    if guess.upper() in guessed_letters:
        print(f"You already guessed '{guess.upper()}'. Try another letter.")
        return False
    return True

def draw_hangman(tries_left):
    # Displays the current visual state of the Hangman based on failed attempts
    # Requirement: Visual state must be implemented as predefined strings
    stages = [
        # 0 tries left: Final LOSE state
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / \\
           -
        """,
        # 1 try left
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / 
           -
        """,
        # 2 tries left
        """
           --------
           |      |
           |      O
           |     /|\\
           |      
           -
        """,
        # 3 tries left
        """
           --------
           |      |
           |      O
           |     /|
           |     
           -
        """,
        # 4 tries left
        """
           --------
           |      |
           |      O
           |      |
           |     
           -
        """,
        # 5 tries left
        """
           --------
           |      |
           |      O
           |    
           |     
           -
        """,
        # 6 tries left: Initial state
        """
           --------
           |      |
           |      
           |    
           |     
           -
        """
    ]
    print(stages[tries_left])

def play_hangman():
    # Main function that controls the game flow and logic
    global game1_count, game1_avg
    
    word = select_word()
    guessed_letters = []
    total_tries = 6
    tries_left = total_tries
    word_completion = "_" * len(word)
    
    print("\n---------- HANGMAN ----------")
    
    # Requirement: Program must display hidden word using underscores
    while tries_left > 0 and "_" in word_completion:
        draw_hangman(tries_left)
        print(f"Word: {' '.join(word_completion)}")
        print(f"Guessed letters: {' '.join(guessed_letters)}")
        
        # Requirement: Accept both lowercase and uppercase inputs
        guess = input("Please guess a letter: ").upper()
        
        # Requirement: Invalid input must not reduce the number of attempts
        if not is_valid_guess(guess, guessed_letters):
            continue 
            
        guessed_letters.append(guess)
        
        if guess in word:
            print(f"Good guess! {guess} is in the word!")
            # Update the underscored word display
            word_as_list = list(word_completion)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
                word_as_list[index] = guess
            word_completion = "".join(word_as_list)
        else:
            # Requirement: Reduce attempts on incorrect guess
            print(f"{guess} is not in the word.")
            tries_left -= 1

    # Final visual state display
    draw_hangman(tries_left)
    
    if "_" not in word_completion:
        print(f"WIN! The word was {word}.")
    else:
        print(f"LOSE! The word was {word}.")
    
    # Requirement: Use specific formula for score calculation
    # Score = (number of remaining tries / total number of tries) * 100
    current_score = (tries_left / total_tries) * 100
    print(f"Game Score: {current_score}")
    
    # Update HW0 tracking stats
    game1_count += 1
    game1_avg = ((game1_avg * (game1_count - 1)) + current_score) / game1_count

# --- MENU AND SYSTEM INTEGRATION ---

def game2():
    # Placeholder for Game 2 logic
    global game2_count, game2_avg
    print("This is a placeholder for game 2.")
    game2_count += 1
    game2_avg = ((game2_avg * (game2_count - 1)) + 2.0) / game2_count

def game3():
    # Placeholder for Game 3 logic
    global game3_count, game3_avg
    print("This is a placeholder for game 3.")
    game3_count += 1
    game3_avg = ((game3_avg * (game3_count - 1)) + 3.0) / game3_count

def display_info():
    # Displays total cumulative score and individual game statistics
    total_score = (game1_avg * game1_count) + (game2_avg * game2_count) + (game3_avg * game3_count)
    print(f"\n--- Statistics ---")
    print(f"Total cumulative score: {total_score}")
    print(f"Game1 (Hangman): played {game1_count} times, average score: {game1_avg:.2f}")
    print(f"Game2: played {game2_count} times, average score: {game2_avg:.2f}")
    print(f"Game3: played {game3_count} times, average score: {game3_avg:.2f}")

def print_menu():
    # Displays the menu options
    print("\n--- Game Menu ---")
    print("1. Play Hangman (Game 1)")
    print("2. Play Game 2")
    print("3. Play Game 3")
    print("4. Display Stats")
    print("5. Exit")

def main():
    # Main execution loop for the game system
    print("Welcome to the Multi-Game System")
    print_menu()
    
    while True:
        choice = input("\nSelect an option (0 to see menu): ")
        
        if not choice.isdigit():
            print("Invalid input. Please enter a number.")
            continue
            
        choice = int(choice)

        if choice == 1:
            play_hangman() # Requirement: Integrated as Game 1
        elif choice == 2:
            game2()
        elif choice == 3:
            game3()
        elif choice == 4:
            display_info()
        elif choice == 5:
            print("Goodbye!")
            break
        elif choice == 0:
            print_menu()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()