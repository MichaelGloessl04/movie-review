from platform import release
from sqlalchemy import ForeignKey, UniqueConstraint

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass


class Movie(Base):
    __tablename__ = 'movies'
    id: Mapped[int] = mapped_column('id', int, primary_key=True)
    name: Mapped[str]
    poster_file: Mapped[str]
    release_date: Mapped[int]
    genre_id: Mapped[int] = mapped_column('genre_id', int, ForeignKey('genres.id'))
    director_id: Mapped[int] = mapped_column('director_id', int, ForeignKey('directors.id'))


class Genre(Base):
    __tablename__ = 'genres'
    id: Mapped[int] = mapped_column('id', int, primary_key=True)
    name: Mapped[str]
    movies: Mapped[Movie] = relationship(
        back_populates='genre',
        cascade='all, delete, delete-orphan'
    )


class Director(Base):
    __tablename__ = 'directors'
    id: Mapped[int] = mapped_column('id', int, primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    birth_date: Mapped[int]
    death_date: Mapped[int]
    country_of_origin: Mapped[str]
    movies: Mapped[Movie] = relationship(
        back_populates='director',
        cascade='all, delete, delete-orphan'
    )


class Review(Base):
    __tablename__ = 'reviews'
    id: Mapped[int] = mapped_column('id', int, primary_key=True)
    rating: Mapped[int]
    review: Mapped[str]
    movie_id: Mapped[int] = mapped_column('movie_id', int, ForeignKey('movies.id'))
    user_id: Mapped[int] = mapped_column('user_id', int, ForeignKey('users.id'))


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column('id', int, primary_key=True)
    username: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]
    reviews: Mapped[Review] = relationship(
        back_populates='user',
        cascade='all, delete, delete-orphan'
    )
    UniqueConstraint('username', 'email', name='unique_user')
