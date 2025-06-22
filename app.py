from flask import Flask, render_template, request, redirect, url_for, jsonify, send_from_directory
import sqlite3
import string
import random
import os
import qrcode

app = Flask(__name__)
DB_NAME = 'shortener.db'
QR_FOLDER = os.path.join('static', 'qr')
os.makedirs(QR_FOLDER, exist_ok=True)

# ✅ Force base URL to use Wi-Fi IP
LOCAL_BASE_URL = "http://192.168.0.185:5000"

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS urls (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                original_url TEXT NOT NULL,
                short_code TEXT NOT NULL UNIQUE,
                click_count INTEGER DEFAULT 0
            )
        ''')

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    while True:
        short_code = ''.join(random.choices(characters, k=length))
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT 1 FROM urls WHERE short_code = ?", (short_code,))
            if not cursor.fetchone():
                return short_code

def generate_qr_code(data, filename):
    img = qrcode.make(data)
    path = os.path.join(QR_FOLDER, filename)
    img.save(path)
    return path

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['url']
        short_code = generate_short_code()

        # 🔗 Use forced base URL
        base_url = LOCAL_BASE_URL
        short_url = base_url.rstrip('/') + '/' + short_code

        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO urls (original_url, short_code) VALUES (?, ?)", (original_url, short_code))
            conn.commit()

        qr_filename = f"{short_code}.png"
        generate_qr_code(short_url, qr_filename)
        qr_url = url_for('serve_qr', filename=qr_filename)

        return render_template('result.html',
                               short_url=short_url,
                               short_code=short_code,
                               qr_filename=qr_filename,
                               qr_url=qr_url)

    return render_template('index.html')

@app.route('/<short_code>')
def redirect_url(short_code):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT original_url, click_count FROM urls WHERE short_code = ?", (short_code,))
        row = cursor.fetchone()
        if row:
            original_url, clicks = row
            cursor.execute("UPDATE urls SET click_count = ? WHERE short_code = ?", (clicks + 1, short_code))
            conn.commit()
            return redirect(original_url)
        else:
            return "URL not found", 404

@app.route('/clicks/<short_code>')
def get_clicks(short_code):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT click_count FROM urls WHERE short_code = ?", (short_code,))
        row = cursor.fetchone()
        return jsonify({'clicks': row[0] if row else 0})

@app.route('/qr/<filename>')
def serve_qr(filename):
    return send_from_directory(QR_FOLDER, filename)

@app.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == '__main__':
    init_db()
    # ✅ Runs ONLY on your Wi-Fi IP — QR codes will work globally if you deploy
    app.run(host='192.168.0.185', port=5000, debug=True, use_reloader=False)
