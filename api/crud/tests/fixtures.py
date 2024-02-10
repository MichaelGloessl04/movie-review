import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.crud.crud import Crud
from api.crud.models import Movie, Genre, Director
from api.crud.tests.populate import populate


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
    populate(session, Movie)
    populate(session, Genre)
    populate(session, Director)
    yield (crud, session)
