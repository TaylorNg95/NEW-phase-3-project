import re
from __init__ import CONN, CURSOR

class Match:
    all = {}
    
    def __init__(self, date, outcome, opponent_id, id=None):
        self.date = date
        self.outcome = outcome
        self.opponent_id = opponent_id
        self.id = id

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        # regex will automatically check for string with length > 0
        if re.fullmatch(r'\d{2}-\d{2}-\d{2}', date):
            self._date = date
        else:
            raise Exception
        
    @property
    def outcome(self):
        return self._outcome
    
    @outcome.setter
    def outcome(self, outcome):
        if outcome == '1' or outcome == '0':
            self._outcome = outcome
        else:
            raise Exception
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS matches(
                id INTEGER PRIMARY KEY,
                date TEXT,
                outcome INTEGER,
                opponent_id INTEGER,
                FOREIGN KEY(opponent_id) REFERENCES opponents(id)
            );
        """
        CURSOR.execute(sql)
        CONN.commit()