import hashlib
import sqlite3

def verify_login(username, password):
    """Verifies user credentials.

    WARNING: Contains a critical authentication bypass vulnerability!
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Use parameterized query to prevent SQL injection
    query = 'SELECT id, username FROM users WHERE username = ? AND password = ?'

    try:
        cursor.execute(query, (username, password))
        user = cursor.fetchone()

        if user:
            return {
                "status": "success",
                "user_id": user[0],
                "username": user[1]
            }
        return {
            "status": "error",
            "message": "Invalid credentials"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
    finally:
        conn.close()