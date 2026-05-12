"""
Blueprint for Productivity Entries
"""

class ProductivityEntry:
    def __init__(self, name, task, current=0, improved=0):
        # Attributes
        self.name = name
        self.task = task
        self.current = current
        self.improved = improved

    # --- SETTER METHODS ---
    def set_task(self, new_task):
        self.task = new_task

    def set_scores(self, current, improved):
        self.current = current
        self.improved = improved

    # --- DISPLAY METHOD ---
    def get_summary(self):
        """Returns a formatted string for the Human Report."""
        return (f"USER: {self.name}\n"
                f"TASK: {self.task}\n"
                f"STATS: {self.current}% Efficiency | {self.improved}% Potential")