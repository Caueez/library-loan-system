from __future__ import annotations

from uuid import uuid4

from domain.entities.user import User

from dataclasses import dataclass

@dataclass
class StudentDTO:
    id_student: str
    name: str
    cpf: str
    matriculation: str


class Student(User):
    def __init__(self, id_student: str, name: str, cpf: str, matriculation: str)-> None:
        super().__init__(id_user=id_student, name=name, cpf=cpf)

        self.matriculation = matriculation

    @property
    def id_student(self):
        return self._id_user

    @property
    def matriculation(self):
        return self._matriculation

    @matriculation.setter
    def matriculation(self, matriculation: str):
        self._matriculation = matriculation

    @staticmethod
    def create(name: str, cpf: str, matriculation: str) -> Student:
        id_student = str(uuid4())
        return Student(
            id_student=id_student,
            name=name, 
            cpf=cpf, 
            matriculation=matriculation
            )

    @staticmethod
    def recovery(id_student: str, name: str, cpf: str, matriculation: str) -> Student:
        return Student(
            id_student=id_student,
            name=name, 
            cpf=cpf, 
            matriculation=matriculation
            )

    def to_dto(self) -> StudentDTO:
        return StudentDTO(
            id_student=self.id_student,
            name=self.name,
            cpf=self.cpf,
            matriculation=self.matriculation   
        )