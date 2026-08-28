
from infrastructure.persistence.interface import DBInterface

BOOK_TABLE = """
    CREATE TABLE IF NOT EXISTS books (
        id_book TEXT PRIMARY KEY,

        name TEXT NOT NULL,
        author TEXT NOT NULL,
        isbn TEXT NOT NULL,

        created_at INTEGER NOT NULL,
        updated_at INTEGER NOT NULL
    );
"""

LOAN_TABLE = """
    CREATE TABLE IF NOT EXISTS loans (
        id_loan TEXT PRIMARY KEY,

        id_book TEXT NOT NULL,
        id_student TEXT NOT NULL,

        checked_in INTEGER NOT NULL,
        checked_out INTEGER,

        created_at INTEGER NOT NULL,
        updated_at INTEGER NOT NULL,
        
        FOREIGN KEY (id_book) REFERENCES books(id_book),
        FOREIGN KEY (id_student) REFERENCES students(id_student)
    );
"""

STUDENT_TABLE = """
    CREATE TABLE IF NOT EXISTS students (
        id_student TEXT PRIMARY KEY,

        name TEXT NOT NULL,
        cpf TEXT NOT NULL,
        matriculation TEXT NOT NULL,
        
        created_at INTEGER NOT NULL,
        updated_at INTEGER NOT NULL
    );
"""

TABLES = [STUDENT_TABLE, BOOK_TABLE, LOAN_TABLE]


def migrate_v1(db: DBInterface):
    for table in TABLES:
        db.execute(query=table)