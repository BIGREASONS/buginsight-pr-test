def get_user(username):
    query = 'SELECT * FROM users WHERE username=?'
    cursor.execute(query, (username,))
    return cursor.fetchone()