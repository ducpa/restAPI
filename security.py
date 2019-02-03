from werkzeug.security import safe_str_cmp
import sqlite3

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def find_by_username(self, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = User(row[0], row[1], row[2])
        else:
            user = None

        connection.close()
        return user

    def find_by_id(self, id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (id,))
        row = result.fetchone()
        if row:
            user = User(row[0], row[1], row[2])
        else:
            user = None

        connection.close()
        return user


'''
users = [
    User(1, 'bob', 'asdf'),
    User(2, 'ducpa', 'abc')
]

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}
'''
def authenticate(username, password):
    user = User.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)