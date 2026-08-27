
from sqlite3 import Connection, Cursor, connect


class SqliteImplementation:
    def __init__(self, uri: str) -> None:        
        self._uri = uri
        self._connection : Connection = connect(uri)

    def connect(self) -> None:
        if not self._uri:
            raise Exception("URI não informada")

        self.connection = connect(self._uri)

    def cursor(self) -> Cursor:
        if not self._connection:
            raise Exception("Conexão não estabelecida")
        
        return self._connection.cursor()

    def commit(self, cursor: Cursor) -> None:
        if not self._connection:
            raise Exception("Conexão não estabelecida")
        
        self._connection.commit()
        cursor.close()

    def roolback(self, cursor: Cursor) -> None:
        if not self._connection:
            raise Exception("Conexão não estabelecida")
        
        self._connection.rollback()
        cursor.close()

    def close(self) -> None:
        if not self._connection:
            raise Exception("Conexão não estabelecida")
        
        self._connection.close()