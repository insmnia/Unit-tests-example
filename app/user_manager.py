from app.db.abc_db import DatabaseABC, User


class UserManager:

    def __init__(self, db: DatabaseABC) -> None:
        self._db = db

    def create_user(self, user_id: str) -> None:
        user = User(user_id=user_id)
        self._db.create_user(user)
    
    def create_user_with_username_in_id(self, user_id: str, username: str, separator: str = "|") -> None:
        user_id_with_username = f"{user_id}{separator}{username}"
        user = User(user_id=user_id_with_username)
        self._db.create_user(user)