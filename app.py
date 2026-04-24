from flask import Flask, render_template, request, redirect, url_for, session, flash, g, jsonify
import sqlite3
import os
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

app = Flask(__name__)
app.secret_key = 'super_secret_ems_key' # In production, use os.urandom(24)
DATABASE = 'database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Ensure we have the required directories
os.makedirs(os.path.join(app.root_path, 'static', 'uploads'), exist_ok=True)
os.makedirs(os.path.join(app.root_path, 'static', 'css'), exist_ok=True)
os.makedirs(os.path.join(app.root_path, 'static', 'js'), exist_ok=True)
os.makedirs(os.path.join(app.root_path, 'static', 'img'), exist_ok=True)
os.makedirs(os.path.join(app.root_path, 'templates'), exist_ok=True)


# -------------- Context Processors --------------
@app.context_processor
def inject_user():
    user = None
    if 'user_id' in session:
        cur = get_db().cursor()
        cur.execute("SELECT * FROM users WHERE id = ?", (session['user_id'],))
        user = cur.fetchone()
    return dict(current_user=user)

# -------------- Main Routes --------------
@app.route('/')
def index():
    db = get_db()
    cur = db.cursor()
    # Fetch top 3 upcoming events
    cur.execute('''
        SELECT * FROM events 
        ORDER BY date ASC 
        LIMIT 3
    ''')
    featured_events = cur.fetchall()
    return render_template('index.html', featured_events=featured_events)

# -------------- Auth Routes --------------
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
            
        hashed_password = generate_password_hash(password)
        try:
            cur.execute("INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)", 
                        (name, email, hashed_password))
            db.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except BaseException as e:
            flash(f'An error occurred: {str(e)}', 'error')
            return redirect(url_for('register'))
            
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        cur = get_db().cursor()
        cur.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cur.fetchone()
        
        if user and check_password_hash(user['password_hash'], password):
            session['user_id'] = user['id']
            session['role'] = user['role']
            flash('Logged in successfully!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password.', 'error')
            
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please log in to access this page.', 'error')
        return redirect(url_for('login'))
    
    db = get_db()
    cur = db.cursor()
    # Fetch registered events for dashboard
    cur.execute('''
        SELECT e.*, r.ticket_id 
        FROM events e
        JOIN registrations r ON e.id = r.event_id
        WHERE r.user_id = ?
    ''', (session['user_id'],))
    registered_events = cur.fetchall()
    
    return render_template('dashboard.html', registered_events=registered_events)

# -------------- Event Routes --------------
@app.route('/events')
def events():
    db = get_db()
    cur = db.cursor()
    category = request.args.get('category')
    search = request.args.get('search')
    
    query = "SELECT * FROM events WHERE 1=1"
    params = []
    
    if category:
        query += " AND category = ?"
        params.append(category)
    if search:
        query += " AND title LIKE ?"
        params.append(f"%{search}%")
        
    query += " ORDER BY date ASC"
    
    cur.execute(query, params)
    event_list = cur.fetchall()
    return render_template('events.html', events=event_list)

@app.route('/event/<int:id>')
def event_details(id):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM events WHERE id = ?", (id,))
    event = cur.fetchone()
    
    if not event:
        flash("Event not found", "error")
        return redirect(url_for('events'))
        
    return render_template('event_details.html', event=event)

