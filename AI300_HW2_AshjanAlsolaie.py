import random

# ============================================================
# DATA STRUCTURE: Nested Dictionary for Statistics
# ============================================================
# Stores count and average for all three games as required [cite: 35, 40]
stats = {
    "game1": {"count": 0, "avg": 0.0},
    "game2": {"count": 0, "avg": 0.0},
    "game3": {"count": 0, "avg": 0.0}
}

# ============================================================
# GAME 1: HANGMAN (From HW1)
# ============================================================

def select_word():
    words = ["BANANA", "PYTHON", "COMPUTER", "ALGORITHM", "SCIENCE", "STUDENT"]
    return random.choice(words)

def is_valid_guess(guess, guessed_letters):
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
        return False
    if guess.upper() in guessed_letters:
        print(f"You already guessed '{guess.upper()}'. Try another letter.")
        return False
    return True

def draw_hangman(tries_left):
    stages = [
        "\n  ––––\n  |      |\n  |      O\n  |     /|\\\n  |     / \\\n  -",
        "\n  ––––\n  |      |\n  |      O\n  |     /|\\\n  |     /\n  -",
        "\n  ––––\n  |      |\n  |      O\n  |     /|\\\n  |\n  -",
        "\n  ––––\n  |      |\n  |      O\n  |     /|\n  |\n  -",
        "\n  ––––\n  |      |\n  |      O\n  |      |\n  |\n  -",
        "\n  ––––\n  |      |\n  |      O\n  |\n  |\n  -",
        "\n  ––––\n  |      |\n  |\n  |\n  |\n  -"
    ]
    print(stages[tries_left])

def play_hangman():
    word = select_word()
    guessed_letters = []
    total_tries = 6
    tries_left = total_tries
    word_completion = "_" * len(word)

    print("\n---------- HANGMAN ----------")

    while tries_left > 0 and "_" in word_completion:
        draw_hangman(tries_left)
        print(f"Word: {' '.join(word_completion)}")
        print(f"Guessed letters: {' '.join(guessed_letters)}")
        guess = input("Please guess a letter: ").upper()

        if not is_valid_guess(guess, guessed_letters):
            continue

        guessed_letters.append(guess)
        if guess in word:
            print(f"Good guess! {guess} is in the word!")
            word_as_list = list(word_completion)
            for i, letter in enumerate(word):
                if letter == guess:
                    word_as_list[i] = guess
            word_completion = "".join(word_as_list)
        else:
            print(f"{guess} is not in the word.")
            tries_left -= 1

    draw_hangman(tries_left)
    if "_" not in word_completion:
        print(f"WIN! The word was {word}.")
    else:
        print(f"LOSE! The word was {word}.")

    # Score calculation for Hangman
    current_score = (tries_left / total_tries) * 100
    print(f"Game Score: {current_score:.2f}")

    # Update Nested Dictionary [cite: 34]
    stats["game1"]["count"] += 1
    n = stats["game1"]["count"]
    stats["game1"]["avg"] = ((stats["game1"]["avg"] * (n - 1)) + current_score) / n

# ============================================================
# GAME 2: TIC TAC TOE (HW2)
# ============================================================

def draw_grid(grid):
    """Displays 3x3 grid using a list [cite: 26, 31]"""
    print("\nCurrent Grid:")
    print("    1   2   3")
    for row in range(3):
        print(f"{row + 1} ", end="")
        for col in range(3):
            cell = grid[row * 3 + col]
            print(f" {cell if cell != ' ' else ' '} ", end="")
            if col < 2:
                print("|", end="")
        print()
        if row < 2:
            print("   ---+---+---")
    print()

def check_winner(grid):
    """Returns 2 (WIN), 1 (TIE), 0 (LOSE), -1 (ongoing) [cite: 28]"""
    win_lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6],
    ]
    for line in win_lines:
        v = [grid[i] for i in line]
        if v[0] != ' ' and v[0] == v[1] == v[2]:
            return 2 if v[0] == 'X' else 0
    return 1 if ' ' not in grid else -1

