from contextlib import contextmanager
from typing import Optional

from sqlite3 import Connection, connect, Row

from infrastructure.persistence.interface import DBInterface

class SqliteDB(DBInterface):
    def __init__(self, uri: str) -> None:        
        self._uri = uri
        self._connection : Connection = connect(uri)
        self._connection.row_factory = Row

        self._config()
    
    def _config(self) -> None:
        self._connection.execute("PRAGMA foreign_keys = ON")

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
            self.rollback()
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

    def fetchall(self, query: str, params: tuple[Optional[str | int], ...] = ()) -> list[Row]:
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

    def rollback(self) -> None:
        if not self._connection:
            raise Exception("Conexão não estabelecida")
        
        self._connection.rollback()

    def close(self) -> None:
        if not self._connection:
            raise Exception("Conexão não estabelecida")
        
        self._connection.close()
