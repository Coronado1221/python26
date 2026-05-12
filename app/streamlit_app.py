# --- User Management ---

import json
import os
from typing import Optional
import streamlit as st
import datetime
import pandas as pd

st.write('App loaded')

# --- CONSTANTS ---
TASK_LIST_FILE = "data/tasks.txt"
DATA_FILE = "data/productivity_log.txt"
USERS_FILE = "data/users.json"

# --- User Class and Helpers ---
class User:
    def __init__(self, user_id: int, name: str, nickname: Optional[str] = None):
        self.id = user_id
        self.name = name
        self.nickname = nickname or name

    def to_dict(self):
        return {"id": self.id, "name": self.name, "nickname": self.nickname}

    @staticmethod
    def from_dict(data):
        return User(user_id=data["id"], name=data["name"], nickname=data.get("nickname"))

def load_users():
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, "r") as f:
        return [User.from_dict(u) for u in json.load(f)]

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump([u.to_dict() for u in users], f, indent=2)

def get_user_by_name(name: str, users):
    for user in users:
        if user.name.lower() == name.lower():
            return user
    return None

def get_next_user_id(users):
    if not users:
        return 1
    return max(u.id for u in users) + 1

def register_or_get_user(name: str, nickname: Optional[str] = None):
    users = load_users()
    user = get_user_by_name(name, users)
    if user:
        return user
    new_id = get_next_user_id(users)
    user = User(user_id=new_id, name=name, nickname=nickname)
    users.append(user)
    save_users(users)
    return user

# --- ProductivityEntry Model ---
class ProductivityEntry:
    def __init__(self, name, task, current=0, improved=0):
        self.name = name
        self.task = task
        self.current = current
        self.improved = improved
    def set_task(self, new_task):
        self.task = new_task
    def set_scores(self, current, improved):
        self.current = current
        self.improved = improved
    def get_summary(self):
        return (f"USER: {self.name}\n"
                f"TASK: {self.task}\n"
                f"STATS: {self.current}% Efficiency | {self.improved}% Potential")

