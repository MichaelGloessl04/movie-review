from typing import Tuple
from sqlalchemy.orm import Session
from api.crud.crud import Crud


def test_movies(crud_session_in_memory: Tuple[Crud, Session, list[dict]]):
    crud_in_memory, session, test_movies = crud_session_in_memory

    movies = crud_in_memory.get_movies()
    assert len(movies) == 3
    for movie, expected in zip(movies, test_movies):
        assert movie.name == expected["name"]
        assert movie.poster_file == expected["poster_file"]
        assert movie.release_date == expected["release_date"]
        assert movie.genre_id == expected["genre_id"]
        assert movie.director_id == expected["director_id"]

    movie = crud_in_memory.get_movies(1)
    for key, value in test_movies[0].items():
        assert getattr(movie[0], key) == value
