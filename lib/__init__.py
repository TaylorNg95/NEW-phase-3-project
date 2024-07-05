import sqlite3

CONN = sqlite3.connect('match_log.db')
CURSOR = CONN.cursor()
