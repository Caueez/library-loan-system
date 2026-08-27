from __future__ import annotations

from datetime import datetime

from domain.values.date import current_date_utc
from src.domain.entities.book import Book


class BookModel:
    def __init__(self, book: Book, created_at: datetime, updated_at: datetime)-> None:

        self.book = book

        self.created_at = created_at
        self.updated_at = updated_at

    @staticmethod
    def create(book: Book) -> BookModel:
        current_time = current_date_utc()
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

    def to_dict(self) -> dict[str, str | int]:
        book_dict = self.book.to_dict()
        model_dict : dict[str, str | int] = {**book_dict}
        model_dict['created_at'] = int(self.created_at.timestamp())
        model_dict['updated_at'] = int(self.updated_at.timestamp())
        return model_dict