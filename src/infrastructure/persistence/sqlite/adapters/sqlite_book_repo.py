
from datetime import datetime
from typing import Optional

from application.ports.book_repo import BookRepository

from domain.entities.book import Book

from infrastructure.persistence.sqlite.models.book import BookModel
from infrastructure.persistence.sqlite.implementation import SqliteImplementation


class SQLiteBookRepository(BookRepository):
    def __init__(self, db: SqliteImplementation):
        self._db = db

    @staticmethod
    def model_to_entity(model: BookModel) -> Book:
        return Book.recovery(
            id_book=model.book.id_book,
            name=model.book.name,
            author=model.book.author,
            iSBN=model.book.iSBN
            )

    @staticmethod
    def entity_to_model(entity: Book) -> BookModel:
        return BookModel.create(entity)

    def get_by_id(self, entity_id: str) -> Optional[Book]:
        QUERY = """
            SELECT * FROM books WHERE id_book = ?
        """

        data = self._db.fetchone(QUERY, (entity_id,))

        if not data:
            return None

        return self.model_to_entity(BookModel(**data))


    def get_by_name(self, name: str) -> list[Book]:
        QUERY = """
            SELECT * FROM books WHERE name = ?
        """

        data = self._db.fetchall(QUERY, (name,))

        if not data:
            return []

        return [self.model_to_entity(BookModel(**book)) for book in data]

    def get_by_author(self, author: str) -> list[Book]:
        QUERY = """
            SELECT * FROM books WHERE author = ?
        """

        data = self._db.fetchall(QUERY, (author,))

        if not data:
            return []

        return [self.model_to_entity(BookModel(**book)) for book in data]
    
    def get_by_iSBN(self, iSBN: str) -> list[Book]:
        QUERY = """
            SELECT * FROM books WHERE iSBN = ?
        """

        data = self._db.fetchall(QUERY, (iSBN,))

        if not data:
            return []

        return [self.model_to_entity(BookModel(**book)) for book in data]

    def create(self, entity: Book) -> Book:
        QUERY = """
            INSERT INTO books (id_book, name, author, iSBN, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)
        """

        model = self.entity_to_model(entity)

        model_dict = model.to_dict()

        with self._db.transaction():
            self._db.execute(
                QUERY, (
                model_dict["id_book"],
                model_dict["name"],
                model_dict["author"],
                model_dict["iSBN"],
                model_dict["created_at"],
                model_dict["updated_at"]
            ))

        return entity

    def update(self, entity: Book) -> Book:
        QUERY = """
            UPDATE books SET name = ?, author = ?, iSBN = ?, updated_at = ? WHERE id_book = ?
        """

        model = self.entity_to_model(entity)

        model_dict = model.to_dict()

        with self._db.transaction():
            self._db.execute(QUERY, (
                model_dict["name"],
                model_dict["author"],
                model_dict["iSBN"],
                model_dict["updated_at"],
                model_dict["id_book"]
            ))

        return entity

    def delete(self, entity_id: str) -> None:
        QUERY = """
            DELETE FROM books WHERE id_book = ?
        """
        with self._db.transaction():
            self._db.execute(QUERY, (entity_id,))


    def get_by_created_at(self, created_at: datetime) -> list[Book]:
        QUERY = """
            SELECT * FROM books WHERE created_at = ?
        """

        created_at_timestamp = int(created_at.timestamp())
        data = self._db.fetchall(QUERY, (created_at_timestamp,))

        if not data:
            return []

        return [self.model_to_entity(BookModel(**book)) for book in data]

    def get_by_updated_at(self, updated_at: datetime) -> list[Book]:
        QUERY = """
            SELECT * FROM books WHERE updated_at = ?
        """
        updated_at_timestamp = int(updated_at.timestamp())

        data = self._db.fetchall(QUERY, (updated_at_timestamp,))

        if not data:
            return []

        return [self.model_to_entity(BookModel(**book)) for book in data]
