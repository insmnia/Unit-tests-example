import abc
from typing import List
from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    user_id: str


class DatabaseABC(abc.ABC):

    @abc.abstractmethod
    def get_user(self, user_id: str) -> Optional[User]:
        """Get user from database by it's id

        Args:
            user_id (str): user id

        Raises:
            NotImplementedError: ABC class, see implementations

        Returns:
            User: a user model from a database
        """
        raise NotImplementedError

    @abc.abstractmethod
    def create_user(self, user: User) -> None:
        """Save user to database

        Args:
            user (User): user model

        Raises:
            NotImplementedError: ABC class, see implementations
        """
        raise NotImplementedError
    
    @abc.abstractmethod
    def list_users(self,) -> List[User]:
        """Returns all users from database

        Raises:
            NotImplementedError: ABC class, see implementations

        Returns:
            List[User]: a list of all users in database
        """
        raise NotImplementedError