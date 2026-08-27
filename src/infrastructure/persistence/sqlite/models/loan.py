from __future__ import annotations

from datetime import datetime

from src.domain.entities.loan import BookLoan


class LoanModel:
    def __init__(self, loan: BookLoan, created_at: datetime, updated_at: datetime) -> None:

        self.loan = loan

        self.created_at = created_at
        self.updated_at = updated_at

    @staticmethod
    def create(loan: BookLoan) -> LoanModel:
        current_time = datetime.now()
        return LoanModel(
            loan=loan,
            created_at=current_time,
            updated_at=current_time
        )

    @staticmethod
    def recovery(loan_model: LoanModel) -> LoanModel:
        return LoanModel(
            loan=loan_model.loan,
            created_at=loan_model.created_at,
            updated_at=loan_model.updated_at
        )

    def to_dict(self) -> dict[str, str | None]:
        loan_dict = self.loan.to_dict()
        loan_dict['created_at'] = datetime.strftime(self.created_at, '%d-%m-%Y')
        loan_dict['updated_at'] = datetime.strftime(self.updated_at, '%d-%m-%Y')
        return loan_dict
