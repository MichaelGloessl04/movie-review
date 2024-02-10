from api.crud.models import Movie, Genre, Director

MOVIES = [
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

GENRES = [
        {"name": "Drama"},
        {"name": "Action"},
    ]

DIRECTORS = [
        {
            "first_name": "Frank",
            "last_name": "Darabont",
            "birth_date": 19590128,
            "death_date": None,
            "country_of_origin": "USA",
        },
        {
            "first_name": "Francis Ford",
            "last_name": "Coppola",
            "birth_date": 19390407,
            "death_date": None,
            "country_of_origin": "USA",
        },
        {
            "first_name": "Christopher",
            "last_name": "Nolan",
            "birth_date": 19770730,
            "death_date": None,
            "country_of_origin": "UK",
        },
    ]


def populate(session, obj):
    mock_values = []
    if obj == Movie:
        mock_values = MOVIES
    elif obj == Genre:
        mock_values = GENRES
    elif obj == Director:
        mock_values = DIRECTORS
    with session() as session:
        for movie in mock_values:
            session.add(obj(**movie))
            session.commit()