@app.route('/event/create', methods=['GET', 'POST'])
def create_event():
    if 'user_id' not in session or session.get('role') not in ['admin', 'organizer']:
        flash("You do not have permission to create events.", "error")
        return redirect(url_for('index'))
        
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        date = request.form.get('date')
        time = request.form.get('time')
        venue = request.form.get('venue')
        category = request.form.get('category')
        total_seats = int(request.form.get('total_seats', 0))
        image_url = request.form.get('image_url') or "https://via.placeholder.com/800x400"
        
        db = get_db()
        cur = db.cursor()
        cur.execute('''
            INSERT INTO events (title, description, date, time, venue, category, image_url, total_seats, available_seats, organizer_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (title, description, date, time, venue, category, image_url, total_seats, total_seats, session['user_id']))
        event_id = cur.lastrowid
        db.commit()
        
        flash("Event created successfully!", "success")
        return redirect(url_for('event_details', id=event_id))
        
    return render_template('create_event.html')

@app.route('/event/<int:id>/register', methods=['POST'])
def register_event(id):
    if 'user_id' not in session:
        flash("Please log in to register for events.", "error")
        return redirect(url_for('login'))
        
    db = get_db()
    cur = db.cursor()
    
    # Check if already registered
    cur.execute("SELECT * FROM registrations WHERE user_id = ? AND event_id = ?", (session['user_id'], id))
    if cur.fetchone():
        flash("You are already registered for this event.", "error")
        return redirect(url_for('event_details', id=id))
        
    cur.execute("SELECT available_seats FROM events WHERE id = ?", (id,))
    event = cur.fetchone()
    
    if not event or event['available_seats'] <= 0:
        flash("Sorry, this event is sold out.", "error")
        return redirect(url_for('event_details', id=id))
        
    # Generate unique ticket ID
    ticket_id = f"TKT-{uuid.uuid4().hex[:8].upper()}"
    
    try:
        cur.execute("BEGIN TRANSACTION")
        
        # Deduct seat
        cur.execute("UPDATE events SET available_seats = available_seats - 1 WHERE id = ?", (id,))
        
        # Add registration
        cur.execute("INSERT INTO registrations (user_id, event_id, ticket_id) VALUES (?, ?, ?)", 
                   (session['user_id'], id, ticket_id))
                   
        # Add points to user (Gamification)
        cur.execute("UPDATE users SET points = points + 10 WHERE id = ?", (session['user_id'],))
        
        # Gamification: Update Badge
        cur.execute("SELECT points FROM users WHERE id = ?", (session['user_id'],))
        user_points = cur.fetchone()['points']
        new_badge = 'Beginner'
        if user_points >= 50:
            new_badge = 'Pro Attendee'
        elif user_points >= 30:
            new_badge = 'Enthusiast'
        elif user_points >= 10:
            new_badge = 'Active'
            
        cur.execute("UPDATE users SET badge = ? WHERE id = ?", (new_badge, session['user_id']))
        
        db.commit()
        flash(f"Successfully registered! Your ticket ID is {ticket_id}", "success")
    except Exception as e:
        db.rollback()
        flash(f"Registration failed: {str(e)}", "error")
        
    return redirect(url_for('event_details', id=id))

@app.route('/event/<int:id>/comments', methods=['GET', 'POST'])
def event_comments(id):
    db = get_db()
    cur = db.cursor()
    
    if request.method == 'POST':
        if 'user_id' not in session:
            return jsonify({'error': 'Unauthorized'}), 401
            
        data = request.get_json()
        comment_text = data.get('text')
        
        if not comment_text:
            return jsonify({'error': 'Comment cannot be empty'}), 400
            
        cur.execute("INSERT INTO comments (user_id, event_id, comment_text) VALUES (?, ?, ?)",
                   (session['user_id'], id, comment_text))
        db.commit()
        
        # Fetch the created comment
        cur.execute('''
            SELECT c.*, u.name 
            FROM comments c JOIN users u ON c.user_id = u.id 
            WHERE c.id = ?
        ''', (cur.lastrowid,))
        new_comment = cur.fetchone()
        
        return jsonify({
            'success': True,
            'comment': {
                'id': new_comment['id'],
                'user': new_comment['name'],
                'text': new_comment['comment_text'],
                'timestamp': new_comment['timestamp']
            }
        })
        
    # GET request: fetch comments
    cur.execute('''
        SELECT c.*, u.name 
        FROM comments c JOIN users u ON c.user_id = u.id 
        WHERE c.event_id = ? 
        ORDER BY c.timestamp DESC
    ''', (id,))
    comments = cur.fetchall()
    
    return jsonify({
        'comments': [
            {'id': c['id'], 'user': c['name'], 'text': c['comment_text'], 'timestamp': c['timestamp']} 
            for c in comments
        ]
    })

@app.route('/analytics')
def analytics():
    if 'user_id' not in session or session.get('role') not in ['admin', 'organizer']:
        flash('Access denied.', 'error')
        return redirect(url_for('index'))
        
    db = get_db()
    cur = db.cursor()
    
    # Total Users
    cur.execute("SELECT COUNT(*) as cnt FROM users")
    total_users = cur.fetchone()['cnt']
    
    # Popular Events (top 5 by registrations)
    cur.execute('''
        SELECT e.title, (e.total_seats - e.available_seats) as registrations 
        FROM events e 
        ORDER BY registrations DESC LIMIT 5
    ''')
    popular_events = cur.fetchall()
    
    return render_template('analytics.html', 
                          total_users=total_users, 
                          popular_events=popular_events)

if __name__ == '__main__':
    app.run(debug=True)

