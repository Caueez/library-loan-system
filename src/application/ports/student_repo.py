from typing import Optional, Protocol

from application.ports.abstract_repo import AbstractRepositoryInterface
from src.domain.entities.student import Student


class StudentRepositoryInterface(AbstractRepositoryInterface[Student], Protocol):
    def get_by_name(self, name: str) -> list[Student]: ...
    
    def get_by_cpf(self, cpf: str) -> Optional[Student]: ...

    def get_by_matriculation(self, matriculation: str) -> Optional[Student]: ...
