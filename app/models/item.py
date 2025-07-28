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
        
    @staticmethod
    def get_all(page=1, per_page=10, user_id=None):
        db = get_db()
        offset = (page - 1) * per_page

        if user_id:
            items = db.execute("SELECT * FROM items where user_id = ? LIMIT ? OFFSET ?", (user_id, per_page, offset)).fetchall()
            total = db.execute("SELECT COUNT(*) FROM items where user_id = ?", (user_id,)).fetchone()[0]
        else:
            items = db.execute("SELECT * FROM items LIMIT ? OFFSET ?", (per_page, offset)).fetchall()
            total = db.execute("SELECT COUNT(*) FROM items").fetchone()[0]
        
        return {
            'items': [dict(item) for item in items],
            'total': total,
            'page': page,
            'per_page': per_page
        }
     
    @staticmethod
    def get_by_id(item_id):
        db = get_db()
        item = db.execute("SELECT * FROM items WHERE id = ?", (item_id,)).fetchone()
        return dict(item) if item else None