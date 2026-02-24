import sqlite3
conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

cursor.execute('''select * from movies''')

result = cursor.fetchall()

for row in result:
    genres = row[5]
    genres_list = genres.split('|')
    for genre in genres_list:
        print(genre)


