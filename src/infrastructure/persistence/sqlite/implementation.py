
from contextlib import contextmanager
from sqlite3 import Connection, connect, Row
from typing import Any, Optional


class SqliteImplementation:
    def __init__(self, uri: str) -> None:        
        self._uri = uri
        self._connection : Connection = connect(uri)

    def connect(self) -> None:
        if not self._uri:
            raise Exception("URI não informada")

        self._connection = connect(self._uri)

    @contextmanager
    def transaction(self):

        try:
            yield
            self.commit()
        except Exception as e:
            self.roolback()
            raise e

    def execute(self, query: str, params: tuple[Optional[str | int], ...] = ()) -> None:
        if not self._connection:
            raise Exception("Conexão não estabelecida")

        cursor = self._connection.cursor()

        try:
            cursor.execute(query, params)
        finally:
            cursor.close()

    def fetchone(self, query: str, params: tuple[Optional[str | int], ...] = ()) -> Optional[Row]:
        if not self._connection:
            raise Exception("Conexão não estabelecida")

        cursor = self._connection.cursor()

        try:
            cursor.execute(query, params)
            return cursor.fetchone()
        finally:
            cursor.close()

    def fetchall(self, query: str, params: tuple[Optional[str | int], ...] = ()) -> list[Any]:
        if not self._connection:
            raise Exception("Conexão não estabelecida")

        cursor = self._connection.cursor()

        try:
            cursor.execute(query, params)
            return cursor.fetchall()
        finally:
            cursor.close()

    def commit(self) -> None:
        if not self._connection:
            raise Exception("Conexão não estabelecida")
        
        self._connection.commit()

    def roolback(self) -> None:
        if not self._connection:
            raise Exception("Conexão não estabelecida")
        
        self._connection.rollback()

    def close(self) -> None:
        if not self._connection:
            raise Exception("Conexão não estabelecida")
        
        self._connection.close()
