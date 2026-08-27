from __future__ import annotations

from uuid import uuid4

from domain.entities.user import User


class Student(User):
    def __init__(self, id_user: str, name: str, cpf: str, matriculation: str)-> None:
        super().__init__(id_user=id_user, name=name, cpf=cpf)

        self.matriculation = matriculation

    @property
    def matriculation(self):
        return self._matriculation

    @matriculation.setter
    def matriculation(self, matriculation: str):
        self._matriculation = matriculation

    @staticmethod
    def create(name: str, cpf: str, matriculation: str) -> Student:
        id_user = str(uuid4())
        return Student(
            id_user=id_user,
            name=name, 
            cpf=cpf, 
            matriculation=matriculation
            )

    @staticmethod
    def recovery(id_user: str, name: str, cpf: str, matriculation: str) -> Student:
        return Student(
            id_user=id_user,
            name=name, 
            cpf=cpf, 
            matriculation=matriculation
            )

    def to_dict(self) -> dict[str, str]:
        return {
            'id_user': self.id_user,
            'name': self.name,
            'cpf': self.cpf,
            'matriculation': self.matriculation
        }