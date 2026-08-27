from typing import Optional, Protocol

from application.ports.default_repo import AbstractRepository
from src.domain.entities.student import Student


class StudentRepository(AbstractRepository[Student], Protocol):
    def get_by_name(self, name: str) -> list[Student]: ...
    
    def get_by_cpf(self, cpf: str) -> Optional[Student]: ...

    def get_by_matriculation(self, matriculation: str) -> Optional[Student]: ...
