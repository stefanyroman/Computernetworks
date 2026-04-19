import sqlite3

# SQLite database file
DB_NAME = "checkins.db"

# Creates and returns a database connection
def get_connection():
    conn = sqlite3.connect(DB_NAME)
    # Allows accessing columns by name instead of index
    conn.row_factory = sqlite3.Row
    return conn

# Initializes and creates checkins table if it doesn't exist
def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # Table structure stores each user check-in and associated results
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS checkins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            test_id TEXT NOT NULL,
            stressed INTEGER NOT NULL,
            happy INTEGER NOT NULL,
            motivation INTEGER NOT NULL,
            mood TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()

# Saves a completed check-in to the database
def save_checkin(username, test_id, stressed, happy, motivation, mood):
    conn = get_connection()
    cursor = conn.cursor()

    # Insert a new row containing user input and computed result
    cursor.execute("""
        INSERT INTO checkins (username, test_id, stressed, happy, motivation, mood)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (username, test_id, stressed, happy, motivation, mood))

    conn.commit()
    conn.close()

# Retrieves all check-ins for a specific user, ordered by most recent first
def get_checkins_by_user(username):
    conn = get_connection()
    cursor = conn.cursor()

    rows = cursor.execute("""
        SELECT *
        FROM checkins
        WHERE username = ?
        ORDER BY created_at DESC, id DESC
    """, (username,)).fetchall()

    conn.close()
    return rows
