from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for flashing messages

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def init_db():
    conn = sqlite3.connect('expense.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    amount REAL NOT NULL,
                    category TEXT NOT NULL,
                    date TEXT NOT NULL,
                    time TEXT NOT NULL,
                    image TEXT)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    conn = sqlite3.connect('expense.db')
    c = conn.cursor()
    c.execute("SELECT * FROM expenses ORDER BY date")
    expenses = c.fetchall()
    conn.close()

    dates = [row[4] for row in expenses]
    amounts = [row[2] for row in expenses]

    return render_template('index.html', expenses=expenses, dates=dates, amounts=amounts)

@app.route('/add', methods=['POST'])
def add_expense():
    name = request.form['name']
    amount = request.form['amount']
    category = request.form['category']
    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H:%M:%S")

    image = request.files.get('image')
    filename = None
    if image and image.filename != '':
        if allowed_file(image.filename):
            filename = secure_filename(image.filename)
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            flash("Invalid image file type. Allowed types: png, jpg, jpeg, gif")
            return redirect(url_for('index'))

    conn = sqlite3.connect('expense.db')
    c = conn.cursor()
    c.execute("INSERT INTO expenses (name, amount, category, date, time, image) VALUES (?, ?, ?, ?, ?, ?)",
              (name, amount, category, date, time, filename))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_expense(id):
    # Optionally delete image file from disk too (not required but cleaner)
    conn = sqlite3.connect('expense.db')
    c = conn.cursor()
    c.execute("SELECT image FROM expenses WHERE id=?", (id,))
    row = c.fetchone()
    if row and row[0]:
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], row[0])
        if os.path.exists(image_path):
            os.remove(image_path)

    c.execute("DELETE FROM expenses WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
