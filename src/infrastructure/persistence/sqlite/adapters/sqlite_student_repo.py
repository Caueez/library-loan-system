
from datetime import datetime

from application.ports.student_repo import StudentRepository
from domain.entities.student import Student

from infrastructure.persistence.sqlite.models.student import StudentModel
from infrastructure.persistence.sqlite.implementation import SqliteImplementation


class SQLiteStudentRepository(StudentRepository):
    def __init__(self, db: SqliteImplementation):
        self._db = db

    @staticmethod
    def model_to_entity(model: StudentModel) -> Student:
        return Student.recovery(
            id=model.student.id,
            name=model.student.name,
            cpf=model.student.cpf,
            matriculation=model.student.matriculation
        )

    @staticmethod
    def entity_to_model(entity: Student) -> StudentModel:
        return StudentModel.create(entity)

    def create(self, entity: Student) -> Student:
        cursor = self._db.cursor()

        model = self.entity_to_model(entity)

        cursor.execute(f"""
            INSERT INTO students (id, name, cpf, matriculation, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)
        """, (
            model.student.id,
            model.student.name,
            model.student.cpf,
            model.student.matriculation,
            model.created_at,
            model.updated_at
        ))

        self._db.commit(cursor)

        return entity

    def update(self, entity: Student) -> Student:
        raise NotImplementedError

    def delete(self, id: str) -> None:
        raise NotImplementedError

    def get_by_id(self, id: str) -> Student | None:
        raise NotImplementedError

    def get_by_created_at(self, created_at: datetime) -> list[Student]:
        raise NotImplementedError

    def get_by_updated_at(self, updated_at: datetime) -> list[Student]:
        raise NotImplementedError

    def get_by_bame(self, name: str) -> list[Student]:
        raise NotImplementedError

    def get_by_cpf(self, cpf: str) -> Student | None:
        raise NotImplementedError

    def get_by_matriculation(self, matriculation: datetime) -> Student | None:
        raise NotImplementedError


    