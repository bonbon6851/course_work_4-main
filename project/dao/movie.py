from project.dao.base import BaseDAO
from project.dao.model.movie import Movie


class MoviesDAO(BaseDAO[Movie]):
    __model__ = Movie
