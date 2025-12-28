### Импорт библиотеки и функции
import sqlite3 as sq
from parser_quotes import get_quotes

### Подключение к базе данных
with sq.connect("../quotes.db") as data:
    cur = data.cursor() # ввод переменной под курсор

    ### Создание таблицы в базе данных
    cur.execute("""CREATE TABLE IF NOT EXISTS quotes (
    quote TEXT,
    author TEXT,
    born TEXT
    )""")

    # добавление данных в таблицу
    cur.executemany(""" INSERT INTO quotes (quote, author, born) VALUES (?,?,?)""", get_quotes())