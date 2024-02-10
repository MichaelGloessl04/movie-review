import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.crud.crud import Crud


@pytest.fixture(scope="function")
def crud_in_memory():
    engine = create_engine("sqlite:///:memory:")
    crud = Crud(engine)
    yield crud


@pytest.fixture(scope="function")
def crud_session_in_memory():
    engine = create_engine("sqlite:///:memory:")
    crud = Crud(engine)
    session = sessionmaker(bind=engine)
    movies = [
        {
            "name": "The Shawshank Redemption",
            "poster_file": "shawshank_redemption.jpg",
            "release_date": 19940923,
            "genre_id": 1,
            "director_id": 1,
        },
        {
            "name": "The Godfather",
            "poster_file": "godfather.jpg",
            "release_date": 19720324,
            "genre_id": 1,
            "director_id": 2,
        },
        {
            "name": "The Dark Knight",
            "poster_file": "dark_knight.jpg",
            "release_date": 20080718,
            "genre_id": 2,
            "director_id": 3,
        },
    ]
    for movie in movies:
        crud.add_movie(
            movie["name"],
            movie["poster_file"],
            movie["release_date"],
            movie["genre_id"],
            movie["director_id"],
        )
    yield (crud, session, movies)
