from typing import Protocol

from application.ports.abstract_repo import AbstractRepositoryInterface
from src.domain.entities.book import Book


class BookRepositoryInterface(AbstractRepositoryInterface[Book], Protocol):
    def get_by_name(self, name: str) -> list[Book]: ...

    def get_by_author(self, author: str) -> list[Book]: ...

    def get_by_isbn(self, isbn: str) -> list[Book]: ...