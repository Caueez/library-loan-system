
from datetime import datetime
from typing import Any, Optional

from application.ports.student_repo import StudentRepository

from domain.entities.student import Student

from infrastructure.persistence.models.student import StudentModel
from infrastructure.persistence.interface import DBInterface


class StudentRepositoryAdapter(StudentRepository):
    def __init__(self, db: DBInterface, queries: dict[str, str]):
        self._db = db
        self._queries = queries

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
        model = self.entity_to_model(entity)

        with self._db.transaction():
            self._db.execute(self._queries["create_student"], (
                model.entity.id_student, 
                model.entity.name, 
                model.entity.cpf, 
                model.entity.matriculation, 
                model.created_at_timestamp, 
                model.updated_at_timestamp,
                )
            )

        return entity

    def update(self, entity: Student) -> Student:
        model = self.entity_to_model(entity)

        with self._db.transaction():
            self._db.execute(self._queries["update_student"], (
                model.entity.name, 
                model.entity.cpf,
                model.entity.matriculation,
                model.updated_at,
                model.entity.id_student, 
            ))

        return entity

    def delete(self, entity_id: str) -> None:
        with self._db.transaction():
            self._db.execute(self._queries["delete_student"], (entity_id,))

    def get_by_id(self, entity_id: str) -> Optional[Student]:
        data = self._db.fetchone(self._queries["get_student_by_id"], (entity_id,))

        if not data:
            return None

        model = self.row_to_model(data)

        return model.entity

    def get_by_created_at(self, created_at: datetime) -> list[Student]:
        created_at_timestamp = int(created_at.timestamp())

        data = self._db.fetchall(self._queries["get_student_by_created_at"], (created_at_timestamp,))

        if not data:
            return []

        models = [self.row_to_model(row) for row in data]

        return [model.entity for model in models]

    def get_by_updated_at(self, updated_at: datetime) -> list[Student]:
        updated_at_timestamp = int(updated_at.timestamp())

        data = self._db.fetchall(self._queries["get_student_by_updated_at"], (updated_at_timestamp,))

        if not data:
            return []

        models = [self.row_to_model(row) for row in data]
        
        return [model.entity for model in models]

    def get_by_name(self, name: str) -> list[Student]:
        data = self._db.fetchall(self._queries["get_student_by_name"], (name,))

        if not data:
            return []

        models = [self.row_to_model(row) for row in data]
                       
        return [model.entity for model in models]

    def get_by_cpf(self, cpf: str) -> Optional[Student]:
        data = self._db.fetchone(self._queries["get_student_by_cpf"], (cpf,))

        if not data:
            return None

        model = self.row_to_model(data)

        return model.entity

    def get_by_matriculation(self, matriculation: str) -> Optional[Student]:        
        data = self._db.fetchone(self._queries["get_student_by_matriculation"], (matriculation,))

        if not data:
            return None

        model = self.row_to_model(data)
        
        return model.entity
