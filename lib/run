#!/usr/bin/env python

from models.match import Match
from models.opponent import Opponent
from cli import Cli

Opponent.create_table()
Match.create_table()

# DEVELOPMENT PURPOSES ONLY**
""" Match.drop_table()
Opponent.drop_table() """

""" Opponent.create_opponent(name='Brittany Collens')
Opponent.create_opponent(name='Katarina Jokic')
Opponent.create_opponent(name='Lauren Proctor')
Opponent.create_opponent(name='Ashley Lahey')
Match.create_match(date='01-15-24', outcome=1, opponent_id=1)
Match.create_match(date='03-15-24', outcome=1, opponent_id=1)
Match.create_match(date='04-10-24', outcome=0, opponent_id=2)
Match.create_match(date='05-01-24', outcome=1, opponent_id=2)
Match.create_match(date='05-01-24', outcome=1, opponent_id=3) """

Opponent.get_all()
Match.get_all()

Cli().run()
