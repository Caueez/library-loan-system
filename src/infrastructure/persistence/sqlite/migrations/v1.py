
from infrastructure.persistence.sqlite.implementation import SqliteImplementation

BOOK_TABLE = """
    CREATE TABLE IF NOT EXISTS books (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        author TEXT NOT NULL,
        ISBN TEXT NOT NULL,
        created_at INTEGER NOT NULL,
        updated_at INTEGER
    );
"""

LOAN_TABLE = """
    CREATE TABLE IF NOT EXISTS loans (
        id TEXT PRIMARY KEY,
        FOREIGN KEY (id_book) REFERENCES books(id),
        FOREIGN KEY (id_students) REFERENCES students(id),
        checked_in INTEGER NOT NULL,
        checked_out INTEGER,
        created_at INTEGER NOT NULL,
        updated_at INTEGER
    );
"""

STUDENT_TABLE = """
    CREATE TABLE IF NOT EXISTS students (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        cpf TEXT NOT NULL,
        matriculation TEXT NOT NULL,
        created_at INTEGER NOT NULL,
        updated_at INTEGER
    );
"""

TABLES = [STUDENT_TABLE, BOOK_TABLE, LOAN_TABLE]


def migrate_v1(db: SqliteImplementation):
    for table in TABLES:
        db.execute(query=table)