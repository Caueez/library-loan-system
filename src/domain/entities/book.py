from __future__ import annotations

from uuid import uuid4


class Book:
    def __init__(self, id_book: str, name: str, author: str, isbn: str)-> None:
        self._id = id_book

        self._name = name
        self._author = author
        self._isbn = isbn

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
    def isbn(self) -> str:
        return self._isbn

    @name.setter
    def name(self, new_name: str) -> None:
        self._name = new_name

    @author.setter
    def author(self, new_author: str) -> None:
        self._author = new_author

    @isbn.setter
    def isbn(self, new_isbn: str) -> None:
        self._isbn = new_isbn


    @staticmethod
    def create(name: str, author: str, isbn: str) -> Book:
        id_book = str(uuid4())
        return Book(
            id_book=id_book,
            name=name, 
            author=author, 
            isbn=isbn
            )

    @staticmethod
    def recovery(id_book: str, name: str, author: str, isbn: str) -> Book:
        return Book(
            id_book=id_book,
            name=name, 
            author=author, 
            isbn=isbn
            )

    def to_dict(self) -> dict[str, str]:
        return {
            'id': self.id_book,
            'name': self.name,
            'author': self.author,
            'isbn': self.isbn
        }
