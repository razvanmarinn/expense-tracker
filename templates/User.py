import psycopg2

class User:
    def __init__(self, username, password):
        self.id = None
        self.username = username
        self.password = password


class UserModel:
    def __init__(self):
        self.conn = psycopg2.connect(
   database="expense-tracker", user='postgres', password='raz', host='127.0.0.1', port= '5432')

    def create_user(self, user):
        c = self.conn.cursor()
        c.execute(
            f"INSERT INTO users (username, password) VALUES ('{user.username}', '{user.password}');"
        )
        self.conn.commit()
        return c.lastrowid

    def get_user(self, user_id):
        c = self.conn.cursor()
        c.execute(f"SELECT * FROM users WHERE id={user_id}")
        return c.fetchone()

    def get_user_by_username(self, username):
        c = self.conn.cursor()
        c.execute(f"SELECT * FROM users WHERE username='{username}'")
        return c.fetchone()


    def delete_user_by_username(self, username):
        c = self.conn.cursor()
        c.execute(f"DELETE FROM users WHERE username='{username}'")
        self.conn.commit()

    def close_connection(self):
        self.conn.close()