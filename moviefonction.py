import sqlite3
conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

def get_movie_from_id(movie_id):
    cursor.execute(f'''SELECT name FROM movie WHERE id = {movie_id}; ''')
    results = cursor.fetchone()
    return results

def get_avg_rating(movie_id):