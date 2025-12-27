import sqlite3 as sq
from parser_quotes import get_quotes

with sq.connect("quotes.db") as data:
    cur = data.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS quotes (
    quote TEXT,
    author TEXT,
    born TEXT
    )""")

    cur.executemany(""" INSERT INTO quotes (quote, author, born) VALUES (?,?,?)""", get_quotes())