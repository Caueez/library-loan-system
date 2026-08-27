
from .v1 import migrate_v1

MIGRATIONS = {
    1: migrate_v1,
}

CURRENT_VERSION = 1

SCHEMA_VERSION_TABLE = """
    CREATE TABLE IF NOT EXISTS schema_version (
        version INTEGER NOT NULL
    );
"""

GET_SCHEMA_VERSION = """
    SELECT version
    FROM schema_version
    LIMIT 1;
"""