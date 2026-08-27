from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import uuid4

from domain.values.date import current_date_utc


class BookLoan:
    def __init__(self, id_loan: str, id_book: str, id_student: str, checked_in: datetime, checked_out: Optional[datetime])-> None:
        self._id_loan = id_loan

        self._id_book = id_book
        self._id_student = id_student

        self._checked_in = checked_in
        self._checked_out = checked_out

    @property
    def id_loan(self):
        return self._id_loan

    @property
    def id_book(self):
        return self._id_book

    @property
    def id_student(self):
        return self._id_student

    @property
    def checked_in(self):
        return self._checked_in

    @property
    def checked_out(self):
        return self._checked_out

    @staticmethod
    def create(id_book: str, id_student: str, checked_in: datetime) -> BookLoan:
        id_loan = str(uuid4())
        current_time = current_date_utc()
        return BookLoan(
            id_loan=id_loan,
            id_book=id_book,
            id_student=id_student,
            checked_in=current_time,
            checked_out=None
            )

    @staticmethod
    def recovery(id_loan: str, id_book: str, id_student: str, checked_in: datetime, checked_out: Optional[datetime]) -> BookLoan:
        return BookLoan(
            id_loan=id_loan,
            id_book=id_book, 
            id_student=id_student, 
            checked_in=checked_in,
            checked_out=checked_out
            )

    def book_returned(self, checked_in: datetime = datetime.now()) -> None:
        self._checked_in = checked_in

    def to_dict(self) -> dict[str, str | int]:
        return {
            'id': self.id_loan,
            'id_book': self.id_book,
            'id_student': self.id_student,
            'checked_in': int(self.checked_in.timestamp()),
            'checked_out': int(self.checked_out.timestamp()) if self.checked_out else 0
        }
