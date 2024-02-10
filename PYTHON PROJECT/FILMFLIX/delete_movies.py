from connect_movies import *

def delete_movie():

    id_field = input("Enter the MovieID you wish to delete: ")

    for check_database in (id_field,):

        db_cursor.execute("SELECT MovieID FROM movies WHERE MovieID = ?", (check_database,))
        check_result = db_cursor.fetchone()

        if check_result is None:
            return print(f"Record number {id_field} not found. Please try again.")    
        else:
            db_cursor.execute(f"DELETE FROM movies WHERE MovieID = {id_field}")
            db_con.commit()
            print(f"Movie {id_field} deleted from the 'Movies' table!")
        
    
if __name__ == "__main__":
    delete_movie()

# when deleting entries SQLite is not re-using IDs and therefore gaps can occur. If you wish to re-use current ID
# use update all fields option. 