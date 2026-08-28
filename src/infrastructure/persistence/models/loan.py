from __future__ import annotations

from datetime import datetime
from typing import Optional

from domain.values.date import current_date_utc
from src.domain.entities.loan import BookLoan

from dataclasses import dataclass

@dataclass
class BookLoanModelDTO:
    id_loan: str
    id_book: str
    id_student: str
    checked_in: datetime
    checked_out: Optional[datetime]
    created_at: int
    updated_at: int


class LoanModel:
    def __init__(self, entity: BookLoan, created_at: datetime, updated_at: datetime) -> None:

        self.entity = entity

        self.created_at = created_at
        self.updated_at = updated_at

    @staticmethod
    def create(entity: BookLoan) -> LoanModel:
        current_time = current_date_utc()
        return LoanModel(
            entity=entity,
            created_at=current_time,
            updated_at=current_time
        )

    @staticmethod
    def recovery(entity: BookLoan, created_at: int, updated_at: int) -> LoanModel:
        return LoanModel(
            entity=entity,
            created_at=datetime.fromtimestamp(created_at),
            updated_at=datetime.fromtimestamp(updated_at)
        )

    def to_dto(self) -> BookLoanModelDTO:
        entity_dto = self.entity.to_dto()

        model_dto = BookLoanModelDTO(
            id_loan=entity_dto.id_loan,
            id_book=entity_dto.id_book,
            id_student=entity_dto.id_student,
            checked_in=entity_dto.checked_in,
            checked_out=entity_dto.checked_out,
            created_at=int(self.created_at.timestamp()),
            updated_at=int(self.updated_at.timestamp())
        )
        
        return model_dto
