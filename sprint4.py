"""
-----------------------------------------------------------------------
ASSIGNMENT 11B: SPRINT 4 - REAL-TIME PERSISTENCE
Project: Productivity Tracker (V4.0)
Developer: Anthony
-----------------------------------------------------------------------
[] 1. Correctly opens file in 'a' mode (Append).
[] 2. Context Manager stays strictly INSIDE the while loop.
[] 3. Data is persisted immediately after gathering input.
[] 4. Follows the "Explain What is Wrong" Protocol for Rule 3.
-----------------------------------------------------------------------
"""
import datetime

# GLOBAL CONSTANTS
LOG_FILE = "productivity_log.txt"
DISTRACTION_LIMIT = 2

def calculate_rates(productive_hours, distracted_hours):
    """Calculate rates and returns TWO values (current, improved)."""
    total_time = productive_hours + distracted_hours
    if total_time == 0:
        return 0, 0
    
    current_rate = (productive_hours / total_time) * 100

    # Logic with Global Constant
    improved_distracted = min(distracted_hours, DISTRACTION_LIMIT)
    improved_total = productive_hours + improved_distracted
    improved_rate = (productive_hours / improved_total) * 100

    return round(current_rate), round(improved_rate)

def main():
    print("--- Productivity Report ---")
    name = input("Enter your name: ").title()

    while True:
        task = input("\nEnter task name (or 'done' to finish): ")
        if task.lower() == 'done':
            print("\nSession complete. Data is safely persisted.")
            break

        try:
            p_hours = float(input(f"Enter productive hours for '{task}': "))
            d_hours = float(input(f"Enter distracted hours for '{task}': "))

            current, improved = calculate_rates(
                productive_hours=p_hours,
                distracted_hours=d_hours)
            
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(LOG_FILE, "a") as file:
                file.write(f"[{timestamp}] USER: {name}\n")
                file.write(f" - Task: {task}\n")
                file.write(f" - Stats: {current}% Current | {improved}% Potential\n")
                file.write("-------------------------------\n")

            print(f" > [Success]: '{task}' calculation and logging complete.")

        except ValueError:
            print(" > [Error]: Numeric input required. Entry skipped.")

main()

