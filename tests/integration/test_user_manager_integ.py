from pathlib import Path

import pytest
from app.db.abc_db import DatabaseABC
from app.db.sqlite_db import SQLiteDatabase
from tests.unit.test_user_manager import TestUserManager as _TestUserManager

class TestUserManagerInteg(_TestUserManager):

    @pytest.fixture(scope="function", name="db")
    def db_(self, tmp_path: Path) -> DatabaseABC:
        return SQLiteDatabase(db_url=tmp_path / "test.db")