import sqlite3
import os
from werkzeug.security import generate_password_hash

DATABASE = 'database.db'

def init_db():
    if os.path.exists(DATABASE):
        os.remove(DATABASE)

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Users Table
    cursor.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            role TEXT DEFAULT 'user',
            points INTEGER DEFAULT 0,
            badge TEXT DEFAULT 'Beginner'
        )
    ''')

    # Events Table
    cursor.execute('''
        CREATE TABLE events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            venue TEXT NOT NULL,
            category TEXT NOT NULL,
            image_url TEXT,
            total_seats INTEGER NOT NULL,
            available_seats INTEGER NOT NULL,
            organizer_id INTEGER,
            FOREIGN KEY (organizer_id) REFERENCES users (id)
        )
    ''')

    # Registrations Table
    cursor.execute('''
        CREATE TABLE registrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            event_id INTEGER NOT NULL,
            ticket_id TEXT UNIQUE NOT NULL,
            registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id),
            FOREIGN KEY (event_id) REFERENCES events (id)
        )
    ''')

    # Comments Table
    cursor.execute('''
        CREATE TABLE comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            event_id INTEGER NOT NULL,
            comment_text TEXT NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id),
            FOREIGN KEY (event_id) REFERENCES events (id)
        )
    ''')

    # Gallery Table
    cursor.execute('''
        CREATE TABLE gallery (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            image_url TEXT NOT NULL,
            FOREIGN KEY (event_id) REFERENCES events (id),
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')

    # Create an admin user for initial testing
    admin_password = generate_password_hash("admin123")
    cursor.execute('''
        INSERT INTO users (name, email, password_hash, role) 
        VALUES (?, ?, ?, ?)
    ''', ('Admin User', 'admin@ems.com', admin_password, 'admin'))

    # Create a regular user for testing
    user_password = generate_password_hash("user123")
    cursor.execute('''
        INSERT INTO users (name, email, password_hash, role) 
        VALUES (?, ?, ?, ?)
    ''', ('Regular User', 'user@ems.com', user_password, 'user'))

    conn.commit()
    conn.close()
    print("Database initialized successfully.")

if __name__ == '__main__':
    init_db()
