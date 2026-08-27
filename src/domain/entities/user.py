from __future__ import annotations



class User:
    def __init__(self, id_user: str, name: str, cpf: str):
        self._id_user = id_user
        self._name = name
        self._cpf = cpf

    @property
    def id_user(self):
        return self._id_user

    @property
    def cpf(self):
        return self._cpf

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        if len(new_name) < 3:
            raise ValueError("Name must be at least 3 characters long")
        
        self._name = new_name
