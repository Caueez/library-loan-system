from __future__ import annotations

from datetime import datetime
from typing import Optional

from domain.values.date import current_date_utc, date_to_timestamp, timestamp_to_date
from src.domain.entities.loan import BookLoan


class LoanModel:
    def __init__(self, entity: BookLoan, created_at: datetime, updated_at: datetime) -> None:

        self.entity = entity

        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def created_at_timestamp(self) -> int: return date_to_timestamp(self.created_at)

    @property
    def updated_at_timestamp(self) -> int: return date_to_timestamp(self.updated_at)

    @staticmethod
    def create(entity: BookLoan) -> LoanModel:
        current_time = current_date_utc()
        return LoanModel(
            entity=entity,
            created_at=current_time,
            updated_at=current_time
        )

    @staticmethod
    def recovery(id_loan: str, id_book: str, id_student: str, checked_in: int, checked_out: Optional[int], created_at: int, updated_at: int) -> LoanModel:
        return LoanModel(
            entity=BookLoan.recovery(
                id_loan=id_loan,
                id_book=id_book, 
                id_student=id_student, 
                checked_in=checked_in,
                checked_out=checked_out
            ),
            created_at=timestamp_to_date(created_at),
            updated_at=timestamp_to_date(updated_at)
        )
    