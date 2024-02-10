from connect_movies import *

def report_movies_released():

    user_input_released = input("Please enter the release year to find: ")

    db_cursor.execute(f"SELECT * FROM movies WHERE Released = {user_input_released}")

    films_released = db_cursor.fetchall()

    for a_film_released in films_released:
        print(a_film_released)

if __name__ == "__main__":
    report_movies_released()