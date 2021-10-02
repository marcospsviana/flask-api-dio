from sqlalchemy import Integer, String, Column
from sqlalchemy import create_engine
from sqlalchemy.dialects.sqlite.json import JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("sqlite:///developers.db")

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


class Developers(Base):
    __tablename__ = "developers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80), nullable=False, index=True)
    skills_ids = Column(JSON(none_as_null=False))

    def delete(self):
        db_session.remove(self)
        db_session.commit()

    def save(self):
        db_session.add(self)
        db_session.commit()


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
