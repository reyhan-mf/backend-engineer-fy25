from app.database import get_db

class Item:
    @staticmethod
    def create(name, description, user_id, status='pending'):
        db = get_db()
        try:
            cursor = db.execute('INSERT INTO items (name, description, status, user_id) values (?, ?, ?, ?)', (name, description, status, user_id))
            db.commit()
            return cursor.lastrowid
        except db.IntegrityError:
            return None
