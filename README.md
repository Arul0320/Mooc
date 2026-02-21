# 📚 Mini MOOC Course Catalog (Django)

A minimal MOOC-style course catalog built with **Django** that allows users to browse courses, enroll, view lessons, and track progress.
This project was created as part of an assignment to demonstrate Django fundamentals and clean architecture.

---

## 🚀 Features

* 🔐 User authentication (Signup, Login, Logout)
* 📖 Course catalog with title and description
* 🧾 Course detail page with lessons list
* ✅ Course enrollment
* 🎓 “My Courses” page for enrolled courses
* ▶️ Lesson detail view
* 📊 Lesson visit/progress tracking per user
* 🛠 Admin panel for managing courses and lessons
* 🐳 Docker support for quick setup

---

## 🏗 Tech Stack

* **Backend:** Django 4+
* **Database:** SQLite (default)
* **Auth:** Django built-in authentication
* **Containerization:** Docker & Docker Compose

---

## 📂 Project Structure

```
mooc/
 ├ courses/          
 ├ mooc/
 ├ templates/        
 ├ Dockerfile
 ├ docker-compose.yml
 ├ requirements.txt
 └ README.md
```

---

## ⚙️ Local Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/Arul0320/Mooc.git
cd mooc
```

### 2️⃣ Create virtual environment

```
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run migrations

```
python manage.py migrate
```

### 5️⃣ Create superuser

```
python manage.py createsuperuser
```

### 6️⃣ Start server

```
python manage.py runserver
```

App will be available at 👉 http://127.0.0.1:8000

---

## 🐳 Run with Docker

### Build & start

```
docker compose up --build
```

Visit 👉 http://localhost:8000

---

## 🔑 Admin Access

Go to
👉 `/admin`

Use the superuser credentials created earlier.

From admin you can:

* Create courses
* Add lessons
* View enrollments
* Track progress

---

## 🧪 How to Test Workflow

1. Register a new user
2. Browse courses
3. Open a course and click **Enroll**
4. Open lessons
5. Visit **My Courses**
6. Check progress records in admin

---

## 📌 Assumptions & Notes

* UI is intentionally minimal (assignment requirement)
* SQLite used for simplicity
* Progress is tracked when a lesson is opened
* One enrollment per user per course

---

## 📈 Possible Improvements

* Course search & filtering
* Progress percentage per course
* REST API with DRF
* Video lessons support
* Production deployment (Postgres + Nginx)

---

## 👨‍💻 Author

**Arulmurugan S**
Python Developer

---