# --- Helper Functions ---
def load_tasks():
    try:
        with open(TASK_LIST_FILE, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

def load_user_entries(user_name):
    try:
        df = pd.read_csv(DATA_FILE, names=["timestamp", "name", "task", "current", "improved"])
        df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
        return df[df["name"].str.lower() == user_name.lower()]
    except Exception:
        return pd.DataFrame(columns=["timestamp", "name", "task", "current", "improved"])

def save_entry(entry_obj):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(DATA_FILE, "a") as f:
        f.write(f"{timestamp},{entry_obj.name},{entry_obj.task},{entry_obj.current},{entry_obj.improved}\n")

def calculate_rates(p_hours, d_hours):
    total = p_hours + d_hours
    if total == 0:
        return 0, 0
    current = round((p_hours / total) * 100)
    improved = round((p_hours / (p_hours + min(d_hours, 2))) * 100)
    return current, improved

def get_efficiency_emoji(eff):
    if eff >= 90:
        return "🔥"
    elif eff >= 70:
        return "😃"
    elif eff >= 50:
        return "🙂"
    elif eff > 0:
        return "😴"
    else:
        return "⚪"

def filter_history(data, task=None, start_date=None, end_date=None):
    if task and task != "All":
        data = data[data["task"] == task]
    if start_date:
        data = data[data["timestamp"] >= start_date]
    if end_date:
        data = data[data["timestamp"] <= end_date]
    return data

# --- Streamlit App Logic ---
st.set_page_config(page_title="Productivity Tracker", page_icon="🚀")

# Theme toggle
theme = st.sidebar.radio("Theme", ["Light", "Dark"])
if theme == "Dark":
    st.markdown("""
        <style>
        body, .stApp { background-color: #222; color: #eee; }
        </style>
    """, unsafe_allow_html=True)

st.title("🚀 Productivity Tracker")

# --- User Session State ---
if 'user' not in st.session_state:
    st.session_state['user'] = None
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

def logout():
    st.session_state['user'] = None
    st.session_state['logged_in'] = False

with st.sidebar:
    if st.session_state['logged_in']:
        st.write(f"👤 User: {st.session_state['user'].nickname} (ID: {st.session_state['user'].id})")
        if st.button("Logout / Switch User"):
            logout()
    else:
        st.header("User Login / Register")
        name = st.text_input("Enter your name:", key="sidebar_name")
        nickname = st.text_input("Display nickname (optional):", key="sidebar_nick")
        if st.button("Login / Register") and name:
            user = register_or_get_user(name, nickname if nickname else None)
            st.session_state['user'] = user
            st.session_state['logged_in'] = True
            st.experimental_rerun()

user = st.session_state['user'] if st.session_state['logged_in'] else None

if user:
    st.success(f"Hello, {user.nickname}! 👋 (ID: {user.id})")
    tasks = load_tasks()
    task_choice = st.selectbox("Select a task:", tasks)
    p_hours = st.number_input("Productive hours:", min_value=0.0, step=0.5)
    d_hours = st.number_input("Distracted hours:", min_value=0.0, step=0.5)
    if st.button("Add Entry ✍️"):
        curr, imp = calculate_rates(p_hours, d_hours)
        entry = ProductivityEntry(name=user.name, task=task_choice, current=curr, improved=imp)
        save_entry(entry)
        st.balloons()
        emoji = get_efficiency_emoji(curr)
        st.success(f"Entry saved! {emoji} {curr}% Efficiency | {imp}% Potential")

    # Show user history with filters
    data = load_user_entries(user.name)
    if not data.empty:
        st.subheader("📊 Your Productivity History")
        # Filtering options
        filter_col1, filter_col2 = st.columns(2)
        with filter_col1:
            task_filter = st.selectbox("Filter by task:", ["All"] + tasks)
        with filter_col2:
            date_range = st.date_input("Date range:", [])
        start_date = date_range[0] if date_range else None
        end_date = date_range[1] if len(date_range) > 1 else None
        filtered = filter_history(data, task=task_filter, start_date=start_date, end_date=end_date)
        st.dataframe(filtered[["timestamp", "task", "current", "improved"]].sort_values("timestamp", ascending=False))
        st.write(f"Average Efficiency: {filtered['current'].mean():.1f}% {get_efficiency_emoji(filtered['current'].mean() if not filtered.empty else 0)}")
        st.write(f"Best Potential: {filtered['improved'].max() if not filtered.empty else 0}% 🌟")
        st.line_chart(filtered.set_index("timestamp")["current"])
        st.bar_chart(filtered.set_index("timestamp")["improved"])
        # Pie chart for task proportions
        if not filtered.empty:
            st.subheader("🧩 Time Spent per Task")
            pie_data = filtered["task"].value_counts()
            st.pyplot(pie_data.plot.pie(autopct="%1.0f%%", ylabel="").get_figure())

        # --- Recent Orders (Entries) ---
        st.sidebar.subheader("🕑 Recent Entries")
        recent = data.sort_values("timestamp", ascending=False).head(5)
        for idx, row in recent.iterrows():
            st.sidebar.write(f"{row['timestamp'].strftime('%Y-%m-%d %H:%M')} | {row['task']} | {row['current']}%")

        # --- Edit/Delete Most Recent Entry ---
        if not data.empty:
            most_recent_idx = data["timestamp"].idxmax()
            most_recent = data.loc[most_recent_idx]
            st.sidebar.markdown("---")
            st.sidebar.write(f"Most Recent: {most_recent['timestamp'].strftime('%Y-%m-%d %H:%M')} | {most_recent['task']} | {most_recent['current']}%")
            edit = st.sidebar.button("✏️ Edit Most Recent")
            delete = st.sidebar.button("🗑️ Delete Most Recent")
            if edit:
                with st.form("edit_form"):
                    new_task = st.selectbox("Edit task:", tasks, index=tasks.index(most_recent['task']) if most_recent['task'] in tasks else 0)
                    new_p = st.number_input("Edit productive hours:", min_value=0.0, value=float(most_recent['current']), step=0.5)
                    new_d = st.number_input("Edit distracted hours:", min_value=0.0, value=0.0, step=0.5)
                    submitted = st.form_submit_button("Save Changes")
                    if submitted:
                        # Update entry in file
                        df = pd.read_csv(DATA_FILE, names=["timestamp", "name", "task", "current", "improved"])
                        df.loc[most_recent_idx, "task"] = new_task
                        df.loc[most_recent_idx, "current"] = new_p
                        # Recalculate improved
                        _, new_imp = calculate_rates(new_p, new_d)
                        df.loc[most_recent_idx, "improved"] = new_imp
                        df.to_csv(DATA_FILE, header=False, index=False)
                        st.success("Most recent entry updated!")
                        st.experimental_rerun()
            if delete:
                if st.sidebar.confirm("Are you sure you want to delete your most recent entry?", key="delete_confirm"):
                    df = pd.read_csv(DATA_FILE, names=["timestamp", "name", "task", "current", "improved"])
                    df = df.drop(most_recent_idx)
                    df.to_csv(DATA_FILE, header=False, index=False)
                    st.success("Most recent entry deleted!")
                    st.experimental_rerun()
    else:
        st.info("No entries yet. Add your first productivity record!")
