import sqlite3
from configs.main_config import DATABASE_PATH


class MovieDatabase:
    def __init__(self) -> None:
        self.connection = sqlite3.connect(DATABASE_PATH)
        self.cursor = self.connection.cursor()
        self.NUMBER_OF_MOVIES = 20

    def get_top_rated_movies(self, page):
        self.cursor.execute(
            f"SELECT title,vote_average,path_to_image,genres,length,description FROM movies ORDER BY vote_average DESC LIMIT {self.NUMBER_OF_MOVIES} OFFSET {(page - 1) * self.NUMBER_OF_MOVIES}"
        )
        return self.cursor.fetchall()

    def get_popular_movies(self, page):
        self.cursor.execute(
            f"SELECT title,vote_average,path_to_image,popularity,genres,length,description FROM movies ORDER BY popularity DESC LIMIT {self.NUMBER_OF_MOVIES} OFFSET {(page - 1) * self.NUMBER_OF_MOVIES}"
        )
        return self.cursor.fetchall()

    def get_movies_by_search(self, search):
        search = f"%{search}%"
        self.cursor.execute(
            "SELECT title,vote_average,path_to_image,genres,length,description FROM movies WHERE title LIKE ?",
            (search,),
        )
        return self.cursor.fetchall()

    def get_alphabetical_movies(self, page):
        self.cursor.execute(
            f"SELECT title,vote_average,path_to_image,genres,length,description FROM movies ORDER BY title ASC LIMIT {self.NUMBER_OF_MOVIES} OFFSET {(page - 1) * self.NUMBER_OF_MOVIES}"
        )
        return self.cursor.fetchall()

    def get_reverse_aphabetical_movies(self, page):
        self.cursor.execute(
            f"SELECT title,vote_average,path_to_image,genres,length,description FROM movies ORDER BY title DESC LIMIT {self.NUMBER_OF_MOVIES} OFFSET {(page - 1) * self.NUMBER_OF_MOVIES}"
        )
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()
