



from typing import Any

from infrastructure.persistence.interface import DBInterface
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

    def __init__(self, settings: dict[str, Any]):
        self.setup()
        self.settings = settings

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
        self._get_queries()
        self._instance_repo_adapters()

    def _instance_database(self) -> None:
        choice = self.settings["database"]["type"]

        match choice:
            case "sqlite":
                self._db = SqliteDB(self.settings[choice]["uri"])
            case _:
                raise Exception("Banco de dados não suportado")

    def _get_queries(self) -> None:
        choice = self.settings["database"]["type"]

        self._queries = self.settings[choice]["queries"]

    def _instance_repo_adapters(self) -> None:
        self._book_repository = BookRepositoryAdapter(self._db, self._queries)
        self._book_loan_repository = BookLoanRepositoryAdapter(self._db, self._queries)
        self._student_repository = StudentRepositoryAdapter(self._db, self._queries)