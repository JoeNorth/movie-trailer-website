from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

base = declarative_base()


# Defining the structure of our Movie object
class Movie(base):
    __tablename__ = 'movies' # Tell SQL Alchemy what the table name will be
    # Here we define columns for the table movies
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    title = Column(String(250), nullable=False)
    poster_url = Column(String(250), nullable=False)
    trailer_url = Column(String(250), nullable=False)


# Retrieves all movies from the database
def get_movies():
    session = dbsession()

    movies = session.query(Movie).all()

    return movies


# Adds a new movie to the database
def create_movie(title, poster_url, trailer_url):
    session = dbsession()
    session.add(Movie(title=title, poster_url=poster_url, trailer_url=trailer_url))
    session.commit()


# Opens a new session to the database. Extracted to its own function to keep things DRY.
def dbsession():
    engine = create_engine('sqlite:///movies.sqlite')
    base.metadata.bind = engine

    session = sessionmaker()
    session.bind = engine
    session = session()

    return session

# Create an engine that stores data in the local directory's
# movies.sqlite file.
engine = create_engine('sqlite:///movies.sqlite')

# Create all tables in the engine.
base.metadata.create_all(engine)
