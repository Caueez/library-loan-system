from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import uuid4


class BookLoan:
    def __init__(self, id: str, id_book: str, id_user: str, checked_in: datetime, checked_out: Optional[datetime])-> None:
        self.id = id

        self.id_book = id_book
        self.id_user = id_user

        self.checked_in = checked_in
        self.checked_out = checked_out

    @staticmethod
    def create(id_book: str, id_user: str, checked_in: datetime) -> BookLoan:
        id = str(uuid4())
        current_time = datetime.now()
        return BookLoan(
            id=id,
            id_book=id_book,
            id_user=id_user,
            checked_in=current_time,
            checked_out=None
            )

    @staticmethod
    def recovery(id: str, id_book: str, id_user: str, checked_in: datetime, checked_out: Optional[datetime]) -> BookLoan:
        return BookLoan(
            id=id,
            id_book=id_book, 
            id_user=id_user, 
            checked_in=checked_in,
            checked_out=checked_out
            )

    def book_returned(self, checked_in: datetime = datetime.now()) -> None:
        self.checked_in = checked_in

    def to_dict(self) -> dict[str, str | None]:
        return {
            'id': self.id,
            'id_book': self.id_book,
            'id_user': self.id_user,
            'checked_in': datetime.strftime(self.checked_in, '%d-%m-%Y'),
            'checked_out': datetime.strftime(self.checked_out, '%d-%m-%Y') if self.checked_out else None
        }
