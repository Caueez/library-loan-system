
from datetime import datetime
from typing import Any, Optional

from application.ports.book_repo import BookRepository

from domain.entities.book import Book

from domain.values.date import date_to_timestamp
from infrastructure.persistence.models.book import BookModel
from infrastructure.persistence.interface import DBInterface


class BookRepositoryAdapter(BookRepository):
    def __init__(self, db: DBInterface, queries: dict[str, str]):
        self._db = db
        self._queries = queries

    @staticmethod
    def data_to_model(data: Any) -> BookModel:
        return BookModel.recovery(
            id_book=data["id_book"],
            name=data["name"],
            author=data["author"],
            isbn=data["isbn"],
            created_at=data["created_at"],
            updated_at=data["updated_at"]
        )

    @staticmethod
    def entity_to_model(entity: Book) -> BookModel:
        return BookModel.create(entity)

# CRUD METHODS -------------------------------

    def create(self, entity: Book) -> Book:
        model = self.entity_to_model(entity)

        with self._db.transaction():
            self._db.execute(
                self._queries["create_book"], (
                model.entity.id_book,
                model.entity.name,
                model.entity.author,
                model.entity.isbn,
                model.created_at_timestamp,
                model.updated_at_timestamp
            ))

        return entity

    def update(self, entity: Book) -> Book:
        model = self.entity_to_model(entity)

        with self._db.transaction():
            self._db.execute(self._queries["update_book"], (
                model.entity.name,
                model.entity.author,
                model.entity.isbn,
                model.updated_at,
                model.entity.id_book
            ))

        return entity

    def delete(self, entity_id: str) -> None:
        with self._db.transaction():
            self._db.execute(self._queries["delete_book"], (entity_id,))

# GET METHODS -------------------------------

    def get_by_id(self, entity_id: str) -> Optional[Book]:
        data = self._db.fetchone(self._queries["get_book_by_id"], (entity_id,))

        if not data:
            return None

        model = self.data_to_model(data)

        return model.entity


    def get_by_name(self, name: str) -> list[Book]:
        data = self._db.fetchall(self._queries["get_book_by_name"], (name,))

        if not data:
            return []

        models = [self.data_to_model(row) for row in data]

        return [model.entity for model in models]

    def get_by_author(self, author: str) -> list[Book]:
        data = self._db.fetchall(self._queries["get_book_by_author"], (author,))

        if not data:
            return []

        models = [self.data_to_model(row) for row in data]

        return [model.entity for model in models]
    
    def get_by_isbn(self, isbn: str) -> list[Book]:
        data = self._db.fetchall(self._queries["get_book_by_isbn"], (isbn,))

        if not data:
            return []

        models = [self.data_to_model(row) for row in data]

        return [model.entity for model in models]


    def get_by_created_at(self, created_at: datetime) -> list[Book]:
        created_at_timestamp = date_to_timestamp(created_at)
        data = self._db.fetchall(self._queries["get_book_by_created_at"], (created_at_timestamp,))

        if not data:
            return []

        models = [self.data_to_model(row) for row in data]

        return [model.entity for model in models]

    def get_by_updated_at(self, updated_at: datetime) -> list[Book]:
        updated_at_timestamp = date_to_timestamp(updated_at)

        data = self._db.fetchall(self._queries["get_book_by_updated_at"], (updated_at_timestamp,))

        if not data:
            return []

        models = [self.data_to_model(row) for row in data]

        return [model.entity for model in models]
