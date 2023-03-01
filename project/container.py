from project.dao.genre import BaseDAO
from project.dao.user import UsersDAO
from project.dao.director import DirectorsDAO
from project.dao.movie import MoviesDAO

from project.services.genres_service import GenresService
from project.setup.db import db

# DAO
genre_dao = BaseDAO(db.session)

# Services
genre_service = GenresService(dao=genre_dao)
