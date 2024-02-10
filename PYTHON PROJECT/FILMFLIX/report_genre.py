from connect_movies import *

def report_movies_genre():

    user_input_genre = input("Please enter the Genre you'd like to search: ")

    db_cursor.execute(f"SELECT * FROM movies WHERE Genre LIKE '%{user_input_genre}%'")

    films_genre = db_cursor.fetchall()

    for a_film_genre in films_genre:
        print(a_film_genre)

if __name__ == "__main__":
    report_movies_genre()


