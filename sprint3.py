"""
Assignment 10B Sprint 3 - Factoring & DATA ACCOUNTABILITY
Project Productivity Tracker (V2.0)
Developer Anthony
"""

# Global Constants
LOG_FILE = "productivity_log.txt"
DISTRACTION_LIMIT = 2

def get_user_info():
    """Ask for name and available hours."""
    name = input("Enter your name: ").title()
    hours = input("Enter available hours: ")
    return name, hours

def collect_data():
    """Collect hours, productive and distracted."""
    study = int(input("Study hours: "))
    work = int(input("Work hours: "))
    workout = int(input("Workout hours: "))
    social = int(input("Social media hours: "))
    gaming = int(input("Gaming hours: "))
    tv = int(input("TV hours: "))
    return {"study": study, "work": work, "workout": workout, "social": social, "gaming": gaming, "tv": tv}

def calculate_productivity(activity_data):
    """Calculates productivity rate."""
    productive = (activity_data["study"] + activity_data["work"] + activity_data["workout"])
    distracted = (activity_data["social"] + activity_data["gaming"] + activity_data["tv"])
    total_time = productive + distracted
    if total_time == 0:
        return 0, 0
    productivity_rate = (productive / total_time) * 100

    # Improve,emt calculations
    improved_distracted = min(distracted, DISTRACTION_LIMIT)
    improved_total = productive + improved_distracted
    improved_rate = (productive / improved_total) * 100
    return round(productivity_rate), round(improved_rate)

def save_data_and_report(user, productivity_rates):
    current, improved = productivity_rates
    # Print report
    print("\n--- PRODUCTIVITY REPORT ---")
    print(f"User: {user}")
    print(f"Current Productivity: {current}%")
    print(f"Improved Productivity: {improved}%")

def main():
    # 1. Identity Phase
    name, hours = get_user_info()

    # 2. Data Collection Phase
    activity_data = collect_data()

    # 3. Calculation Phase
    productivity_results = calculate_productivity(activity_data)

    # 4. Handoff Phase (Using KEYWORD ARGUMENTS)
    save_data_and_report(user=name, productivity_rates=productivity_results)

main()






