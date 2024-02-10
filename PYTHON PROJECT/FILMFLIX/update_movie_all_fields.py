from connect_movies import *

def update_movie_all_fields():

    id_field = input("Enter the MovieID you wish to completely update: ")

    title_value = input("Change the Title to: ")
    released_value = input("Change the Released Date to: ")
    rating_value = input("Change the Rating to (G, PG, PG-13, R, NR): ")
    duration_value = input("Change the Duration Time to: ")
    genre_value = input("Change the Genre to: ")

    title_value = "'" + title_value + "'"
    rating_value = "'" + rating_value + "'"
    genre_value = "'" + genre_value + "'"

    db_cursor.execute(
        f"UPDATE movies SET Title = {title_value}, Released = {released_value}, Rating = {rating_value}, Duration = {duration_value}, Genre = {genre_value} WHERE MovieID = {id_field}")
    
    db_con.commit()

    print(f"Record ID number {id_field} changed in the Movies table.")

if __name__ == "__main__":
    update_movie_all_fields()

