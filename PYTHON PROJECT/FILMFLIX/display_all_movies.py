from connect_movies import *

def read_movies():
    db_cursor.execute("SELECT * FROM movies")

    all_movies = db_cursor.fetchall()

    for a_movie in all_movies:
        print(a_movie)

if __name__ == "__main__":
    read_movies()

