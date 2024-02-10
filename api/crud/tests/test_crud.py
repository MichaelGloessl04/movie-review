import pytest
from api.crud.crud import Crud
from api.crud.tests.populate import MOVIES, GENRES, DIRECTORS, USER, REVIEW

BADVALUES = {
    "str": "string",
    "int": 1,
    "float": 1.0,
    "none": None,
    "list": ["list"],
    "dict": {"dict": "dict"},
    "tuple": ("tuple",)
}


def test_get_movies(crud_in_memory: Crud):
    movies = crud_in_memory.get_movies()
    assert len(movies) == len(MOVIES)
    for movie, expected in zip(movies, MOVIES):
        for key, value in expected.items():
            assert getattr(movie, key) == value

    movie = crud_in_memory.get_movies(1)
    for key, value in MOVIES[0].items():
        assert getattr(movie[0], key) == value


def test_add_movie(crud_in_memory: Crud):
    new_movie = {
        "name": "The Matrix",
        "poster_file": "the_matrix.jpg",
        "release_date": 19990331,
        "genre_id": 1,
        "director_id": 1
    }

    movie = crud_in_memory.add_movie(**new_movie)

    for key, value in new_movie.items():
        assert getattr(movie, key) == value

    movies = crud_in_memory.get_movies()
    assert len(movies) == len(MOVIES) + 1
    for key, value in new_movie.items():
        assert getattr(movies[-1], key) == value


def test_add_invalid_movie(crud_in_memory: Crud):
    movie = {
        "name": "str",
        "poster_file": "str",
        "release_date": "int",
        "genre_id": "int",
        "director_id": "int"
    }

    for key, value in movie.items():
        good_movie = {
            "name": "The Matrix",
            "poster_file": "the_matrix.jpg",
            "release_date": 19990331,
            "genre_id": 1,
            "director_id": 1
        }
        for bad_key, bad_value in BADVALUES.items():
            if value != bad_key:
                good_movie[key] = bad_value
                with pytest.raises(TypeError):
                    crud_in_memory.add_movie(**good_movie)
            else:
                continue


def test_get_genres(crud_in_memory: Crud):
    genres = crud_in_memory.get_genres()
    assert len(genres) == len(GENRES)
    for genre, expected in zip(genres, GENRES):
        for key, value in expected.items():
            assert getattr(genre, key) == value

    genre = crud_in_memory.get_genres(1)
    for key, value in GENRES[0].items():
        assert getattr(genre[0], key) == value


def test_add_genre(crud_in_memory: Crud):
    new_genre = {"name": "Sci-Fi"}

    genre = crud_in_memory.add_genre(**new_genre)

    for key, value in new_genre.items():
        assert getattr(genre, key) == value

    genres = crud_in_memory.get_genres()
    assert len(genres) == len(GENRES) + 1
    for key, value in new_genre.items():
        assert getattr(genres[-1], key) == value


def test_add_invalid_genre(crud_in_memory: Crud):
    genre = {"name": "str"}

    for key, value in genre.items():
        good_genre = {"name": "Sci-Fi"}
        for bad_key, bad_value in BADVALUES.items():
            if value != bad_key:
                good_genre[key] = bad_value
                with pytest.raises(TypeError):
                    crud_in_memory.add_genre(**good_genre)
            else:
                continue


def test_get_directors(crud_in_memory: Crud):
    directors = crud_in_memory.get_directors()
    assert len(directors) == len(DIRECTORS)
    for director, expected in zip(directors, DIRECTORS):
        for key, value in expected.items():
            assert getattr(director, key) == value

    director = crud_in_memory.get_directors(1)
    for key, value in DIRECTORS[0].items():
        assert getattr(director[0], key) == value


def test_add_director(crud_in_memory: Crud):
    new_director = {
        "first_name": "Lana",
        "last_name": "Wachowski",
        "birth_date": 19650621,
        "death_date": None,
        "country_of_origin": "USA"
    }

    director = crud_in_memory.add_director(**new_director)

    for key, value in new_director.items():
        assert getattr(director, key) == value

    directors = crud_in_memory.get_directors()
    assert len(directors) == len(DIRECTORS) + 1
    for key, value in new_director.items():
        assert getattr(directors[-1], key) == value


def test_add_invalid_director(crud_in_memory: Crud):
    director = {
        "first_name": "str",
        "last_name": "str",
        "birth_date": "int",
        "death_date": "int",
        "country_of_origin": "str"
    }

    for key, value in director.items():
        good_director = {
            "first_name": "Lana",
            "last_name": "Wachowski",
            "birth_date": 19650621,
            "death_date": None,
            "country_of_origin": "USA"
        }
        for bad_key, bad_value in BADVALUES.items():
            if value != bad_key:
                good_director[key] = bad_value
                with pytest.raises(TypeError):
                    crud_in_memory.add_director(**good_director)
            else:
                continue


def test_get_reviews(crud_in_memory: Crud):
    reviews = crud_in_memory.get_reviews()
    assert len(reviews) == len(REVIEW)
    for review, expected in zip(reviews, REVIEW):
        for key, value in expected.items():
            assert getattr(review, key) == value

    review = crud_in_memory.get_reviews(1)
    for key, value in REVIEW[0].items():
        assert getattr(review[0], key) == value


def test_add_review(crud_in_memory: Crud):
    new_review = {
        "rating": 4,
        "review": "Good movie",
        "movie_id": 1,
        "user_id": 1
    }

    review = crud_in_memory.add_review(**new_review)

    for key, value in new_review.items():
        assert getattr(review, key) == value

    reviews = crud_in_memory.get_reviews()
    assert len(reviews) == len(REVIEW) + 1
    for key, value in new_review.items():
        assert getattr(reviews[-1], key) == value


def test_add_invalid_review(crud_in_memory: Crud):
    review = {
        "rating": "int",
        "review": "str",
        "movie_id": "int",
        "user_id": "int"
    }

    for key, value in review.items():
        good_review = {
            "rating": 4,
            "review": "Good movie",
            "movie_id": 1,
            "user_id": 1
        }
        for bad_key, bad_value in BADVALUES.items():
            if value != bad_key:
                good_review[key] = bad_value
                with pytest.raises(TypeError):
                    crud_in_memory.add_review(**good_review)
            else:
                continue


def test_get_users(crud_in_memory: Crud):
    users = crud_in_memory.get_users()
    assert len(users) == len(USER)
    for user, expected in zip(users, USER):
        for key, value in expected.items():
            assert getattr(user, key) == value

    user = crud_in_memory.get_users(1)
    for key, value in USER[0].items():
        assert getattr(user[0], key) == value


def test_add_user(crud_in_memory: Crud):
    new_user = {
        "username": "user2",
        "email": "email2",
        "password": "password2"
    }

    user = crud_in_memory.add_user(**new_user)

    for key, value in new_user.items():
        assert getattr(user, key) == value

    users = crud_in_memory.get_users()
    assert len(users) == len(USER) + 1
    for key, value in new_user.items():
        assert getattr(users[-1], key) == value


def test_add_invalid_user(crud_in_memory: Crud):
    user = {
        "username": "str",
        "email": "str",
        "password": "str"
    }

    for key, value in user.items():
        good_user = {
            "username": "user2",
            "email": "email2",
            "password": "password2"
        }
        for bad_key, bad_value in BADVALUES.items():
            if value != bad_key:
                good_user[key] = bad_value
                with pytest.raises(TypeError):
                    crud_in_memory.add_user(**good_user)
            else:
                continue
