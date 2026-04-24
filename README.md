# 🎪 Event Management System

> **A modern, full-featured web application for seamless event management, registration, and community engagement**

![GitHub License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-black?style=flat-square&logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=flat-square&logo=sqlite)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

---

## 📋 Table of Contents

- [✨ Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [📸 Preview](#-preview)
- [⚡ Quick Start](#-quick-start)
- [📂 Project Structure](#-project-structure)
- [🚀 Usage](#-usage)
- [💻 Code Highlights](#-code-highlights)
- [🔮 Future Enhancements](#-future-enhancements)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👤 Author](#-author)

---

## ✨ Features

### 🔐 **Authentication & Security**
- Secure user registration and login system
- Password hashing with Werkzeug security
- Session management for user persistence
- Role-based access control (Admin, Organizer, User)

### 🎟️ **Event Management**
- Create, browse, and register for events
- Event categorization and filtering
- Search functionality for quick discovery
- Detailed event information display
- Real-time seat availability tracking

### 🏆 **Gamification System**
- Point-based reward system
- Dynamic badge achievement system
  - 🟤 Beginner (0+ points)
  - 🟡 Active (10+ points)
  - 🟠 Enthusiast (30+ points)
  - 🔴 Pro Attendee (50+ points)
- Motivates user engagement and participation

### 💬 **Community Features**
- Event-specific comment threads
- Real-time comment submission
- User engagement tracking
- Community feedback system

### 📊 **Analytics & Insights**
- Event popularity metrics
- User engagement statistics
- Top-performing events dashboard
- Administrator analytics panel
- Registration tracking

### 📱 **User Experience**
- Responsive and intuitive interface
- User dashboard for registered events
- Ticket generation system
- Unique ticket ID tracking (TKT-XXXXXXXX format)
- Flash notifications for user feedback

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| **Backend** | Flask (Python Web Framework) |
| **Language** | Python 3.8+ |
| **Database** | SQLite3 |
| **Frontend** | HTML5, CSS3, JavaScript (ES6) |
| **Security** | Werkzeug Security (Password Hashing) |
| **Session Management** | Flask Session |
| **Data Format** | JSON, SQL |

---

## 📸 Preview

### 🎨 Interface Showcase

![Login Interface](Screenshot%202026-04-25%20002535.png)
*User-friendly login interface with secure authentication*

![Event Dashboard](Screenshot%202026-04-25%20002602.png)
*Comprehensive event browsing and registration dashboard*

![Event Details](Screenshot%202026-04-25%20002630.png)
*Detailed event information with registration and comments*

---

## ⚡ Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/RITESH2127/WT-PBL-THEORY-.git
   cd WT-PBL-THEORY-
   ```

2. **Create Virtual Environment** (Recommended)
   ```bash
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install flask
   ```

4. **Initialize Database**
   ```bash
   python init_db.py
   ```

5. **Run the Application**
   ```bash
   python app.py
   ```

6. **Access the Application**
   ```
   Open your browser and navigate to: http://127.0.0.1:5000
   ```

---

## 📂 Project Structure

```
WT-PBL-THEORY-/
│
├── app.py                      # Main Flask application & routes
├── init_db.py                  # Database initialization script
├── database.db                 # SQLite database file
├── style.css                   # Global stylesheets
├── main.js                     # Frontend JavaScript logic
│
├── templates/                  # HTML templates
│   ├── base.html               # Base template (layout)
│   ├── index.html              # Homepage
│   ├── login.html              # Login page
│   ├── register.html           # Registration page
│   ├── dashboard.html          # User dashboard
│   ├── events.html             # Events listing page
│   ├── event_details.html      # Event detail view
│   ├── create_event.html       # Event creation form
│   └── analytics.html          # Analytics dashboard
│
└── static/                     # Static assets
    ├── uploads/                # User uploads directory
    ├── css/                    # Additional stylesheets
    ├── js/                     # Additional JavaScript
    └── img/                    # Image assets
```

---

## 🚀 Usage

### For End Users

1. **Register/Login**
   - Create an account or log in with existing credentials
   - Secure password protection with hashing

2. **Browse Events**
   - View all available events
   - Filter by category
   - Search for specific events

3. **Register for Events**
   - Click "Register" on any event
   - Receive unique ticket ID
   - Earn points for engagement
   - Track earned badges

4. **View Dashboard**
   - Access your registered events
   - View earned badges
   - Track your points

5. **Engage with Community**
   - Leave comments on events
   - Read feedback from other attendees
   - Build community connections

### For Event Organizers/Admins

1. **Create Events**
   - Navigate to event creation page
   - Set event details (title, description, date, venue, category)
   - Define seat capacity
   - Add event image

2. **Monitor Analytics**
   - View total user count
   - Track popular events
   - Monitor registration trends

3. **Manage System**
   - Access admin panel
   - View system statistics

---

## 💻 Code Highlights

### User Registration with Security
```python
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        
        db = get_db()
        cur = db.cursor()
        
        # Check if user exists
        cur.execute("SELECT * FROM users WHERE email = ?", (email,))
        if cur.fetchone():
            flash('Email already registered. Please log in.', 'error')
            return redirect(url_for('register'))
            
        # Hash password securely
        hashed_password = generate_password_hash(password)
        try:
            cur.execute("INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)", 
                        (name, email, hashed_password))
            db.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'error')
```

### Event Registration with Gamification
```python
@app.route('/event/<int:id>/register', methods=['POST'])
def register_event(id):
    # Begin transaction for data consistency
    cur.execute("BEGIN TRANSACTION")
    
    # Deduct seat
    cur.execute("UPDATE events SET available_seats = available_seats - 1 WHERE id = ?", (id,))
    
    # Add registration with unique ticket
    ticket_id = f"TKT-{{uuid.uuid4().hex[:8].upper()}}"
    cur.execute("INSERT INTO registrations (user_id, event_id, ticket_id) VALUES (?, ?, ?)", 
               (session['user_id'], id, ticket_id))
    
    # Award points
    cur.execute("UPDATE users SET points = points + 10 WHERE id = ?", (session['user_id'],))
    
    # Update badge based on points
    cur.execute("SELECT points FROM users WHERE id = ?", (session['user_id'],))
    user_points = cur.fetchone()['points']
    
    badge = 'Beginner'
    if user_points >= 50:
        badge = 'Pro Attendee'
    elif user_points >= 30:
        badge = 'Enthusiast'
    elif user_points >= 10:
        badge = 'Active'
    
    cur.execute("UPDATE users SET badge = ? WHERE id = ?", (badge, session['user_id']))
    db.commit()
    
    flash(f"Successfully registered! Your ticket ID is {ticket_id}", "success")
```

### Real-time Comment System
```python
@app.route('/event/<int:id>/comments', methods=['GET', 'POST'])
def event_comments(id):
    db = get_db()
    cur = db.cursor()
    
    if request.method == 'POST':
        data = request.get_json()
        comment_text = data.get('text')
        
        cur.execute("INSERT INTO comments (user_id, event_id, comment_text) VALUES (?, ?, ?)",
                   (session['user_id'], id, comment_text))
        db.commit()
        
        return jsonify({'success': True, 'message': 'Comment added!'})
```

---

## 🔮 Future Enhancements

- 📧 Email notifications for event updates
- 📍 Location-based event discovery
- 🎫 Advanced ticket management system
- 💳 Payment gateway integration
- 📱 Mobile application
- 🔔 Push notifications
- 📅 Calendar integration
- 🌍 Multi-language support
- 👥 Social sharing features
- 🎁 Referral rewards system
- 📹 Video streaming for virtual events
- 🤖 AI-powered event recommendations

---

## 🤝 Contributing

Contributions are warmly welcomed! To contribute:

1. **Fork the Repository**
   ```bash
   git clone https://github.com/RITESH2127/WT-PBL-THEORY-.git
   ```

2. **Create Feature Branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```

3. **Commit Changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```

4. **Push to Branch**
   ```bash
   git push origin feature/AmazingFeature
   ```

5. **Open Pull Request**
   - Describe your changes clearly
   - Reference any related issues

---

## 📄 License

This project is licensed under the **MIT License** - see the LICENSE file for details.

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 👤 Author

**Ritesh Kumar**
- 🐙 GitHub: [@RITESH2127](https://github.com/RITESH2127)
- 💼 Project: Event Management System
- 📅 Last Updated: April 2026

---

<div align="center">

### ⭐ If you found this project helpful, please give it a star!

Made with ❤️ by [RITESH2127](https://github.com/RITESH2127)

**[↑ Back to Top](#event-management-system)**

</div>