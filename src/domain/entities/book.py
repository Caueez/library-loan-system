from __future__ import annotations

from uuid import uuid4


class Book:
    def __init__(self, id: str, name: str, author: str, ISBN: str)-> None:
        self.id = id

        self.name = name
        self.author = author
        self.ISBN = ISBN


    @staticmethod
    def create(name: str, author: str, ISBN: str) -> Book:
        id = str(uuid4())
        return Book(
            id=id,
            name=name,
            author=author,
            ISBN=ISBN
            )

    @staticmethod
    def recovery(id: str, name: str, author: str, ISBN: str) -> Book:
        return Book(
            id=id,
            name=name, 
            author=author, 
            ISBN=ISBN
            )

    def to_dict(self) -> dict[str, str]:
        return {
            'id': self.id,
            'name': self.name,
            'author': self.author,
            'ISBN': self.ISBN
        }
