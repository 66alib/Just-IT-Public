from connect_movies import *

db_cursor.execute(
    """
CREATE TABLE "movies" (
    "MovieID"       INTEGER NOT NULL UNIQUE,
    "Title"         TEXT,
    "Released"      INTEGER NOT NULL,
    "Rating"        TEXT,
    "Duration"      INTEGER NOT NULL,
    "Genre"         TEXT,
    PRIMARY KEY("MovieID" AUTOINCREMENT)
)"""
)

