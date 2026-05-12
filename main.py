import datetime
from blueprint import ProductivityEntry # Import your Suitcase!

# GLOBAL CONSTANTS
TASK_LIST_FILE = "tasks.txt"      
DATA_FILE = "productivity_log.txt" 
REPORT_FILE = "human_report.txt"   

def calculate_rates(p_hours, d_hours):
    total = p_hours + d_hours
    if total == 0: return 0, 0
    current = round((p_hours / total) * 100)
    # simplified improved logic for brevity
    improved = round((p_hours / (p_hours + min(d_hours, 2))) * 100)
    return current, improved

def save_to_vault(entry_obj):
    """Saves the Object data to files."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    try:
        # 1. Log (Raw Data)
        with open(DATA_FILE, "a") as f:
            f.write(f"{timestamp},{entry_obj.name},{entry_obj.task},{entry_obj.current},{entry_obj.improved}\n")

        # 2. Report (Using the Object's own display method)
        with open(REPORT_FILE, "w") as f:
            f.write(f"--- SPRINT 6 ARCHIVE: {timestamp} ---\n")
            f.write(entry_obj.get_summary()) # Call the object's method!
            
    except Exception as e:
        print(f"❌ Persistence Error: {e}")

def main():
    print("--- THE MODULAR ENGINE: PRODUCTIVITY ---")
    user_name = input("Enter user name: ").title()
    
    # Create the Object (The Suitcase)
    # We initialize with placeholder task/scores
    current_entry = ProductivityEntry(name=user_name, task="None")

    while True:
        task_choice = input("\nEnter task (or 'done'): ").title()
        if task_choice == "Done": break

        try:
            p_hours = float(input("Productive hours: "))
            d_hours = float(input("Distracted hours: "))
            curr, imp = calculate_rates(p_hours, d_hours)

            # Use SETTERS to update the object
            current_entry.set_task(new_task=task_choice)
            current_entry.set_scores(current=curr, improved=imp)

            # Pass the WHOLE OBJECT to the saver
            save_to_vault(entry_obj=current_entry)
            print("✅ Object state persisted.")

        except ValueError:
            print("❌ Invalid input.")

if __name__ == "__main__":
    main()
    