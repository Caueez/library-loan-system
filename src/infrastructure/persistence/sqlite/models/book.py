from __future__ import annotations

from datetime import datetime

from domain.values.date import current_date_utc
from src.domain.entities.book import Book


class BookModel:
    def __init__(self, entity: Book, created_at: datetime, updated_at: datetime)-> None:

        self.entity = entity

        self.created_at = created_at
        self.updated_at = updated_at

    @staticmethod
    def create(entity: Book) -> BookModel:
        current_time = current_date_utc()
        return BookModel(
            entity=entity,
            created_at=current_time,
            updated_at=current_time
        )

    @staticmethod
    def recovery(entity: Book, created_at: int, updated_at: int) -> BookModel:
        return BookModel(
            entity=entity,
            created_at=datetime.fromtimestamp(created_at),
            updated_at=datetime.fromtimestamp(updated_at)
        )

    def to_dict(self) -> dict[str, str | int]:
        entity_dict = self.entity.to_dict()
        model_dict : dict[str, str | int] = {**entity_dict}
        model_dict['created_at'] = int(self.created_at.timestamp())
        model_dict['updated_at'] = int(self.updated_at.timestamp())
        return model_dict