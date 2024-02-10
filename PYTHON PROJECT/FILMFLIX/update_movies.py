from connect_movies import *

def update_movie():

    id_field = input("Enter the MovieID of the record you wish to update: ")

    field_name = input("Field you wish to update (Title, Released, Ratind, Duration, Genre): ")

    field_value = input(f"Enter new value for {field_name}: ")

    field_value = "'" + field_value + "'"

    db_cursor.execute(f"UPDATE movies SET {field_name} = {field_value} WHERE MovieID = {id_field}")

    db_con.commit()

    print(f"Value {field_name} of a record number {id_field} updated.")

if __name__ == "__main__":
    update_movie()