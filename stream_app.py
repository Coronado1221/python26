import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from blueprint import ProductivityEntry
from db_logic import get_user_id, save_log, get_logs

st.title("Productivity Tracker Dashboard")

# --- User Selection ---
user_name = st.text_input("Enter your name:").title()
if user_name:
    user_id = get_user_id(user_name)
    st.success(f"Welcome, {user_name}!")

    # --- Task Entry ---
    with st.form("log_form"):
        task = st.text_input("Task name:")
        p_hours = st.number_input("Productive hours", min_value=0.0, step=0.25)
        d_hours = st.number_input("Distracted hours", min_value=0.0, step=0.25)
        submitted = st.form_submit_button("Log Entry")
        if submitted and task:
            # Calculate rates
            total = p_hours + d_hours
            current = round((p_hours / total) * 100) if total else 0
            improved = round((p_hours / (p_hours + min(d_hours, 2))) * 100) if (p_hours + min(d_hours, 2)) else 0
            entry = ProductivityEntry(name=user_name, task=task, current=current, improved=improved)
            save_log(user_id, entry, p_hours, d_hours)
            st.success("Entry saved!")

    # --- Logs and Pie Chart ---
    logs = get_logs(user_id)
    if logs:
        df = pd.DataFrame(logs, columns=["Task", "Productive", "Distracted", "Current %", "Improved %", "Timestamp"])
        st.subheader("Your Productivity Log")
        st.dataframe(df)
        # Pie chart for total time spent
        total_productive = df["Productive"].sum()
        total_distracted = df["Distracted"].sum()
        if total_productive + total_distracted > 0:
            fig, ax = plt.subplots()
            ax.pie([total_productive, total_distracted], labels=["Productive", "Distracted"], autopct="%1.1f%%", colors=["#4CAF50", "#F44336"])
            ax.set_title("Time Spent (All Tasks)")
            st.pyplot(fig)
        else:
            st.info("No time logged yet for pie chart.")
    else:
        st.info("No logs found. Start by adding a task!")
else:
    st.info("Enter your name to begin.")
