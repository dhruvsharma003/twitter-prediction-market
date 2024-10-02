from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('predictions.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT,
            prediction TEXT,
            event TEXT,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_prediction():
    user = request.form['user']
    prediction = request.form['prediction']
    event = request.form['event']

    conn = sqlite3.connect('predictions.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO predictions (user, prediction, event) VALUES (?, ?, ?)', (user, prediction, event))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
