import re
from __init__ import CONN, CURSOR
from datetime import datetime
import ipdb

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
            raise Exception('Date must be formatted as MM-DD-YY')
        
    @property
    def outcome(self):
        return self._outcome
    
    @outcome.setter
    def outcome(self, outcome):
        try:
            outcome_int = int(outcome)
            if outcome_int == 1 or outcome_int == 0:
                self._outcome = outcome_int
            else:
                raise Exception('Outcome must be 1 or 0')
        except:
            raise Exception('Outcome must be 1 or 0') 
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS matches(
                id INTEGER PRIMARY KEY,
                date TEXT,
                outcome INTEGER,
                opponent_id INTEGER
            );
        """
        CURSOR.execute(sql)
        CONN.commit()

    # DEVELOPMENT PURPOSES ONLY**
    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE matches"
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create_match(cls, date, outcome, opponent_id):
        match = cls(date=date, outcome=outcome, opponent_id=opponent_id)
        match.save()

    def save(self):
        sql = """
            INSERT INTO matches(date, outcome, opponent_id) VALUES(?, ?, ?)
        """
        CURSOR.execute(sql, (self.date, self.outcome, self.opponent_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        Match.all[self.id] = self

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM matches"
        matches_rows = CURSOR.execute(sql).fetchall()
        for row in matches_rows:
            match = cls.instance_from_db(row)
            cls.all[match.id] = match

    @classmethod
    def instance_from_db(cls, row):
        id = row[0]
        date = row[1]
        outcome = row[2]
        opponent_id = row[3]
        match = cls(id=id, date=date, outcome=outcome, opponent_id=opponent_id)
        return match

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM matches WHERE id = ?"
        match = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(match)

    def delete_match(self):
        sql = "DELETE FROM matches WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del Match.all[self.id]
        self.id = None

    @classmethod
    def search_by_date(cls, start, end):
        date_format = "%m-%d-%y"
        start_date = datetime.strptime(start, date_format)
        end_date = datetime.strptime(end, date_format)
        return [match for match_id, match in Match.all.items() if start_date <= datetime.strptime(match.date, date_format) <= end_date]