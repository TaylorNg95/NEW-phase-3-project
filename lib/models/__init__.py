import sqlite3

CONN = sqlite3.connect('../db/match_log.db')
CURSOR = CONN.cursor()
