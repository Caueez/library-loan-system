from datetime import datetime
from typing import Any, Optional

from application.ports.loan_repo import BookLoanRepository

from domain.entities.loan import BookLoan

from infrastructure.persistence.sqlite.implementation import SqliteImplementation
from infrastructure.persistence.sqlite.models.loan import LoanModel


class SQLiteBookRepository(BookLoanRepository):
    def __init__(self, db: SqliteImplementation):
        self._db = db

    @staticmethod
    def row_to_model(row: Any) -> BookLoan:
        return BookLoan.recovery(
            id_loan=row["id_loan"],
            id_book=row["id_book"],
            id_student=row["id_student"],
            checked_in=row["checked_in"],
            checked_out=row["checked_out"]
        )

    @staticmethod
    def entity_to_model(entity: BookLoan) -> LoanModel:
        return LoanModel.create(entity)

    def get_by_id(self, entity_id: str) -> Optional[BookLoan]:
        QUERY = """
            SELECT * FROM loans WHERE id_loan = ?
        """
        
        data = self._db.fetchone(QUERY, (entity_id,))

        if not data:
            return None

        return self.row_to_model(data)

    def get_by_id_book(self, id_book: str) -> list[BookLoan]:
        QUERY = """
            SELECT * FROM loans WHERE id_book = ?
        """
        data = self._db.fetchall(QUERY, (id_book,))

        if not data:
            return []

        return [self.row_to_model(row) for row in data]

    def get_by_id_student(self, id_student: str) -> list[BookLoan]:
        QUERY = """
            SELECT * FROM loans WHERE id_student = ?
        """
        data = self._db.fetchall(QUERY, (id_student,))

        if not data:
            return []

        return [self.row_to_model(row) for row in data]

    def get_by_checked_in(self, checked_in: datetime) -> list[BookLoan]:
        QUERY = """
            SELECT * FROM loans WHERE checked_in = ?
        """
        checked_in_timestamp = int(checked_in.timestamp())
        data = self._db.fetchall(QUERY, (checked_in_timestamp,))

        if not data:
            return []

        return [self.row_to_model(row) for row in data]

    def get_checked_out_range(self, start_date: datetime, end_date: datetime) -> list[BookLoan]:
        QUERY = """
            SELECT * FROM loans
            WHERE checked_out >= ? AND checked_out < ?
        """
        data = self._db.fetchall(
            QUERY,
            (int(start_date.timestamp()), int(end_date.timestamp())),
        )

        if not data:
            return []

        return [self.row_to_model(row) for row in data]

    def create(self, entity: BookLoan) -> BookLoan:
        QUERY = """
            INSERT INTO loans (id_loan, id_book, id_student, checked_in, checked_out, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        model = self.entity_to_model(entity)
        model_dict = model.to_dict()

        with self._db.transaction():
            self._db.execute(
                QUERY,
                (
                    model_dict["id_loan"],
                    model_dict["id_book"],
                    model_dict["id_student"],
                    model_dict["checked_in"],
                    model_dict["checked_out"],
                    model_dict["created_at"],
                    model_dict["updated_at"],
                ),
            )

        return entity

    def update(self, entity: BookLoan) -> BookLoan:
        QUERY = """
            UPDATE loans
            SET id_book = ?, id_student = ?, checked_in = ?, checked_out = ?, updated_at = ?
            WHERE id_loan = ?
        """
        model = self.entity_to_model(entity)
        model_dict = model.to_dict()

        with self._db.transaction():
            self._db.execute(
                QUERY,
                (
                    model_dict["id_book"],
                    model_dict["id_student"],
                    model_dict["checked_in"],
                    model_dict["checked_out"],
                    model_dict["updated_at"],
                    model_dict["id_loan"],
                ),
            )

        return entity

    def delete(self, entity_id: str) -> None:
        QUERY = """
            DELETE FROM loans WHERE id_loan = ?
        """

        with self._db.transaction():
            self._db.execute(QUERY, (entity_id,))

    def get_by_created_at(self, created_at: datetime) -> list[BookLoan]:
        QUERY = """
            SELECT * FROM loans WHERE created_at = ?
        """
        created_at_timestamp = int(created_at.timestamp())
        data = self._db.fetchall(QUERY, (created_at_timestamp,))

        if not data:
            return []

        return [self.row_to_model(row) for row in data]

    def get_by_updated_at(self, updated_at: datetime) -> list[BookLoan]:
        QUERY = """
            SELECT * FROM loans WHERE updated_at = ?
        """
        updated_at_timestamp = int(updated_at.timestamp())
        data = self._db.fetchall(QUERY, (updated_at_timestamp,))

        if not data:
            return []

        return [self.row_to_model(row) for row in data]

    def get_by_checked_out(self, checked_out: datetime) -> list[BookLoan]:
        QUERY = """
            SELECT * FROM loans WHERE checked_out = ?
        """
        checked_out_timestamp = int(checked_out.timestamp())
        data = self._db.fetchall(QUERY, (checked_out_timestamp,))

        if not data:
            return []

        return [self.row_to_model(row) for row in data]
