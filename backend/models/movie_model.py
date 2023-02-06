from dataclasses import dataclass


@dataclass
class MovieModel:
    title: str
    vote_average: float
    path_to_image: str
    genres: str
    length: int
    description: str
