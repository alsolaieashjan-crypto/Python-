# Lab 7 algorithm plan
# Ask the user for wall heights separated by commas
# Use a loop and slicing to manually extract numbers between commas
# Turn those slices into integers and add them to the heights list
# If any number is negative, show an error and exit
# If there are fewer than 3 walls, the output will be 0 (because no water can be trapped)
# Start a water counter at 
# For each wall (except first and last):
#  - Find the tallest wall to its left and right using list slicing
#  - Water height = smaller of those two tall walls
#  - If water height > current wall, add the difference to total
# Print final total

def calculate_trapped_water():
    try:
        user_input = input("Enter wall heights separated by commas: ")
        heights = []
        
        # MANUALLY PARSING WITH SLICING
        start = 0
        while True:
            comma_index = user_input.find(',', start)
            if comma_index == -1:
                # No more commas, slice until the end of the string
                heights.append(int(user_input[start:].strip()))
                break
            # Slice from the start position to the comma
            heights.append(int(user_input[start:comma_index].strip()))
            start = comma_index + 1

        # Check for negative numbers
        if any(h < 0 for h in heights):
            print("Error: Heights must be non-negative.") 
            return

        # Need at least 3 walls to hold water
        n = len(heights)
        if n < 3:
            print("Total trapped rainwater: 0 units") 
            return

        total_water = 0

        # Loop through middle walls and use LIST SLICING to find max heights
        for i in range(1, n - 1):
            # heights[:i+1] is a slice of everything to the left
            left_max = max(heights[:i+1])
            
            # heights[i:] is a slice of everything to the right
            right_max = max(heights[i:])
            
            # The water level is limited by the shorter side
            water_level = min(left_max, right_max)
            amount = water_level - heights[i]
            
            if amount > 0:
                total_water += amount

        print(f"Total trapped rainwater: {total_water} units") 

    except ValueError:
        print("Error: Please enter valid integers separated by commas.")

if __name__ == "__main__":
    calculate_trapped_water()