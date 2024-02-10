from connect_movies import *

def add_movie():
    film_title = input("Enter movie title: ")
    film_year = input("Enter movie release date: ")
    film_rating = input("Enter movie rating (G, PG, PG-13, R, NR): ")
    film_duration = input("Enter movie length: ")
    film_genre = input("Enter movie genre of: ")

    db_cursor.execute("INSERT INTO movies (Title, Released, Rating, Duration, Genre) VALUES(?, ?, ?, ?, ?)", 
                  (film_title, film_year, film_rating, film_duration, film_genre))

    db_con.commit()

    print(f" '{film_title}' inserted in the Movies list.")

if __name__ == "__main__":
    add_movie()

