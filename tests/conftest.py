import pytest
import sys

import os


from api.app_rest import create_app
from sqlalchemy import Integer, String, Column
from sqlalchemy import create_engine
from sqlalchemy.dialects.sqlite.json import JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("sqlite:///memory:")

conn = engine.connect()

db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(25), nullable=False, index=True, unique=True)
    password = Column(String(500), nullable=False)

    def __repr__(self):
        return self.username

    def save(self):
        db_session.add(self)
        db_session.commit()


@pytest.fixture(scope="module")
def app():
    return create_app()


@pytest.fixture
def db():
    user = Users(id=1, username="devpro", password="devnull")
    return user

