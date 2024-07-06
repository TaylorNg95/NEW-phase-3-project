from __init__ import CONN, CURSOR
from models.match import Match

class Opponent:
    all = {}

    def __init__(self, name, id=None):
        self.name = name
        self.id = id

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise Exception('Name must be a non-empty string')
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS opponents(
                id INTEGER PRIMARY KEY,
                name TEXT
            );
        """
        CURSOR.execute(sql)
        CONN.commit()

    # DEVELOPMENT PURPOSES ONLY**
    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE opponents"
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create_opponent(cls, name):
        opponent = cls(name=name)
        opponent.save()

    def save(self):
        sql = """
            INSERT INTO opponents(name) VALUES(?)
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        Opponent.all[self.id] = self

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM opponents"
        opponent_rows = CURSOR.execute(sql).fetchall()
        for row in opponent_rows:
            opponent = cls.instance_from_db(row)
            cls.all[opponent.id] = opponent

    @classmethod
    def instance_from_db(cls, row):
        id = row[0]
        name = row[1]
        opponent = cls(id=id, name=name)
        return opponent
    
    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM opponents WHERE id = ?"
        opponent = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(opponent)
    
    def delete_opponent(self):
        sql = "DELETE FROM opponents WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del Opponent.all[self.id]
        self.id = None

    def get_matches(self):
        return [match for match_id, match in Match.all.items() if match.opponent_id == self.id]