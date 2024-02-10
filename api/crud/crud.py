from sqlalchemy.orm import Session
from api.crud.models import Base, Movie, Genre, Director, Review, User


class Crud:
    def __init__(self, engine):
        """
        Initializes the Crud class with the given database engine.
        """
        self._engine = engine
        Base.metadata.create_all(self._engine)

    def get_movies(self, id: int = None) -> list[Movie]:
        """
        Retrieves a list of movies from the database.

        Args:
            id (int, optional): The ID of the movie to retrieve. Defaults to
            None.

        Returns:
            list[Movie]: A list of Movie objects.
        """
        return self._get(Movie, id)

    def add_movie(self,
                  name: str,
                  poster_file: str,
                  release_date: str,
                  genre_id: int,
                  director_id: int) -> Movie:
        """
        Adds a new movie to the database.

        Args:
            name (str): The name of the movie.
            poster_file (str): The file path of the movie poster.
            release_date (str): The release date of the movie.
            genre_id (int): The ID of the genre associated with the movie.
            director_id (int): The ID of the director associated with the
            movie.

        Returns:
            Movie: The newly added Movie object.
        """
        return self._add(Movie(
                        name=name,
                        poster_file=poster_file,
                        release_date=release_date,
                        genre_id=genre_id,
                        director_id=director_id))

    def get_genres(self, id: int = None) -> list[Genre]:
        """
        Retrieves a list of genres from the database.

        Args:
            id (int, optional): The ID of the genre to retrieve.
            Defaults to None.

        Returns:
            list[Genre]: A list of Genre objects.
        """
        return self._get(Genre, id)

    def add_genre(self, name: str) -> Genre:
        """
        Adds a new genre to the database.

        Args:
            name (str): The name of the genre.

        Returns:
            Genre: The newly added Genre object.
        """
        return self._add(Genre(name=name))

    def get_directors(self, id: int = None) -> list[Director]:
        """
        Retrieves a list of directors from the database.

        Args:
            id (int, optional): The ID of the director to retrieve.
            Defaults to None.

        Returns:
            list[Director]: A list of Director objects.
        """
        return self._get(Director, id)

    def add_director(self,
                     first_name: str,
                     last_name: str,
                     birth_date: int,
                     death_date: int,
                     country_of_origin: str) -> Director:
        """
        Adds a new director to the database.

        Args:
            first_name (str): The first name of the director.
            last_name (str): The last name of the director.
            birth_date (int): The birth date of the director.
            death_date (int): The death date of the director.
            country_of_origin (str): The country of origin of the director.

        Returns:
            Director: The newly added Director object.
        """
        return self._add(Director(
                        first_name=first_name,
                        last_name=last_name,
                        birth_date=birth_date,
                        death_date=death_date,
                        country_of_origin=country_of_origin))

    def _add(self, obj: Base):
        with Session(self._engine) as session:
            session.add(obj)
            session.commit()
            return session.query(obj.__class__) \
                .order_by(obj.__class__.id.desc()).first()

    def _get(self, obj: Base, id: int = None):
        with Session(self._engine) as session:
            if id:
                return session.query(obj).filter(obj.id == id).all()
            else:
                return session.query(obj).all()
