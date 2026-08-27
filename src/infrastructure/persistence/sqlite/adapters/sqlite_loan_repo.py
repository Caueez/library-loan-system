
from datetime import datetime, timedelta
from typing import Optional

from application.ports.loan_repo import BookLoanRepository

from domain.entities.loan import BookLoan
from infrastructure.persistence.sqlite.models.loan import LoanModel

from infrastructure.persistence.sqlite.implementation import SqliteImplementation



class SQLiteBookRepository(BookLoanRepository):
    def __init__(self, db: SqliteImplementation):
        self._db = db

    @staticmethod
    def model_to_entity(model: LoanModel) -> BookLoan:
        return BookLoan.recovery(
            id=model.loan.id,
            id_book=model.loan.id_book,
            id_user=model.loan.id_user,
            checked_in=model.loan.checked_in,
            checked_out=model.loan.checked_out
            )

    @staticmethod
    def entity_to_model(entity: BookLoan) -> LoanModel:
        return LoanModel.create(entity)

    def get_by_id(self, id: str) -> Optional[BookLoan]:
        cursor = self._db.cursor()
        data = cursor.execute(f"""
            SELECT * FROM loans WHERE id = '{id}'
        """).fetchone()

        if not data:
            return None

        return self.model_to_entity(LoanModel(**data))


    def get_by_id_book(self, id_book: str) -> list[BookLoan]:
        cursor = self._db.cursor()
        data = cursor.execute(f"""
            SELECT * FROM loans WHERE id_book = '{id_book}'
        """)

        if not data:
            return []

        return [self.model_to_entity(LoanModel(**book)) for book in data]

    def get_by_id_student(self, id_student: str) -> list[BookLoan]:
        cursor = self._db.cursor()
        data = cursor.execute(f"""
            SELECT * FROM loans WHERE id_student = '{id_student}'
        """)

        if not data:
            return []

        return [self.model_to_entity(LoanModel(**book)) for book in data]
    
    def get_by_checked_in(self, checked_in: datetime) -> list[BookLoan]:
        cursor = self._db.cursor()
        data = cursor.execute(f"""
            SELECT * FROM books WHERE checked_in = '{checked_in}'
        """)

        if not data:
            return []

        return [self.model_to_entity(LoanModel(**book)) for book in data]

    def get_checked_today(self) -> list[BookLoan]:
        cursor = self._db.cursor()
        data = cursor.execute(f"""
            SELECT * FROM loans WHERE 
                checked_out >= '{datetime.now().date()}'
                checked_out <= '{datetime.now().date() + timedelta(days=1)}'
        """)

        if not data:
            return []

        return [self.model_to_entity(LoanModel(**book)) for book in data]

    def set_book_return(self, id: str) -> None:
        cursor = self._db.cursor()
        cursor.execute(f"""
            UPDATE loans SET checked_out = ? WHERE id = ?
        """, (
            datetime.now(),
            id
        ))

        self._db.commit(cursor)

    def create(self, entity: BookLoan) -> BookLoan:
        cursor = self._db.cursor()
        model = self.entity_to_model(entity)

        cursor.execute(f"""
            INSERT INTO loans (id, id_book, id_user, checked_in, checked_out, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            model.loan.id,
            model.loan.id_book,
            model.loan.id_user,
            model.loan.checked_in,
            model.loan.checked_out,
            model.created_at,
            model.updated_at
        ))

        self._db.commit(cursor)

        return entity

    def update(self, entity: BookLoan) -> BookLoan:
        cursor = self._db.cursor()
        model = self.entity_to_model(entity)

        cursor.execute(f"""
            UPDATE loans SET id_book = ?, id_user = ?, checked_in = ?, checked_out = ?, updated_at = ? WHERE id = ?
        """, (
            model.loan.id_book,
            model.loan.id_user,
            model.loan.checked_in,
            model.loan.checked_out,
            model.updated_at,
            model.loan.id
        ))

        self._db.commit(cursor)

        return entity

    def delete(self, id: str) -> None:
        cursor = self._db.cursor()

        cursor.execute(f"""
            DELETE FROM loans WHERE id = ?
        """, (id,))

        self._db.commit(cursor)

    def get_by_created_at(self, created_at: datetime) -> list[BookLoan]:
        cursor = self._db.cursor()

        data = cursor.execute(f"""
            SELECT * FROM loans WHERE created_at = '{created_at}'
        """)

        if not data:
            return []

        return [self.model_to_entity(LoanModel(**book)) for book in data]

    def get_by_updated_at(self, updated_at: datetime) -> list[BookLoan]:
        cursor = self._db.cursor()

        data = cursor.execute(f"""
            SELECT * FROM loans WHERE updated_at = '{updated_at}'
        """)

        if not data:
            return []

        return [self.model_to_entity(LoanModel(**book)) for book in data]

    def get_by_checked_out(self, checked_out: datetime) -> list[BookLoan]:
        cursor = self._db.cursor()

        data = cursor.execute(f"""
            SELECT * FROM loans WHERE checked_out = '{checked_out}'
        """)

        if not data:
            return []

        return [self.model_to_entity(LoanModel(**book)) for book in data]

