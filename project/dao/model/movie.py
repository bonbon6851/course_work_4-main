from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship

from project.setup.db import models


class Movie(models.Base):
    __tablename__ = 'movie'

    title = Column(String(100))
    description = Column(String(250))
    trailer = Column(String(200))
    year = Column(Integer)
    rating = Column(Float(100))
    genre_id = Column(Integer, ForeignKey("genre.id"))
    genre = relationship("Genre")
    director_id = Column(Integer, ForeignKey("director.id"))
    director = relationship("Director")
