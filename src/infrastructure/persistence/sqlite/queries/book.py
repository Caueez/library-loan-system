
CREATE_BOOK = """
            INSERT INTO books (id_book, name, author, isbn, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?)
        """

UPDATE_BOOK = """
            UPDATE books
            SET name = ?, author = ?, isbn = ?, updated_at = ?
            WHERE id_book = ?
        """

DELETE_BOOK = """
            DELETE FROM books WHERE id_book = ?
        """

GET_BOOK_BY_ID = """
            SELECT * FROM books WHERE id_book = ?
        """


GET_BOOK_BY_NAME = """
            SELECT * FROM books WHERE name = ?
        """

GET_BOOK_BY_AUTHOR = """
            SELECT * FROM books WHERE author = ?
        """

GET_BOOK_BY_ISBN = """
            SELECT * FROM books WHERE isbn = ?
        """

GET_BOOK_BY_CREATED_AT = """
            SELECT * FROM books WHERE created_at = ?
        """

GET_BOOK_BY_UPDATED_AT = """
            SELECT * FROM books WHERE updated_at = ?
        """

SQLITE_BOOK_QUERIES = {
    "create_book": CREATE_BOOK,
    "update_book": UPDATE_BOOK,
    "delete_book": DELETE_BOOK,
    "get_book_by_id": GET_BOOK_BY_ID,
    "get_book_by_name": GET_BOOK_BY_NAME,
    "get_book_by_author": GET_BOOK_BY_AUTHOR,
    "get_book_by_isbn": GET_BOOK_BY_ISBN,
    "get_book_by_created_at": GET_BOOK_BY_CREATED_AT,
    "get_book_by_updated_at": GET_BOOK_BY_UPDATED_AT,
}
