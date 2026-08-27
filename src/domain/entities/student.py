from __future__ import annotations

from uuid import uuid4

from domain.entities.user import User


class Student(User):
    def __init__(self, id: str, name: str, cpf: str, matriculation: str)-> None:
        super().__init__(id=id, name=name, cpf=cpf)

        self.matriculation = matriculation


    @staticmethod
    def create(name: str, cpf: str, matriculation: str) -> Student:
        id = str(uuid4())
        return Student(
            id=id,
            name=name,
            cpf=cpf,
            matriculation=matriculation
            )

    @staticmethod
    def recovery(id: str, name: str, cpf: str, matriculation: str) -> Student:
        return Student(
            id=id,
            name=name,
            cpf=cpf,
            matriculation=matriculation
            )

    def to_dict(self) -> dict[str, str]:
        return {
            'id': self.id,
            'name': self.name,
            'cpf': self.cpf,
            'matriculation': self.matriculation
        }