

from application.ports.student_repo import StudentRepository
from domain.entities.student import Student


class CreateStudentUseCase:
    def __init__(self, student_repository: StudentRepository) -> None:
        self._student_repository = student_repository

    def execute(self, name: str, cpf: str) -> None:
        self._validate_cpf(cpf)

        matriculation = self._student_repository.get_last_matriculation()

        entity = Student.create(name, cpf, matriculation)

        self._student_repository.create(entity)

    def _validate_cpf(self, cpf: str) -> None:
        if self._student_repository.get_by_cpf(cpf):
            raise ValueError("CPF já cadastrado")