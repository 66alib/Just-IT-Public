from connect_movies import *

def report_movies_rating():

    user_input_rating = input("Please enter the Rating based which you'd like to search: ")

    db_cursor.execute(f"SELECT * FROM movies WHERE Rating LIKE '%{user_input_rating}%'")

    films_rating = db_cursor.fetchall()

    for a_film_rating in films_rating:
        print(a_film_rating)

if __name__ == "__main__":
    report_movies_rating()