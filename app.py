
from flask import Flask, render_template, request, redirect, url_for

import sqlite3, os
from datetime import datetime

app = Flask(__name__)
DB_FILE = os.path.join(os.path.dirname(__file__), 'attendance.db')


def init_db():  
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS attendance (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT NOT NULL,
                    timestamp TEXT NOT NULL
                )''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mark_attendance', methods=['POST'])
def mark_attendance():
    user_id = request.form.get('user_id')
    if not user_id:
        return "❌ No user_id", 400

    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO attendance (user_id, timestamp) VALUES (?, ?)", (user_id, datetime.now().isoformat(' ', 'seconds')))
    conn.commit()
    conn.close()
    return render_template('suc.html', student_id=user_id)

@app.route('/records')
def records():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM attendance ORDER BY timestamp DESC")
    rows = c.fetchall()
    conn.close()
    return render_template('records.html', rows=rows)


@app.route('/clear_records')
def clear_records():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("DELETE FROM attendance")
    conn.commit()
    conn.close()
    return "<h2 style='color:lime;font-family:monospace;'>🧹 All records cleared.<br><a href='/records'>⬅️ Back to Records</a></h2>"


if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5050, use_reloader=False)
