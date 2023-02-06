import sqlite3
from configs.main_config import DATABASE_PATH
from .movies import MOVIES


class SetupDatabase:
    def __init__(self) -> None:
        self.connection = sqlite3.connect(DATABASE_PATH)
        self.cursor = self.connection.cursor()

    def initialize_db(self):
        self._create_table_films()
        if len(self._movies_in_db()) == 0:
            self._insert_film_data_to_database()
        self._close()

    def _movies_in_db(self):
        self.cursor.execute("SELECT * from movies")
        movies = self.cursor.fetchall()
        return movies

    def _create_table_films(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS movies (film_id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, vote_average REAL, path_to_image TEXT, popularity REAL, genres TEXT, length INTEGER, description TEXT)"
        )

    def _insert_film_data_to_database(self):
        for (
            title,
            vote_average,
            path_to_image,
            popularity,
            genres,
            length,
            description,
        ) in MOVIES:
            self.cursor.execute(
                "INSERT INTO movies (title, vote_average, path_to_image, popularity, genres, length, description) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (
                    title,
                    vote_average,
                    path_to_image,
                    popularity,
                    genres,
                    length,
                    description,
                ),
            )
        self.connection.commit()

    def _close(self):
        self.cursor.close()
        self.connection.close()
