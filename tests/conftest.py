import pytest
import sys

import os
from passlib.hash import pbkdf2_sha256

from api.app_rest import create_app
from sqlalchemy import Integer, String, Column
from sqlalchemy import create_engine
from sqlalchemy.dialects.sqlite.json import JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("sqlite://")

conn = engine.connect()


conn.execute(
    """
CREATE TABLE users
(
  id INTEGER NOT NULL,
  username  TEXT   NOT NULL,
  password  TEXT   NOT NULL,
  PRIMARY KEY (id)
);
"""
)

conn.execute(
    """
CREATE TABLE developers
(
  id INTEGER NOT NULL,
  name  TEXT   NOT NULL,
  skills_ids  JSON ,
  PRIMARY KEY (id)
);
"""
)

# class UserTest(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     username = Column(String(25), nullable=False, index=True, unique=True)
#     password = Column(String(500), nullable=False)

#     def __repr__(self):
#         return self.username

#     def delete(self):
#         db_session.remove(self)
#         db_session.commit()

#     def save(self):
#         db_session.add(self)
#         db_session.commit()


@pytest.fixture(scope="session")
def app():
<<<<<<< HEAD
    app = create_app()
    return app


@pytest.fixture(scope="session")
def db():
    password_hash = pbkdf2_sha256.hash('devnull')
    conn.execute(
        f"INSERT INTO users(id, username, password) VALUES (1, 'devtest', {password_hash} )"
    )

    user = conn.execute("SELECT  * FROM users WHERE id = 1")
    yield user
    # # db_user = db_session.query(UserTest).filter(UserTest.username == 'devtest').first()
    # # user.delete(db_user)
    conn.execute("DELETE FROM users WHERE id = 1")
    # conn.close()
=======
    
    return create_app()


@pytest.fixture
def db():
    user = Users(id=1, username="devpro", password="devnull")
    return user

>>>>>>> 94f1ea30bd90da17b14242862bf049a0b5ab9f9e
