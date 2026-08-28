from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import uuid4

from dataclasses import dataclass

@dataclass
class BookLoanDTO:
    id_loan: str
    id_book: str
    id_student: str
    checked_in: datetime
    checked_out: Optional[datetime]

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
        return BookLoan(
            id_loan=id_loan,
            id_book=id_book,
            id_student=id_student,
            checked_in=checked_in,
            checked_out=None
            )

    @staticmethod
    def recovery(id_loan: str, id_book: str, id_student: str, checked_in: int, checked_out: Optional[int]) -> BookLoan:
        return BookLoan(
            id_loan=id_loan,
            id_book=id_book, 
            id_student=id_student, 
            checked_in=datetime.fromtimestamp(checked_in),
            checked_out=(
                datetime.fromtimestamp(checked_out) 
                if checked_out is not None 
                else None
                )
            )

    def book_returned(self, checked_out: datetime) -> None:
        self._checked_out = checked_out

    def to_dto(self) -> BookLoanDTO:
        return BookLoanDTO(
            id_loan=self._id_loan,
            id_book=self._id_book,
            id_student=self._id_student,
            checked_in=self._checked_in,
            checked_out=self._checked_out
        )
