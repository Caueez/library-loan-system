from typing import Protocol

from application.ports.abstract_repo import AbstractRepository
from src.domain.entities.book import Book


class BookRepository(AbstractRepository[Book], Protocol):
    def get_by_name(self, name: str) -> list[Book]: ...

    def get_by_author(self, author: str) -> list[Book]: ...

    def get_by_isbn(self, isbn: str) -> list[Book]: ...