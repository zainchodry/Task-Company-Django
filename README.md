# 🧑‍💼 Team Task Tracker — Project & Daily Report System

A Django-based web application where **Team Leads** can assign projects and daily tasks to **Team Members**, and team members can submit their daily work reports.

---

## 🚀 Features

- 🔐 User authentication (Sign up, Login, Logout)
- 📋 Team Lead can:
  - Create projects
  - Assign tasks to users
  - View tasks submitted by the team
- 🧑‍💻 Team Member can:
  - View assigned tasks
  - Submit daily report for a task
  - Automatically mark task as completed when report is submitted
- 🗓️ Tracks `created_at`, `due_date`, and `completed_at`
- 📊 Dashboard view with all relevant projects and tasks

---

## 🛠️ Tech Stack

- Python 3.x
- Django 4.x
- SQLite3 (can be replaced with PostgreSQL)
- Bootstrap 5 (for responsive UI)

---

## 📂 Project Structure

team_tracker/
├── tracker/ # Main app
│ ├── models.py # Project, Task, Report models
│ ├── views.py # Core logic (dashboard, forms, reports)
│ ├── forms.py # Django ModelForms
│ ├── urls.py # App-level routes
│ └── templates/ # HTML files
├── team_tracker/ # Django project config
│ ├── settings.py
│ └── urls.py
├── manage.py
└── db.sqlite3


---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/zainchodry/Task-Company-Django.git
cd Task-Company-Django


#Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


