# 💸 Expense Tracker Web App (Flask)

A dynamic web application to track your daily expenses with category, time, date, and even uploaded images. Built using **Flask**, **SQLite**, **Chart.js**, and styled with **CSS**.

---

## 📸 Features

- Add expenses with name, amount, category, date & time
- Upload a receipt image for each expense
- View expenses in a table with edit/delete options
- Interactive expense chart (bar graph)
- Stores data in SQLite database (persistent)
- Clean, responsive UI for desktop and mobile

---

## 🛠️ Tech Stack

| Layer       | Technology              |
|-------------|--------------------------|
| Frontend    | HTML, CSS, JavaScript, Chart.js |
| Backend     | Python Flask             |
| Database    | SQLite                   |
| Deployment  | GitHub, Docker, AWS EC2/S3 (Planned) |

---

## 🖼️ Screenshots

![Screenshot](static/demo_screenshot.png) <!-- Replace with your own image -->

---

## 🚀 Getting Started Locally

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/expense-tracker.git
cd expense-tracker


2. Create Virtual Environment

python -m venv venv
venv\Scripts\activate  # For Windows
# source venv/bin/activate  # For Linux/Mac

3. Install Requirements
pip install -r requirements.txt

4. Run the App
python app.py
Visit: http://localhost:5000 in your browser 🚀

📂 Project Structure

expense-tracker/
│
├── app.py
├── expense.db
├── requirements.txt
├── README.md
│
├── static/
│   ├── style.css
│   └── uploads/
│
└── templates/
    ├── index.html
    ├── edit.html


📦 Planned DevOps Integration
CI/CD with Jenkins

Dockerize the app

Deploy on AWS EC2

Optional static hosting via S3
#dummy readme contribution
