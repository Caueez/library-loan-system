
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
            id=model.book.id,
            name=model.book.name,
            author=model.book.author,
            ISBN=model.book.ISBN
            )

    @staticmethod
    def entity_to_model(entity: Book) -> BookModel:
        return BookModel.create(entity)

    def get_by_id(self, id: str) -> Optional[Book]:
        cursor = self._db.cursor()
        data = cursor.execute(f"""
            SELECT * FROM books WHERE id = '{id}'
        """).fetchone()

        if not data:
            return None

        return self.model_to_entity(BookModel(**data))


    def get_by_name(self, name: str) -> list[Book]:
        cursor = self._db.cursor()
        data = cursor.execute(f"""
            SELECT * FROM books WHERE name = '{name}'
        """)

        if not data:
            return []

        return [self.model_to_entity(BookModel(**book)) for book in data]

    def get_by_author(self, author: str) -> list[Book]:
        cursor = self._db.cursor()
        data = cursor.execute(f"""
            SELECT * FROM books WHERE author = '{author}'
        """)

        if not data:
            return []

        return [self.model_to_entity(BookModel(**book)) for book in data]
    
    def get_by_ISBN(self, ISBN: str) -> list[Book]:
        cursor = self._db.cursor()
        data = cursor.execute(f"""
            SELECT * FROM books WHERE ISBN = '{ISBN}'
        """)

        if not data:
            return []

        return [self.model_to_entity(BookModel(**book)) for book in data]

    def create(self, entity: Book) -> Book:
        cursor = self._db.cursor()
        model = self.entity_to_model(entity)

        cursor.execute(f"""
            INSERT INTO books (id, name, author, ISBN, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)
        """, (
            model.book.id,
            model.book.name,
            model.book.author,
            model.book.ISBN,
            model.created_at,
            model.updated_at
        ))

        self._db.commit(cursor)

        return entity

    def update(self, entity: Book) -> Book:
        cursor = self._db.cursor()
        model = self.entity_to_model(entity)

        cursor.execute(f"""
            UPDATE books SET name = ?, author = ?, ISBN = ?, updated_at = ? WHERE id = ?
        """, (
            model.book.name,
            model.book.author,
            model.book.ISBN,
            model.updated_at,
            model.book.id
        ))

        self._db.commit(cursor)

        return entity

    def delete(self, id: str) -> None:
        cursor = self._db.cursor()

        cursor.execute(f"""
            DELETE FROM books WHERE id = ?
        """, (id,))

        self._db.commit(cursor)

    def get_by_created_at(self, created_at: datetime) -> list[Book]:
        cursor = self._db.cursor()

        data = cursor.execute(f"""
            SELECT * FROM books WHERE created_at = '{created_at}'
        """)

        if not data:
            return []

        return [self.model_to_entity(BookModel(**book)) for book in data]

    def get_by_updated_at(self, updated_at: datetime) -> list[Book]:
        cursor = self._db.cursor()

        data = cursor.execute(f"""
            SELECT * FROM books WHERE updated_at = '{updated_at}'
        """)

        if not data:
            return []

        return [self.model_to_entity(BookModel(**book)) for book in data]

