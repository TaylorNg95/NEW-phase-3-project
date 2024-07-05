from __init__ import CONN, CURSOR

class Opponent:
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
            raise Exception
        
    @classmethod
    def create_table(cls):
        pass