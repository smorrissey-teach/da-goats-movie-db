import sqlite3
conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

cursor.execute('''select * from movies''')

result = cursor.fetchall()

for row in result:
    genres = row[5]
    movie_id = row[0]
    genres_list = genres.split('|')
    for genre in genres_list:
        print(genre)
        cursor.execute('''INSERT OR IGNORE INTO genre (genre_name) VALUES (?)''', (genre,))
        cursor.execute(f'''SELECT genre_id FROM genre WHERE genre_name= "{genre}" ''', (genre,))
        result = cursor.fetchone()
        print(result)


#cursor.execute('''DROP TABLE genre''')
conn.commit()
cursor.execute('''create table if not exists genre(genre_id INTEGER,genre_name TEXT unique);''')

cursor.execute('''CREATE TABLE IF NOT EXISTS movie_genre (movie_id INTERGER NOT NULL, genre_id INTERGER NOT NULL, PRIMARY KEY(movie_id, genre_id), FOREIGN KEY (movie_id) REFERENCES movie(id) ON DELETE CASCADE ON UPDATE CASCADE, FOREIGN KEY (genre_id) REFERENCES genre(id) ON DELETE CASCADE ON UPDATE CASCADE);''')
