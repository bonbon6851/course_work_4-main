from sqlalchemy import Column, String

from project.setup.db import models


class User(models.Base):
    __tablename__ = 'user'

    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)
    surname = Column(String(100))
    favorite_genre = Column(String(100))
