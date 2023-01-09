from flask_login import LoginManager
import psycopg2


login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    # Return the user object for the user ID
    return User.get(user_id)

class User:
    def __init__(self,id , username, password):
        self.id = id
        self.username = username
        self.password = password

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    @classmethod
    def get(cls, user_id):
        conn = psycopg2.connect(
   database="expense-tracker", user='postgres', password='raz', host='127.0.0.1', port= '5432')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE id=%s"%(user_id))
        actual_user = c.fetchone()
        # Retrieve the user object from the database
        user = User(actual_user[0], actual_user[1], actual_user[2])
        return user

class UserModel:
    def __init__(self):
        self.conn = psycopg2.connect(
   database="expense-tracker", user='postgres', password='raz', host='127.0.0.1', port= '5432')

    def create_user(self, user):
        c = self.conn.cursor()
        c.execute("INSERT INTO users (username, password) VALUES ('%s', '%s');" % (user.username, user.password))
        self.conn.commit()
        return c.lastrowid

    def get_user(self, user_id):
        c = self.conn.cursor()
        c.execute("SELECT * FROM users WHERE id=%s"%(user_id))
        return c.fetchone()

    def get_user_by_username(self, username):
        c = self.conn.cursor()
        c.execute("SELECT * FROM users WHERE username='%s'"%(username))
        return c.fetchone()


    def delete_user_by_username(self, username):
        c = self.conn.cursor()
        c.execute("DELETE FROM users WHERE username='%s'"%(username))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()