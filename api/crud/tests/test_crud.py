from typing import Tuple
from sqlalchemy.orm import Session

from api.crud.crud import Crud
from api.crud.tests.populate import MOVIES, GENRES, DIRECTORS


def test_get_movies(crud_session_in_memory: Tuple[Crud, Session]):
    crud_in_memory, session = crud_session_in_memory

    movies = crud_in_memory.get_movies()
    assert len(movies) == 3
    for movie, expected in zip(movies, MOVIES):
        for key, value in expected.items():
            assert getattr(movie, key) == value

    movie = crud_in_memory.get_movies(1)
    for key, value in MOVIES[0].items():
        assert getattr(movie[0], key) == value


def test_add_movie(crud_session_in_memory: Tuple[Crud, Session]):
    crud_in_memory, _ = crud_session_in_memory

    movie = crud_in_memory.add_movie(
        "The Matrix",
        "matrix.jpg",
        19990331,
        2,
        4,
    )
    assert movie.name == "The Matrix"
    assert movie.poster_file == "matrix.jpg"
    assert movie.release_date == 19990331
    assert movie.genre_id == 2
    assert movie.director_id == 4

    movies = crud_in_memory.get_movies()
    assert len(movies) == 4
    assert movies[-1].name == "The Matrix"
    assert movies[-1].poster_file == "matrix.jpg"
    assert movies[-1].release_date == 19990331
    assert movies[-1].genre_id == 2
    assert movies[-1].director_id == 4


def test_get_genres(crud_session_in_memory: Tuple[Crud, Session]):
    crud_in_memory, _ = crud_session_in_memory

    genres = crud_in_memory.get_genres()
    assert len(genres) == 2
    for genre, expected in zip(genres, GENRES):
        for key, value in expected.items():
            assert getattr(genre, key) == value

    genre = crud_in_memory.get_genres(1)
    for key, value in GENRES[0].items():
        assert getattr(genre[0], key) == value


def test_add_genre(crud_session_in_memory: Tuple[Crud, Session]):
    crud_in_memory, _ = crud_session_in_memory

    genre = crud_in_memory.add_genre("Science Fiction")
    assert genre.name == "Science Fiction"

    genres = crud_in_memory.get_genres()
    assert len(genres) == 3
    assert genres[-1].name == "Science Fiction"
