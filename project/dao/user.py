from .base import BaseDAO
from .model.user import User


class UsersDAO(BaseDAO[User]):
    __model__ = User
