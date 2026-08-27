from __future__ import annotations

from datetime import datetime

from src.domain.entities.student import Student


class StudentModel:
    def __init__(self, student: Student, created_at: datetime, updated_at: datetime) -> None:

        self.student = student

        self.created_at = created_at
        self.updated_at = updated_at

    @staticmethod
    def create(student: Student) -> StudentModel:
        current_time = datetime.now()
        return StudentModel(
            student=student,
            created_at=current_time,
            updated_at=current_time
        )

    @staticmethod
    def recovery(student_model: StudentModel) -> StudentModel:
        return StudentModel(
            student=student_model.student,
            created_at=student_model.created_at,
            updated_at=student_model.updated_at
        )

    def to_dict(self) -> dict[str, str]:
        student_dict = self.student.to_dict()
        student_dict['created_at'] = datetime.strftime(self.created_at, '%d-%m-%Y')
        student_dict['updated_at'] = datetime.strftime(self.updated_at, '%d-%m-%Y')
        return student_dict
