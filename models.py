from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relationship

engine = create_engine("sqlite:///developers.db")

db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

CHOICES = ["PHP", "Python", "C#", "Javascript", "C++"]


class Skills(Base):
    __tablename__ = "skills"
    id = Column(Integer, primary_key=True, autoincrement=True)
    skill = Column(String(50), index=True)

    def __repr__(self):
        return self.skill


class DeleveLopers(Base):
    __tablename__ = "developers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80), nullable=False, index=True)
    skills_id = Column(Integer, ForeignKey("skills.id"))
    skill = relationship("Skills")


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
