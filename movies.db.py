import sqlite3
import csv
conn = sqlite3.connect('movies.db')
cursor = conn.cursor()
cursor.execute('''create table if not exists Movies(
    movie_id INTEGER PRIMARY KEY,
    Name TEXT,
    MPA_Rating TEXT,
    Directer TEXT,
    Length TEXT,
    Genre TEXT,
    Release_date TEXT,
    Production_Company TEXT,
    Country TEXT);''')

cursor.execute('''create table if not exists Actors(
            actor_id INTEGER PRIMARY KEY,
            Name TEXT,
            Lastname TEXT);''')


cursor.execute('''create table if not exists Links(
movie_id PRIMARY KEY,
imbdID NUMERIC,
tmbdID NUMERIC,
FOREIGN KEY (movie_id) REFERENCES Movies(id));''')

cursor.execute('''create table if not exists Tags(
id INTEGER PRIMARY KEY,
userID inteGER,
movie_id INTEGER,
tag TEXT,
timestamp INTEGER,
FOREIGN KEY (movie_id) REFERENCES Movie(movie_id));''')
cursor.execute('''create table if not exists Users(
            user_id INTEGER PRIMARY KEY,
            Firstname TEXT,
            Lastname TEXT,
            Email TEXT,
            Age TEXT);''')

cursor.execute('''create table if not exists Movie_Reviews(
            review_id INTEGER PRIMARY KEY,
            movie_id INTEGER,
            Rates TEXT,
            Description TEXT);''')

cursor.execute('''create table if not exists Actors_Movie(
            movie_id INTEGER,
            actor_id INTEGER,
            PRIMARY KEY (movie_id, actor_id) ,
            FOREIGN KEY (movie_id) REFERENCES Movies(movie_id),
            FOREIGN KEY (actor_id) REFERENCES Actors(actor_id));''')

cursor.execute('''create table if not exists Users_Reviews(
            user_id INTEGER,
            review_id INTEGER,
            PRIMARY KEY (user_id, review_id),
            FOREIGN KEY (user_id) REFERENCES Users(user_id),
            FOREIGN KEY (review_id) REFERENCES Reviews(review_id));''')

conn.commit()

with open('data/movies.csv', newline='', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    next(reader)
    contents = ((int(row[0]), row[1], row[2]) for row in reader)
    cursor.executemany('INSERT INTO Movies (movie_id,Name,Genre) VALUES (?,?,?)', contents)

conn.commit()