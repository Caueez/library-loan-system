from datetime import datetime
from typing import Any, Optional

from application.ports.loan_repo import BookLoanRepositoryInterface

from domain.entities.loan import BookLoan

from infrastructure.persistence.interface import DBInterface
from infrastructure.persistence.models.loan import LoanModel


class BookLoanRepository(BookLoanRepositoryInterface):
    def __init__(self, db: DBInterface, QUERIES: dict[str, str]):
        self._db = db
        self._QUERIES = QUERIES

    @staticmethod
    def row_to_model(row: Any) -> LoanModel:
        return LoanModel.recovery(
            entity=BookLoan.recovery(
                id_loan=row["id_loan"],
                id_book=row["id_book"],
                id_student=row["id_student"],
                checked_in=row["checked_in"],
                checked_out=row["checked_out"]
            ),
            created_at=row["created_at"],
            updated_at=row["updated_at"]
        )

    @staticmethod
    def entity_to_model(entity: BookLoan) -> LoanModel:
        return LoanModel.create(entity)

    def create(self, entity: BookLoan) -> BookLoan:
        model = self.entity_to_model(entity)
        model_dto = model.to_dto()

        with self._db.transaction():
            self._db.execute(
                self._QUERIES["create_loan"],
                (
                    model_dto.id_loan,
                    model_dto.id_book,
                    model_dto.id_student,
                    model_dto.checked_in,
                    model_dto.checked_out,
                    model_dto.created_at,
                    model_dto.updated_at,
                ),
            )

        return entity

    def update(self, entity: BookLoan) -> BookLoan:
        model = self.entity_to_model(entity)
        model_dto = model.to_dto()

        with self._db.transaction():
            self._db.execute(
                self._QUERIES["update_loan"],
                (
                    model_dto.id_book,
                    model_dto.id_student,
                    model_dto.checked_in,
                    model_dto.checked_out,
                    model_dto.updated_at,
                    model_dto.id_loan,
                ),
            )

        return entity

    def delete(self, entity_id: str) -> None:
        with self._db.transaction():
            self._db.execute(self._QUERIES["delete_loan"], (entity_id,))

    def get_by_id(self, entity_id: str) -> Optional[BookLoan]:        
        data = self._db.fetchone(self._QUERIES["get_loan_by_id"], (entity_id,))

        if not data:
            return None

        model = self.row_to_model(data)

        return model.entity

    def get_by_id_book(self, id_book: str) -> list[BookLoan]:
        data = self._db.fetchall(self._QUERIES["get_loan_by_id_book"], (id_book,))

        if not data:
            return []

        models = [self.row_to_model(row) for row in data]
                
        return [model.entity for model in models]

    def get_by_id_student(self, id_student: str) -> list[BookLoan]:
        data = self._db.fetchall(self._QUERIES["get_loan_by_id_student"], (id_student,))

        if not data:
            return []

        models = [self.row_to_model(row) for row in data]
                        
        return [model.entity for model in models]

    def get_by_checked_in(self, checked_in: datetime) -> list[BookLoan]:
        checked_in_timestamp = int(checked_in.timestamp())
        data = self._db.fetchall(self._QUERIES["get_loan_by_checked_in"], (checked_in_timestamp,))

        if not data:
            return []

        models = [self.row_to_model(row) for row in data]
                        
        return [model.entity for model in models]

    def get_by_checked_out(self, checked_out: datetime) -> list[BookLoan]:
        checked_out_timestamp = int(checked_out.timestamp())
        data = self._db.fetchall(self._QUERIES["get_loan_by_checked_out"], (checked_out_timestamp,))

        if not data:
            return []

        models = [self.row_to_model(row) for row in data]
                        
        return [model.entity for model in models]

    def get_checked_out_range(self, start_date: datetime, end_date: datetime) -> list[BookLoan]:
        data = self._db.fetchall(
            self._QUERIES["get_loan_by_checked_out_range"],
            (int(start_date.timestamp()), int(end_date.timestamp())),
        )

        if not data:
            return []

        models = [self.row_to_model(row) for row in data]
                        
        return [model.entity for model in models]

    def get_by_created_at(self, created_at: datetime) -> list[BookLoan]:
        created_at_timestamp = int(created_at.timestamp())
        data = self._db.fetchall(self._QUERIES["get_loan_by_created_at"], (created_at_timestamp,))

        if not data:
            return []

        models = [self.row_to_model(row) for row in data]
                        
        return [model.entity for model in models]

    def get_by_updated_at(self, updated_at: datetime) -> list[BookLoan]:
        updated_at_timestamp = int(updated_at.timestamp())
        data = self._db.fetchall(self._QUERIES["get_loan_by_updated_at"], (updated_at_timestamp,))

        if not data:
            return []

        models = [self.row_to_model(row) for row in data]
                        
        return [model.entity for model in models]
