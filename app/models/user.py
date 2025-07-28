from app.database import get_db
import bcrypt

class User:
    @staticmethod
    def create(email, password):
        db = get_db()
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        try:
            cursor = db.execute('INSERT INTO users (email, password) values (?, ?)', (email, hashed))
            db.commit()
            return cursor.lastrowid
        except db.IntegrityError:
            return None

    @staticmethod
    def get_by_email(email):
        db = get_db()
        user = db.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
        return dict(user) if user else None

    @staticmethod
    def get_by_id(user_id):
        db = get_db()
        user = db.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
        return dict(user) if user else None