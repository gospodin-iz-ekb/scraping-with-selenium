import sqlite3 # импорт библиотеки

conn = sqlite3.connect('quotes.db') # подключение к базе данных
cursor = conn.cursor() # создание курсора

cursor.execute('SELECT * FROM quotes') # получение всех строк из таблицы
all_quotes = cursor.fetchall()

for quote in all_quotes:
    print('quote: ',  quote[0] + '\n', 'author: ',  quote[1] + '\n', 'born: ', quote[2]) # вывод строк