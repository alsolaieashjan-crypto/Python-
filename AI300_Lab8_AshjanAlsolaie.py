import random

# ---------- SETUP ----------
n = int(input("Enter grid size (n): "))

# Tuple for starting position
start_pos = (0, 0)

# Dictionary for player info
player = {"pos": start_pos, "path": [start_pos]}

# Generate random star position
green_star = (random.randint(0, n - 1), random.randint(0, n - 1))

# Make sure star is not on player start
while green_star == start_pos:
    green_star = (random.randint(0, n - 1), random.randint(0, n - 1))

# Store stars in a dictionary
stars = {"G": green_star}

# Create random blocks stored in a list of tuples
num_blocks = n
blocks = [] 

while len(blocks) < num_blocks:
    block_pos = (random.randint(0, n - 1), random.randint(0, n - 1))
    # Ensure blocks don't land on player or star
    if block_pos != start_pos and block_pos not in stars.values() and block_pos not in blocks:
        blocks.append(block_pos)

# ---------- FUNCTION TO PRINT GRID ----------
def print_grid():
    for r in range(n):
        for c in range(n):
            pos = (r, c) 
            if pos == player["pos"]:
                print("P", end=" ")
            elif pos == stars["G"]:
                print("G", end=" ")
            elif pos in blocks:
                print("#", end=" ")
            elif pos in player["path"]:
                print("*", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

# ---------- GAME ----------
print("\nLegend:")
print("P = Player, G = Green Star")
print("* = Path Trail, # = Blocked Wall\n")

print("Starting Grid:")
print_grid()

# Take user input for movement
steps = input("Enter your path using WASD (example: wddssa): ").lower()

# Movement dictionary
moves = {
    "w": (-1, 0), # Up
    "s": (1, 0),  # Down
    "a": (0, -1), # Left
    "d": (0, 1)   # Right
}

for step in steps:
    if step not in moves:
        continue

    dr, dc = moves[step]
    r, c = player["pos"]
    new_pos = (r + dr, c + dc)

    # Check bounds
    if not (0 <= new_pos[0] < n and 0 <= new_pos[1] < n):
        continue

    # Check if the player hit a blocked wall
    if new_pos in blocks:
        continue

    # Update player position and path trail
    player["pos"] = new_pos
    player["path"].append(new_pos)

    # Check win condition
    if new_pos == stars["G"]:
        print("You reached the GREEN star!")
        break
else:
    print("You did not reach a star.")

# Final output
print("\nFinal Grid:")
print_grid()
