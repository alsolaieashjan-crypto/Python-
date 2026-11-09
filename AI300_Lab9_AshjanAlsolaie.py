import os

def main():
    
    my_name = "AshjanAlsolaie" 
    initial_filename = f"{my_name}_Lab9.txt"
    
    paragraph = "I want this semester to end as soon as possible!!!"
    
    try:
        # This section creates your file and writes the paragraph automatically
        with open(initial_filename, "w") as f:
            f.write("1\n")  # The first line must be 1
            f.write(paragraph)
        print(f"DONE: Created '{initial_filename}' automatically.")
    except Exception as e:
        print(f"Error creating file: {e}")

    # --- Part 2: Opening and Editing (The end of the script) ---
    while True:
        target_filename = input("\nEnter a filename to open (e.g., AshjanAlsolaie_Lab9.txt): ")
        
        if os.path.exists(target_filename):
            break
        else:
            print(f"Error: '{target_filename}' not found. Please try again.")

    try:
        with open(target_filename, "r") as f:
            lines = f.readlines()

        if not lines:
            print("Error: The file is empty.")
            return

        # Verify the edit count is a valid integer
        try:
            edit_count = int(lines[0].strip())
        except (ValueError, IndexError):
            print("Error: Invalid edit counter format.")
            return

        # Display the file content to the user
        print("\n----- FILE CONTENT -----")
        print("".join(lines[1:]).strip()) 

        # Ask the user for a comment
        user_comment = input("\nEnter a comment about this file: ")
        
        # Update the edit count and append the comment
        new_edit_count = edit_count + 1
        with open(target_filename, "w") as f:
            f.write(f"{new_edit_count}\n")
            f.writelines(lines[1:]) 
            if not lines[-1].endswith('\n'):
                f.write('\n')
            f.write(f"Comment: {user_comment}\n")

        print("\nFile updated successfully!")
        print(f"New edit count = {new_edit_count}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()