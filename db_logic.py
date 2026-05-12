import sqlite3
from blueprint import ProductivityEntry
from datetime import datetime

DB_NAME = "productivity.db"

def get_user_id(name):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO users (name) VALUES (?)", (name,))
    conn.commit()
    c.execute("SELECT id FROM users WHERE name = ?", (name,))
    user_id = c.fetchone()[0]
    conn.close()
    return user_id

def save_log(user_id, entry: ProductivityEntry, p_hours, d_hours):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''INSERT INTO logs (user_id, task, productive_hours, distracted_hours, current_rate, improved_rate, timestamp)
                 VALUES (?, ?, ?, ?, ?, ?, ?)''',
              (user_id, entry.task, p_hours, d_hours, entry.current, entry.improved, datetime.now().strftime("%Y-%m-%d %H:%M")))
    conn.commit()
    conn.close()

def get_logs(user_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''SELECT task, productive_hours, distracted_hours, current_rate, improved_rate, timestamp FROM logs WHERE user_id = ? ORDER BY timestamp DESC''', (user_id,))
    logs = c.fetchall()
    conn.close()
    return logs
