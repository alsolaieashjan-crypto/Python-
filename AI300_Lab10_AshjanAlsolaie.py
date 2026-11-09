# Missionaries and Cannibals
# OOP Version with Shore + game classes
# Run: python game.py

#*************************************** Start Of Task 1 : Defining classes *****************************************
#TODO: Write the header to create a class named Shore
class Shore:
#*************************************** End Of Task 1 *****************************************

    #*************************************** Start Of Task 2: initializing attributes ***********************************
    #TODO: Write a method that takes 3 parameters
    # and uses them to set the attributes m, c, and name respectively, 
    # where m is the number of missionarieson the shore, c is the number of Cannibals, and name is the shore name. 
    def __init__(self, m, c, name):
        self.m = m
        self.c = c
        self.name = name
    #*************************************** End Of Task 2*****************************************

    def remove(self, m, c):
        """Remove m mercenaries and c commissioners from this shore."""
        self.m -= m
        self.c -= c

    #*************************************** Start Of Task 3: Writing Methods *****************************************
    #TODO: write a method named add that takes 2 parameters, m and c, 
    # and increments the number of missionaries by m, and the canabals by c. 
    def add(self, m, c):
        self.m += m
        self.c += c
    #*************************************** End Of Task 3*****************************************

    def is_safe(self):
        """Safe if mercenaries are not outnumbered (unless m == 0)."""
        #*************************************** Start Of Task 4: More methods *****************************************
        #TODO: complete the method is_safe to return True if the missonaries are 0 
        # or if they are not outnumbered.  
        return self.m == 0 or self.m >= self.c
        #*************************************** End Of Task 4 *****************************************

    def __str__(self):
        # 12 underscores total, fill with M and C
        m_str = "M" * self.m
        c_str = "C" * self.c
        inside = (m_str + "_" + c_str).ljust(7, "_")  # total inside length 10
        return f"_{inside}_"


class Game:
    
    #*************************************** Start Of Task 5: Composition *****************************************
    # TODO: Write the game class initializor where a game is COMPOSED of the following: 
    # shores: and array of the left and right shores, in order
    # current_shore :  the crrent position of the boat, 0 if at the left shore, 1 if at the right. 
    # num_moves: number of times the boat has been moved. 
    def __init__(self):
        self.shores = [Shore(3, 3, "Left"), Shore(0, 0, "Right")]
        self.current_shore = 0
        self.num_moves = 0
    #*************************************** End Of Task 5 *****************************************
    
    def other_shore_index(self):
        return 1 if self.current_shore == 0 else 0

    def is_legal_move(self, m, c):
        if m < 0 or c < 0 or m + c < 1 or m + c > 2:
            return False
        #*************************************** Start Of Task 6: Accessing list attributes *****************************************
        # TODO: Write code that returns False if the current shore 
        # has less than m Missionaries or less than c Canables.  
        if self.shores[self.current_shore].m < m or self.shores[self.current_shore].c < c:
            return False
        #*************************************** End Of Task 6 *****************************************
        return True
        
    #*************************************** Start Of Task 7: Using methods *****************************************
    # TODO : Define a method named move that takes 2 parameters (m and c) 
    # if m,c is an illegal move, it returns false. 
    # Else, it moves m missionaries and c cannables from the current shore, adds them to the next shore
    # and updates the current shore and the number of moves. 
    def move(self, m, c):
        if not self.is_legal_move(m, c):
            return False
        
        destination_shore = self.other_shore_index()
        
        # Move people
        self.shores[self.current_shore].remove(m, c)
        self.shores[destination_shore].add(m, c)
        
        # Update game state
        self.current_shore = destination_shore
        self.num_moves += 1
        return True
    #*************************************** End Of Task 7 *****************************************

    def draw(self):
        boat_icon = "🚣"
        shore_left = "🏝️"
        shore_right = "🏝️"
        water = "🌊🌊🌊🌊🌊🌊"
    
        if self.current_shore == 0:
            print(f"{shore_left} {self.shores[0]}  {boat_icon} {water}  {self.shores[1]} {shore_right}")
        else:
            print(f"{shore_left} {self.shores[0]}  {water} {boat_icon}  {self.shores[1]} {shore_right}")
    
        print(f"Moves: {self.num_moves}")

    def has_won(self):
        return self.shores[1].m == 3 and self.shores[1].c == 3
        
    def has_lost(self):
        return not self.shores[1].is_safe() or not self.shores[0].is_safe()

    def play(self):
        print("MISSIONARIES & CANNIBALS (Mercenaries M, Commissioners C)")
        print("Boat holds 1 or 2 people.")
        print("If Commissioners outnumber Mercenaries on a shore, you lose.\n")

        while True:
            self.draw()

            if self.has_won():
                print("\n🎉 YOU WIN! Everyone crossed safely.")
                break
            if self.has_lost():
                print("\n 💀 YOU LOSE! The CANNIBALS outnumbered the Missionaries on one shore. .")
                break
                
            cmd = input("\nEnter move (m, mm, c, cc, mc) or 'quit': ").strip().lower()

            if cmd == "quit":
                print("Game ended.")
                break
                
            # Convert shorthand command into (m, c)
            if cmd == "m":
                m, c = 1, 0
            elif cmd == "mm":
                m, c = 2, 0
            elif cmd == "c":
                m, c = 0, 1
            elif cmd == "cc":
                m, c = 0, 2
            elif cmd in ["mc", "cm"]:
                m, c = 1, 1
            else:
                print("Invalid move. Use: m, mm, c, cc, mc")
                continue

            success = self.move(m, c)

            if not success:
                print("\n Illegal move! Try again.")
                # self.draw() # Removed duplicate draw call for cleaner flow


if __name__ == "__main__":
    game = Game()
    game.play()