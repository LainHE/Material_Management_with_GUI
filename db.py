import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS list (id INTEGER PRIMARY KEY, name text, author text, "
                         "publisher text, dateOfPublish text, type text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM list")
        rows = self.cur.fetchall()
        return rows

    def insert(self, name, author, publisher, dateOfPublish, type):
        self.cur.execute("INSERT INTO list VALUES (NULL, ?, ?, ?, ?, ?)",
                         (name, author, publisher, dateOfPublish, type))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM list WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, name, author, publisher, dateOfPublish, type):
        self.cur.execute("UPDATE list SET name = ?, author = ?, publisher = ?, dateOfPublish = ?, type = ? WHERE "
                         "id = ?", (name, author, publisher, dateOfPublish, type, id))
        self.conn.commit()

    def selectName(self, name):
        self.cur.execute("SELECT * FROM list WHERE name LIKE '%"+name+"%'")
        rows = self.cur.fetchall()
        return rows

    def selectAuthor(self, author):
        self.cur.execute("SELECT * FROM list WHERE author LIKE '%"+author+"%'")
        rows = self.cur.fetchall()
        return rows

    def selectPublisher(self, publisher):
        self.cur.execute("SELECT * FROM list WHERE publisher LIKE '%"+publisher+"%'")
        rows = self.cur.fetchall()
        return rows

    def selectDateOfPublish(self, dateOfPublish):
        self.cur.execute("SELECT * FROM list WHERE dateOfPublish LIKE '%"+dateOfPublish+"%'")
        rows = self.cur.fetchall()
        return rows

    def __del__(self):
        self.conn.close()


db = Database('list.db')