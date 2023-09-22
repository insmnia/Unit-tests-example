from typing import List, Optional
from app.db.abc_db import DatabaseABC, User


class InMemoryDatabase(DatabaseABC):

    def __init__(self) -> None:
        self._storage: dict[str, User] = {}

    def create_user(self, user: User) -> None:
        self._storage[user.user_id] = user
    
    def get_user(self, user_id: str) -> Optional[User]:
        return self._storage.get(user_id)

    def list_users(self) -> List[User]:
        return list(self._storage.values())