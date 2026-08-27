from __future__ import annotations

from datetime import datetime

from src.domain.entities.book import Book


class BookModel:
    def __init__(self, book: Book, created_at: datetime, updated_at: datetime)-> None:

        self.book = book

        self.created_at = created_at
        self.updated_at = updated_at

    @staticmethod
    def create(book: Book) -> BookModel:
        current_time = datetime.now()
        return BookModel(
            book=book,
            created_at=current_time,
            updated_at=current_time
        )

    @staticmethod
    def recovery(book_model: BookModel) -> BookModel:
        return BookModel(
            book=book_model.book,
            created_at=book_model.created_at,
            updated_at=book_model.updated_at
        )

    def to_dict(self) -> dict[str, str]:
        book_dict = self.book.to_dict()
        book_dict['created_at'] = datetime.strftime(self.created_at, '%d-%m-%Y')
        book_dict['updated_at'] = datetime.strftime(self.updated_at, '%d-%m-%Y')
        return book_dict