def is_valid_step(user_input, grid, current_turn):
    """Validates input format and move rules [cite: 29, 30]"""
    parts = user_input.strip().upper().split(',')
    if len(parts) != 3:
        print("Invalid format. Use LETTER,ROW,COL (example: X,2,3)")
        return False
    
    letter, r_s, c_s = parts
    if letter not in ('X', 'O'):
        print("Invalid letter. Use X or O.")
        return False
    if letter != current_turn:
        print(f"It is {current_turn}'s turn. You cannot play {letter}.")
        return False
    if not r_s.isdigit() or not c_s.isdigit():
        print("Row and column must be numbers.")
        return False
    
    r, c = int(r_s), int(c_s)
    if not (1 <= r <= 3 and 1 <= c <= 3):
        print("Row and column must be 1-3.")
        return False
    
    if grid[(r-1)*3 + (c-1)] != ' ':
        print("Cell is already taken. Try again.")
        return False
    return True

def computer_play(grid, comp_letter, player_letter):
    """AI for extra credit [cite: 42]"""
    lines = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    def find(l):
        for line in lines:
            v = [grid[i] for i in line]
            if v.count(l) == 2 and v.count(' ') == 1:
                return line[v.index(' ')]
        return None
    
    move = find(comp_letter) or find(player_letter)
    if move is not None: return move
    if grid[4] == ' ': return 4
    for i in [0, 2, 6, 8]:
        if grid[i] == ' ': return i
    return grid.index(' ')

def play_TicTacToe():
    """Main Tic Tac Toe logic [cite: 27]"""
    print("\n--- TIC TAC TOE ---")
    print("Enter moves like: X,2,3 or O,1,1")
    
    mode = input("Play against computer? (y/n): ").lower()
    vs_computer = (mode == 'y')
    grid = [' '] * 9
    
    # First move decides Player 1's identity
    while True:
        draw_grid(grid)
        move = input("Player 1, enter your first move: ").strip().upper()
        parts = move.split(',')
        if len(parts) == 3 and is_valid_step(move, grid, parts[0]):
            p1_letter = parts[0]
            p2_letter = 'O' if p1_letter == 'X' else 'X'
            grid[(int(parts[1])-1)*3 + (int(parts[2])-1)] = p1_letter
            break
        print("Invalid first move.")

    turn_order = [p1_letter, p2_letter]
    current_idx = 1 # Player 2 goes next

    while True:
        draw_grid(grid)
        result = check_winner(grid)
        if result != -1: break

        current_letter = turn_order[current_idx]
        if vs_computer and current_letter == 'O':
            print("Computer is thinking...")
            idx = computer_play(grid, 'O', 'X')
            grid[idx] = 'O'
        else:
            prompt = f"Player {'1' if current_letter == p1_letter else '2'} ({current_letter}), enter your move: "
            move = input(prompt)
            if not is_valid_step(move, grid, current_letter): continue
            parts = move.strip().upper().split(',')
            grid[(int(parts[1])-1)*3 + (int(parts[2])-1)] = current_letter
        
        current_idx = 1 - current_idx

    # Scoring formula [cite: 23, 24, 25]
    if result == 2: print("WIN"); score = 100
    elif result == 0: print("LOSE"); score = 0
    else: print("TIE"); score = 50

    # Update Nested Dictionary [cite: 34]
    stats["game2"]["count"] += 1
    n = stats["game2"]["count"]
    stats["game2"]["avg"] = ((stats["game2"]["avg"] * (n - 1)) + score) / n

# ============================================================
# MENU AND STATISTICS
# ============================================================

def display_info():
    """Displays average score and play count [cite: 34, 38, 39]"""
    total_score = sum(stats[g]["avg"] * stats[g]["count"] for g in stats)
    print(f"\n— Statistics —")
    print(f"Total cumulative score: {total_score:.2f}")
    for g in ["game1", "game2", "game3"]:
        print(f"{g.capitalize()}: played {stats[g]['count']} times, average score: {stats[g]['avg']:.2f}")

def main():
    while True:
        print("\nSelect the option you want by typing its number")
        print("1. Game 1 (Hang Man)")
        print("2. Game 2 (Tic Tac Toe)")
        print("3. Game 3 (Coming soon..)")
        print("4. Display info")
        print("5. Exit")
        
        choice = input()
        if choice == '1': play_hangman()
        elif choice == '2': play_TicTacToe()
        elif choice == '3': print("Game 3 is not available yet.")
        elif choice == '4': display_info()
        elif choice == '5': break
        else: print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

