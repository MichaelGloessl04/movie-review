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
