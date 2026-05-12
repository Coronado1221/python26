"""
ASSIGNMENT 12B: SPRINT 5 - DATA PERSISTENCE
Project: Productivity Tracker (The Architect's Vault)
Developer: Anthony
"""
import datetime

# GLOBAL CONSTANTS
TASK_LIST_FILE = "tasks.txt"      
DATA_FILE = "productivity_log.txt" 
REPORT_FILE = "human_report.txt"   
DISTRACTION_LIMIT = 2

def calculate_rates(productive_hours, distracted_hours):
    """Calculates efficiency and potential rates."""
    total_time = productive_hours + distracted_hours
    if total_time == 0:
        return 0, 0
    
    current_rate = (productive_hours / total_time) * 100
    improved_distracted = min(distracted_hours, DISTRACTION_LIMIT)
    improved_total = productive_hours + improved_distracted
    improved_rate = (productive_hours / improved_total) * 100

    return round(current_rate), round(improved_rate)

def save_persistence(name, task, current, improved):
    """Saves to TWO files using the Two-File Pattern."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    
    try:
        # 1. Computer Log: Append mode ('a'), comma-separated
        with open(DATA_FILE, "a") as f:
            f.write(f"{timestamp},{name},{task},{current},{improved}\n")

        # 2. Human Report: Write mode ('w'), pretty formatted
        with open(REPORT_FILE, "w") as f:
            f.write("--- LATEST PRODUCTIVITY SCAN ---\n")
            f.write(f"USER: {name}\n")
            f.write(f"TASK: {task}\n")
            f.write(f"STATS: {current}% Efficiency | {improved}% Potential\n")
            f.write(f"SAVED AT: {timestamp}\n")
            f.write("--------------------------------\n")
            
    except Exception as e:
        print(f"❌ System Error during save: {e}")

def load_categories():
    """Reads task categories from an external file."""
    print("\n--- AVAILABLE CATEGORIES ---")
    try:
        with open(TASK_LIST_FILE, "r") as f:
            for line in f:
                print(f"• {line.strip()}")
    except FileNotFoundError:
        print("⚠️ Warning: tasks.txt not found!")

def main():
    print("--- QUACKEN ARCHIVE ENGINE: PRODUCTIVITY ---")
    name = input("Enter user name: ").title()

    while True:
        load_categories()
        
        task = input("\nSelect a task category (or 'done' to exit): ").title()
        if task == "Done":
            break

        try:
            p_hours = float(input(f"Enter productive hours for '{task}': "))
            d_hours = float(input(f"Enter distracted hours for '{task}': "))

            current, improved = calculate_rates(productive_hours=p_hours, distracted_hours=d_hours)
            
            # FIXED: Using Keyword Arguments for the Golden Rule
            save_persistence(
                name=name, 
                task=task, 
                current=current, 
                improved=improved
            )
            
            print(f"✅ Records updated in {DATA_FILE} and {REPORT_FILE}.")

        except ValueError:
            print("❌ Error: Numeric input required.")

if __name__ == "__main__":
    main()