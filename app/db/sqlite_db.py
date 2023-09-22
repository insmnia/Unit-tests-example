import sqlite3
from typing import List, Optional
from app.db.abc_db import DatabaseABC, User


class SQLiteDatabase(DatabaseABC):

    def __init__(self, db_url: str) -> None:
        self._connection = sqlite3.connect(db_url)
        self._cursor = self._connection.cursor()
        self._create_table_user()

    def _create_table_user(self) -> None:  # done just to not use migration tool
        self._cursor.execute("CREATE TABLE IF NOT EXISTS user(user_id TEXT NOT NULL)")

    def create_user(self, user: User) -> None:
        self._cursor.execute("INSERT INTO user(user_id) VALUES (?)", (user.user_id,))
        self._connection.commit()
    
    def get_user(self, user_id: str) -> Optional[User]:
        self._cursor.execute("SELECT * FROM user WHERE user_id=?", (user_id,))
        user_id = self._cursor.fetchone()
        if not user_id:
            return None
        return User(user_id=user_id)
    
    def list_users(self) -> List[User]:
        self._cursor.execute("SELECT * FROM user")
        results = self._cursor.fetchall()
        return [User(user_id=result[0]) for result in results]