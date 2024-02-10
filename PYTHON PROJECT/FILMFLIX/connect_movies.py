import sqlite3 as sql

db_con = sql.connect("PYTHON\\PYTHON PROJECT\\FILMFLIX\\movies.db")

db_cursor = db_con.cursor()