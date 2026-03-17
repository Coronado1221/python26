"""
Assignment 9B: Sprint 2 - Functional Stubs
Project: Productivity Tracker (V1.0)
Developer: Anthony
"""

# Constants
LOG_FILE = "productivity_log.txt"

def get_info():
    """Ask for user name and available hours"""
    # TODO: Ask for user's name and available hours
    return "Anthony", 17

def collect_data():
    """Collects productive and distracted hours."""
    # TODO: Get study, work, workout hours
    # TODO: Get social media, gaming, TV and other distracted hours

    # Placeholder so function after receives data
    activity_data = {}

    return activity_data

def calculate_productivity(activity_data):
    """Calculates productivity rate and improvement."""
    # TODO: Calculate total productive time
    # TODO: Calculate total distraction time
    # TODO: Calculate productivity percentage
    # TODO: Calculate productivity if distractions limited

    return 74, 87

def save_data_and_report(user, productivity_rates):
    """Saves data to log file and print the human file."""
    # TODO: Add data entry to productivity_log.txt
    # TODO: Print productivity report for user
    pass

def main():
    # 1. Identity Phases
    name, hours = get_info()
    print(f"User: {name} | Available Hours: {hours}")

    # 2. Data Collection Phase
    activity_data = collect_data()

    # 3. Calculation Phase
    productivity_results = calculate_productivity(activity_data)

    # 4. Handoff Phase
    save_data_and_report(name, productivity_results)

main()

                         