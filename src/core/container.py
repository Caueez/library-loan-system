

from infrastructure.persistence.sqlite.queries import get_queries
from src.core.settings import Settings

from src.infrastructure.persistence.interface import DBInterface
from src.infrastructure.persistence.sqlite.implementation import SqliteDB

from src.application.ports import (
    BookRepository,
    BookLoanRepository,
    StudentRepository
    )

from src.infrastructure.persistence.adapters import (
    BookRepositoryAdapter, 
    BookLoanRepositoryAdapter,
    StudentRepositoryAdapter
    )


class Container:
    _db: DBInterface
    _book_repository: BookRepository
    _book_loan_repository: BookLoanRepository
    _student_repository: StudentRepository

    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.setup()

    @property
    def db(self) -> DBInterface:
        return self._db

    @property
    def book_repository(self) -> BookRepository:
        return self._book_repository

    @property
    def book_loan_repository(self) -> BookLoanRepository:
        return self._book_loan_repository

    @property
    def student_repository(self) -> StudentRepository:
        return self._student_repository


    def setup(self):
        self._instance_database()
        self._instance_repo_adapters()

    def _instance_database(self) -> None:
        database = self.settings.database

        match database.type:
            case "sqlite":
                self._db = SqliteDB(database.uri)
                self._queries = get_queries(database.type)

            case _:
                raise ValueError("Banco de dados não suportado")

    def _instance_repo_adapters(self) -> None:
        self._book_repository = BookRepositoryAdapter(self._db, self._queries["book"])
        self._book_loan_repository = BookLoanRepositoryAdapter(self._db, self._queries["loan"])
        self._student_repository = StudentRepositoryAdapter(self._db, self._queries["student"])