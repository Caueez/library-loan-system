from __future__ import annotations

from uuid import uuid4


class Book:
    def __init__(self, id_book: str, name: str, author: str, iSBN: str)-> None:
        self._id = id_book

        self._name = name
        self._author = author
        self._iSBN = iSBN

    @property
    def id_book(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    @property
    def iSBN(self) -> str:
        return self._iSBN

    @name.setter
    def name(self, new_name: str) -> None:
        self._name = new_name

    @author.setter
    def author(self, new_author: str) -> None:
        self._author = new_author

    @iSBN.setter
    def iSBN(self, new_iSBN: str) -> None:
        self._iSBN = new_iSBN


    @staticmethod
    def create(name: str, author: str, iSBN: str) -> Book:
        id_book = str(uuid4())
        return Book(
            id_book=id_book,
            name=name, 
            author=author, 
            iSBN=iSBN
            )

    @staticmethod
    def recovery(id_book: str, name: str, author: str, iSBN: str) -> Book:
        return Book(
            id_book=id_book,
            name=name, 
            author=author, 
            iSBN=iSBN
            )

    def to_dict(self) -> dict[str, str]:
        return {
            'id': self.id_book,
            'name': self.name,
            'author': self.author,
            'iSBN': self.iSBN
        }
