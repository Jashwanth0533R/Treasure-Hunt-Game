# 🏴‍☠️ Treasure Hunt Game

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightblue?logo=sqlite)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-orange?logo=pandas)
![HTML](https://img.shields.io/badge/Frontend-HTML5-orange?logo=html5)
![CSS](https://img.shields.io/badge/CSS3-1572B6?logo=css3)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-Academic-lightgrey)

---

## 📌 Project Overview

Treasure Hunt Game is an interactive web-based puzzle and quiz game developed using Flask, SQLite, HTML, CSS, and JavaScript.

The game dynamically loads questions from a CSV dataset into an SQLite database and presents them to players based on age groups.

The project focuses on:

- Interactive Gameplay
- Dynamic Question Loading
- Database Integration
- Backend Development
- Real-Time Question Retrieval
- Responsive User Interface

The application provides an engaging treasure hunt experience where users solve questions and progress through different game stages.

---

## 🚀 Key Features

- 🎮 Interactive Treasure Hunt Gameplay
- 🧠 Dynamic Quiz Question System
- 👦 Age-Based Question Selection
- 💾 SQLite Database Integration
- 📂 CSV-to-Database Automatic Loading
- 🌐 Flask Backend Routing
- ⚡ Real-Time Question Retrieval
- 📱 Responsive Frontend Interface

---

## 🧠 System Workflow

1. User enters player information
2. Flask application starts game session
3. Questions are fetched from SQLite database
4. Questions are filtered based on age group
5. User answers questions interactively
6. Game progresses dynamically

---

## 🏗️ Technology Stack

### Backend
- Python 3
- Flask
- SQLite

### Frontend
- HTML
- CSS
- JavaScript

### Data Processing
- Pandas

### Database
- SQLite3

### Tools
- VS Code
- GitHub

---

## 📂 Project Structure

```bash
Treasure-Hunt-Game/
│
├── app.py
├── load_data.py
├── questions.csv
├── requirements.txt
├── README.md
│
├── database/
│   └── questions.db
│
├── templates/
│   ├── index.html
│   └── game.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       ├── index.js
│       └── game.js
│
└── assets/
```

---

## 📥 Dataset Information

The project uses a CSV dataset containing quiz questions.

### Dataset File

```bash
questions.csv
```

The CSV file is automatically converted into SQLite database format using:

```bash
load_data.py
```

---

## 📊 CSV Dataset Format

Example structure:

```csv
question,options,answer,age_group
"What has keys but can't open locks?","Keyboard;Clock;Book;Phone","Keyboard","kids"
```

### Required Fields

- question
- options
- answer
- age_group

---

## ⚙️ Local Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Jashwanth0533R/Treasure-Hunt-Game.git

cd Treasure-Hunt-Game
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 Create requirements.txt

If requirements file is missing:

```bash
pip freeze > requirements.txt
```

---

## 🗄️ Create SQLite Database

Before running the application, delete any corrupted or empty database file:

```bash
database/questions.db
```

Then generate fresh database using:

```bash
python load_data.py
```

Expected Output:

```text
✅ Success! Loaded questions into database/questions.db
```

---

## ▶️ Run Application

```bash
python app.py
```

---

## 🌐 Open in Browser

```text
http://127.0.0.1:5000
```

---

## 🎮 Gameplay Instructions

1. Enter player details
2. Select/start game
3. Questions are loaded dynamically
4. Answer questions correctly
5. Progress through treasure hunt stages

---

## 💾 Database Workflow

```text
questions.csv
        ↓
load_data.py
        ↓
questions.db
        ↓
Flask app.py
        ↓
Frontend Game UI
```

---

## 🔐 Backend Features

- Flask Routing
- Dynamic API Responses
- SQLite Query Execution
- Real-Time Question Retrieval
- Age-Based Filtering

---

## 📈 Future Enhancements

- 🏆 Leaderboard System
- ⏳ Timer-Based Challenges
- 🎵 Sound Effects
- 🌍 Multiplayer Treasure Hunt
- 📍 GPS-Based Treasure Hunt
- 🤖 AI-Generated Questions
- 📱 Mobile Responsive Design
- 🧩 Difficulty Levels

---

## 💡 Learning Outcomes

Through this project, I gained practical experience in:

- Flask Backend Development
- SQLite Database Integration
- CSV Data Processing
- API Development
- Frontend-Backend Communication
- Dynamic Game Logic
- Full Stack Development

---

## 👨‍💻 Author

### Jashwanth Kumar Gutta

AI & ML Student | Python Developer | Backend Developer

📧 Email:  
gjashwanthkumar711@gmail.com

🔗 GitHub:  
https://github.com/Jashwanth0533R

🔗 LinkedIn:  
https://www.linkedin.com/in/jashwanth-kumar-g-431477383/

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---

## 📜 License

Developed for educational and academic purposes only.
