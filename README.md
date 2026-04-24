<div align="center">
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Calendar.png" alt="EMS Logo" width="120" />
  
  <h1 align="center">EMS Portal 🚀</h1>
  <h3 align="center">A Smart, Gamified Event Management System</h3>

  <p align="center">
    Streamline departmental events, workshops, and meetups with our state-of-the-art platform designed for unparalleled user engagement.
  </p>

  <p align="center">
    <img src="https://img.shields.io/badge/Python-3.8+-blue.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/Flask-Framework-black.svg?style=for-the-badge&logo=flask&logoColor=white" alt="Flask" />
    <img src="https://img.shields.io/badge/SQLite-Database-003B57.svg?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite" />
    <img src="https://img.shields.io/badge/UI-Glassmorphism-FF69B4.svg?style=for-the-badge" alt="UI" />
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge" alt="License" />
  </p>
</div>

---

## 📋 Table of Contents
- [📖 Overview](#-overview)
- [✨ Key Features](#-key-features)
- [📸 Interface Preview](#-interface-preview)
- [🏗️ System Architecture](#️-system-architecture)
- [📂 Directory Structure](#-directory-structure)
- [🚀 Installation & Setup](#-installation--setup)
- [🔮 Future Scope](#-future-scope)
- [🧑‍💻 About the Developer](#-about-the-developer)

---

## 📖 Overview

The **EMS Portal** (Event Management System) is a comprehensive web application engineered to modernize how academic and extracurricular events are organized. Moving away from messy spreadsheets and manual ticketing, this platform provides a centralized, automated, and visually stunning hub.

What sets this portal apart is its **premium Glassmorphism UI** and built-in **Gamification Engine**, which incentivizes student participation by awarding points and dynamic badges (Bronze, Silver, Gold) for registering and attending events.

---

## ✨ Key Features

| Feature | Description |
| :--- | :--- |
| **🔐 Secure Auth** | End-to-end encrypted password hashing with secure session management. Role-based access control. |
| **📅 Event CRUD** | Organizers can effortlessly create, edit, view, and delete events. |
| **🎟️ RSVP Tracking** | Real-time capacity monitoring preventing overbooking and duplicate registrations. |
| **🎮 Gamification** | Users earn points for engagement, unlocking tier-based badges displayed on their dashboards. |
| **📊 Admin Analytics** | A dedicated space for organizers to track platform metrics and registration trends using Chart.js. |
| **💎 Premium UI** | A breathtaking, modern interface featuring frosted glass aesthetics and CSS micro-animations. |

---

## 📸 Interface Preview

*(Note: Ensure images are placed in your `static/img/` folder for these to render correctly)*

<table align="center">
  <tr>
    <td align="center"><b>🏠 Discover Awesome Events</b></td>
  </tr>
  <tr>
    <td><img src="static/img/home_preview.png" alt="Home Page" width="800" style="border-radius:8px"/></td>
  </tr>
</table>

<table align="center">
  <tr>
    <td align="center"><b>🔐 Secure Login</b></td>
    <td align="center"><b>📝 Instant Registration</b></td>
  </tr>
  <tr>
    <td><img src="static/img/login_preview.png" alt="Login Page" width="400" style="border-radius:8px"/></td>
    <td><img src="static/img/register_preview.png" alt="Register Page" width="400" style="border-radius:8px"/></td>
  </tr>
</table>

---

## 🏗️ System Architecture

- **Backend:** Python, Flask (Jinja2, Werkzeug)
- **Database:** SQLite (Relational DB)
- **Frontend:** HTML5, CSS3 (Vanilla + Glassmorphism design system)
- **Interactivity:** Vanilla JavaScript (DOM Manipulation, Chart.js)
- **Icons:** Phosphor Icons

---

## 📂 Directory Structure

<details>
<summary><b>Click to expand</b></summary>

```text
WT_PBL/
├── static/
│   ├── css/
│   │   └── style.css       # Core styling & Glassmorphism classes
│   ├── js/
│   │   └── main.js         # Frontend interactivity
│   └── img/                # Assorted graphics & screenshots
├── templates/
│   ├── base.html           # Main layout block
│   ├── index.html          # Landing page
│   ├── login.html          # Auth pages
│   ├── dashboard.html      # User dashboards
│   └── analytics.html      # Admin data visualization
├── app.py                  # Core Flask Application setup & routes
├── init_db.py              # Database initialization & seeding
├── database.db             # SQLite database file
└── requirements.txt        # Python dependencies
```
</details>

---

## 🚀 Installation & Setup

Want to run the EMS Portal locally? Follow these simple steps:

### Prerequisites
- [Python 3.8+](https://www.python.org/downloads/) installed on your machine.
- [Git](https://git-scm.com/) installed.

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/event-management-portal.git
cd event-management-portal
```

### 2️⃣ Create a Virtual Environment & Install Dependencies
```bash
# Create Virtual Environment
python -m venv .venv

# Activate it (Windows)
.\.venv\Scripts\activate

# Activate it (macOS/Linux)
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

### 3️⃣ Initialize the Database & Run
```bash
# Initialize DB
python init_db.py

# Run the app!
python app.py
```
> 🎉 **Success!** The application will launch on your local server. Open your browser and navigate to: `http://127.0.0.1:5000`

---

## 🔮 Future Scope

- [ ] **Automated Emails:** Integrate SMTP to send RSVP confirmations and reminders.
- [ ] **Payment Gateway:** Add Stripe integration for premium/paid event ticketing.
- [ ] **Social Sharing:** Allow users to share events directly to WhatsApp and LinkedIn.
- [ ] **Live Forums:** Implement WebSockets for real-time event-specific discussion forums.

---

