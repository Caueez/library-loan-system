
from datetime import datetime
from typing import Any, Optional

from application.ports.student_repo import StudentRepository

from domain.entities.student import Student

from infrastructure.persistence.sqlite.models.student import StudentModel
from infrastructure.persistence.sqlite.implementation import SqliteImplementation


class SQLiteStudentRepository(StudentRepository):
    def __init__(self, db: SqliteImplementation):
        self._db = db

    @staticmethod
    def row_to_model(row: Any) -> StudentModel:
        return StudentModel.recovery(
            entity=Student.recovery(
                id_student=row["id_student"],
                name=row["name"],
                cpf=row["cpf"],
                matriculation=row["matriculation"]
            ),
            created_at=row["created_at"],
            updated_at=row["updated_at"]
        )

    @staticmethod
    def entity_to_model(entity: Student) -> StudentModel:
        return StudentModel.create(entity)

    def create(self, entity: Student) -> Student:
        QUERY = """
            INSERT INTO students (id_student, name, cpf, matriculation, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?)
        """

        model = self.entity_to_model(entity)

        model_dict = model.to_dict()

        with self._db.transaction():
            self._db.execute(QUERY, (
                model_dict["id_student"],
                model_dict["name"],
                model_dict["cpf"],
                model_dict["matriculation"],
                model_dict["created_at"],
                model_dict["updated_at"]
            ))

        return entity

    def update(self, entity: Student) -> Student:
        QUERY = """
            UPDATE students
            SET name = ?, cpf = ?, matriculation = ?, updated_at = ?
            WHERE id_student = ?
        """

        model = self.entity_to_model(entity)
        model_dict = model.to_dict()

        with self._db.transaction():
            self._db.execute(QUERY, (
                model_dict["name"],
                model_dict["cpf"],
                model_dict["matriculation"],
                model_dict["updated_at"],
                model_dict["id_student"],
            ))

        return entity

    def delete(self, entity_id: str) -> None:
        QUERY = """
            DELETE FROM students WHERE id_student = ?
        """

        with self._db.transaction():
            self._db.execute(QUERY, (entity_id,))

    def get_by_id(self, entity_id: str) -> Optional[Student]:
        QUERY = """
            SELECT * FROM students WHERE id_student = ?
        """

        data = self._db.fetchone(QUERY, (entity_id,))

        if not data:
            return None

        model = self.row_to_model(data)

        return model.entity

    def get_by_created_at(self, created_at: datetime) -> list[Student]:
        QUERY = """
            SELECT * FROM students WHERE created_at = ?
        """

        created_at_timestamp = int(created_at.timestamp())
        data = self._db.fetchall(QUERY, (created_at_timestamp,))

        if not data:
            return []

        models = [self.row_to_model(row) for row in data]

        return [model.entity for model in models]

    def get_by_updated_at(self, updated_at: datetime) -> list[Student]:
        QUERY = """
            SELECT * FROM students WHERE updated_at = ?
        """

        updated_at_timestamp = int(updated_at.timestamp())
        data = self._db.fetchall(QUERY, (updated_at_timestamp,))

        if not data:
            return []

        models = [self.row_to_model(row) for row in data]
        
        return [model.entity for model in models]

    def get_by_name(self, name: str) -> list[Student]:
        QUERY = """
            SELECT * FROM students WHERE name = ?
        """

        data = self._db.fetchall(QUERY, (name,))

        if not data:
            return []

        models = [self.row_to_model(row) for row in data]
                       
        return [model.entity for model in models]

    def get_by_cpf(self, cpf: str) -> Optional[Student]:
        QUERY = """
            SELECT * FROM students WHERE cpf = ?
        """

        data = self._db.fetchone(QUERY, (cpf,))

        if not data:
            return None

        model = self.row_to_model(data)

        return model.entity

    def get_by_matriculation(self, matriculation: str) -> Optional[Student]:
        QUERY = """
            SELECT * FROM students WHERE matriculation = ?
        """
        
        data = self._db.fetchone(QUERY, (matriculation,))

        if not data:
            return None

        model = self.row_to_model(data)
        
        return model.entity
