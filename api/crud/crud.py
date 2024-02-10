from sqlalchemy.orm import Session
from api.crud.models import Base, Movie, Genre, Director, Review, User


class Crud():
    def __init__(self, engine):
        self._engine = engine
        Base.metadata.create_all(self._engine)

    def get_movies(self, id: int = None) -> list[Movie]:
        with Session(self._engine) as session:
            if id:
                return session.query(Movie).filter(Movie.id == id).all()
            else:
                return session.query(Movie).all()

    def add_movie(self,
                  name: str,
                  poster_file,
                  release_date,
                  genre_id,
                  director_id) -> Movie:
        movie = Movie(name=name,
                      poster_file=poster_file,
                      release_date=release_date,
                      genre_id=genre_id,
                      director_id=director_id)
        with Session(self._engine) as session:
            session.add(movie)
            session.commit()
            session.refresh(movie)
            return movie
