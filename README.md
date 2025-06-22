# 🔗 URL Shortener with QR Code

An interactive web app that shortens long URLs, generates **QR codes**, and tracks click statistics — built using **Flask**, **SQLite**, and **Vanilla JavaScript**.

🧠 Ideal for sharing compact links with added scan-ability and real-time analytics.

---

## 🚀🚀🚀 LIVE DEMO

👉👉👉 **[🔗 CLICK HERE TO TRY THE APP LIVE!](https://vikasravuru.pythonanywhere.com)** 👈👈👈

> Paste your long URL ➜ Get a short one ➜ Scan or share instantly!

---

## 🎯 What This Project Does

🔹 Allows users to:

- Enter a **long URL** and get a **shortened version**
- Auto-generate and display a **QR Code**
- Track the number of **clicks** on the short link
- **Download** the QR Code as an image
- **Test** the short URL instantly in a new tab

🔹 Also includes:

- Stylish and responsive UI
- Toast notifications for better UX
- Short codes stored in an SQLite DB
- Each short link redirects with click tracking

---

## 💼 Use Cases

- ✅ Sharing URLs via print or SMS using QR codes
- ✅ Masking long or messy links for presentations
- ✅ Creating trackable promotional links
- ✅ Generating smart QR flyers and posters

---

## 🧱 Tech Stack

| Tech              | Purpose                              |
|------------------|---------------------------------------|
| **Flask**         | Web Framework (Python)               |
| **SQLite**        | Lightweight database                 |
| **HTML/CSS**      | Frontend UI layout & styles          |
| **JavaScript**    | Frontend interactions & feedback     |
| **qrcode (Python)**| QR Code generation                  |
| **PythonAnywhere**| Cloud Hosting Platform               |

---

## 🧩 Folder Structure

url_shortener/

├── app.py # 🚀 Main Flask app logic

├── shortener.db # 🧱 SQLite database

├── requirements.txt # 📦 Python dependencies

├── templates/ # 🧾 HTML templates

               ├── index.html # 🔗 Input page

               └── result.html # ✅ Result page with QR
  
├── static/

               ├── style.css # 💅 Styling

               ├── script.js # ⚙️ Frontend logic

               └── qr/ # 📁 QR Code image output

