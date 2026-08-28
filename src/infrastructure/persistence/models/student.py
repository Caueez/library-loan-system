from __future__ import annotations

from datetime import datetime

from domain.values.date import current_date_utc, date_to_timestamp, timestamp_to_date
from src.domain.entities.student import Student


class StudentModel:
    def __init__(self, entity: Student, created_at: datetime, updated_at: datetime) -> None:

        self.entity = entity

        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def created_at_timestamp(self) -> int: return date_to_timestamp(self.created_at)

    @property
    def updated_at_timestamp(self) -> int: return date_to_timestamp(self.updated_at)

    @staticmethod
    def create(entity: Student) -> StudentModel:
        current_time = current_date_utc()
        return StudentModel(
            entity=entity,
            created_at=current_time,
            updated_at=current_time
        )

    @staticmethod
    def recovery(id_student: str, name: str, cpf: str, matriculation: str, created_at: int, updated_at: int) -> StudentModel:
        return StudentModel(
            entity=Student.recovery(
                id_student=id_student,
                name=name,
                cpf=cpf,
                matriculation=matriculation
            ),
            created_at=timestamp_to_date(created_at),
            updated_at=timestamp_to_date(updated_at)
        )
    