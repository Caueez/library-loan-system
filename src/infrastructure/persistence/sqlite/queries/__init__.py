from .book import SQLITE_BOOK_QUERIES
from .student import SQLITE_STUDENT_QUERIES
from .loan import SQLITE_LOAN_QUERIES


def get_queries(database: str) -> dict[str, dict[str, str]]:
    match database:
        case "sqlite":
            return {
                "book": SQLITE_BOOK_QUERIES,
                "student": SQLITE_STUDENT_QUERIES,
                "loan": SQLITE_LOAN_QUERIES
            }
        case _:
            raise ValueError("Banco de dados não suportado")
