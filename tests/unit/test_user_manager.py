import secrets
import pytest
from app.db.abc_db import DatabaseABC

from app.db.in_memory_db import InMemoryDatabase
from app.user_manager import UserManager

class TestUserManager:

    @pytest.fixture(scope="function", name="db")
    def db_(self,) -> DatabaseABC:
        return InMemoryDatabase()
    
    @pytest.fixture(scope="function", name="manager")
    def manager_(self,db: DatabaseABC) -> UserManager:
        return UserManager(db=db)
    
    def test_create_user(self, db: DatabaseABC, manager: UserManager) -> None:
        # arrange
        user_id = secrets.token_hex(2)

        # act
        manager.create_user(user_id)

        # assert
        assert db.get_user(user_id) is not None
    
    def test_create_user_with_username_in_id(self, db: DatabaseABC, manager: UserManager) -> None:
        # arrange
        user_id = secrets.token_hex(2)
        username = secrets.token_hex(1)
        separator = "|"

        # act
        manager.create_user_with_username_in_id(user_id=user_id, username=username, separator=separator)

        # assert
        saved_user = db.list_users()[0]
        assert username in saved_user.user_id
        assert user_id in saved_user.user_id
        assert separator in saved_user.user_id