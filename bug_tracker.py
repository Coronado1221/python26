"""
-----------------------------------------------------------------------
ASSIGNMENT 11A REVISED: THE BUG TRACKING LOG
-----------------------------------------------------------------------
[ ] 1. Program uses a while loop to keep asking for bugs.
[ ] 2. Uses the datetime module to get a timestamp format.
[ ] 3. Stores the timestamp, file name, description, and priority in a dictionary.
[ ] 4. Uses `with open("bug_log.txt", "a")` to append to the file safely.
[ ] 5. The bug_log.txt file is formatted neatly with newlines.
-----------------------------------------------------------------------
"""
import datetime

def get_bug_input():
    """ Collect data and handle user input."""
    file_name = input("File name: ")
    description = input("Description of error: ")
    priority = input("Priority (High, Medium, Low): ")
    return file_name, description, priority 

def save_bug_to_file(timestamp, data_list):
    """Handle writing to text file."""
    with open("bug_log.txt", "a") as file:
        log_entry = f"""[{timestamp}]
File: {data_list[0]}
Status: {data_list[1]}
Priority: {data_list[2]}
-------------------------------\n"""
        file.write(log_entry)

def main():
    """Manage the loop and handoff."""
    bug_data = {}

    while True:
        user_choice = input("Enter 'log' to record a bug, or 'quit' to stop: ").lower().strip()

        if user_choice == 'quit':
            print("Bug log updated")
            break

        elif user_choice == 'log':
            # 1. Collection Phase
            file_name, description, priority = get_bug_input()

            # 2. Processing Phase
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            bug_data[timestamp] = [file_name, description, priority]

            # 3. Persistance Phase
            save_bug_to_file(timestamp=timestamp, data_list=bug_data[timestamp])

        else: 
            print("Invalid input. Please type 'log' or 'quit'.")

if __name__ == "__main__":   
    main()
