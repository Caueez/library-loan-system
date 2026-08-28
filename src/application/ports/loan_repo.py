from datetime import datetime
from typing import Protocol

from application.ports.abstract_repo import AbstractRepositoryInterface
from src.domain.entities.loan import BookLoan


class BookLoanRepositoryInterface(AbstractRepositoryInterface[BookLoan], Protocol):
    def get_by_id_book(self, id_book: str) -> list[BookLoan]: ...

    def get_by_id_student(self, id_student: str) -> list[BookLoan]: ...

    def get_by_checked_in(self, checked_in: datetime) -> list[BookLoan]: ...

    def get_by_checked_out(self, checked_out: datetime) -> list[BookLoan]: ...

    def get_checked_out_range(self, start_date: datetime, end_date: datetime) -> list[BookLoan]: ...