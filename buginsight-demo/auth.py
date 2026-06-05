def get_user(username):
    query = f"SELECT * FROM users WHERE username='{username}'"
    return query
