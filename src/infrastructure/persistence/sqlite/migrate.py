

from infrastructure.persistence.sqlite.implementation import SqliteImplementation

from infrastructure.persistence.sqlite.migrations import (
    MIGRATIONS, 
    CURRENT_VERSION, 
    SCHEMA_VERSION_TABLE, 
    GET_SCHEMA_VERSION
    )


class Migration:
    def __init__(self, db: SqliteImplementation) -> None:
        self._db = db

    @staticmethod
    def create_schema_version_table(db: SqliteImplementation) -> None:
        db.execute(SCHEMA_VERSION_TABLE)
        db.execute("""
            INSERT INTO schema_version (version)
            SELECT 0
            WHERE NOT EXISTS (
                SELECT 1 FROM schema_version
            );
        """)

    @staticmethod
    def get_current_version(db: SqliteImplementation) -> int:
        return db.fetchone(GET_SCHEMA_VERSION)[0]

    def migrate(self) -> None:

        self.create_schema_version_table(self._db)

        with self._db.transaction():
            current_version = self.get_current_version(self._db)

            for version in range(
                current_version + 1,
                CURRENT_VERSION + 1
            ):
                MIGRATIONS[version](self._db)

                self._db.execute("""
                    UPDATE schema_version
                    SET version = ?;
                """, (version,))