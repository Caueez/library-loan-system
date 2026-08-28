
CREATE_LOAN = """
            INSERT INTO loans (id_loan, id_book, id_student, checked_in, checked_out, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """

UPDATE_LOAN = """
            UPDATE loans
            SET id_book = ?, id_student = ?, checked_in = ?, checked_out = ?, updated_at = ?
            WHERE id_loan = ?
        """

DELETE_LOAN = """
            DELETE FROM loans WHERE id_loan = ?
        """

GET_LOAN_BY_ID = """
            SELECT * FROM loans WHERE id_loan = ?
        """

GET_LOAN_BY_ID_BOOK = """
            SELECT * FROM loans WHERE id_book = ?
        """

GET_LOAN_BY_ID_STUDENT = """
            SELECT * FROM loans WHERE id_student = ?
        """

GET_LOAN_BY_CHECKED_IN = """
            SELECT * FROM loans WHERE checked_in = ?
        """

GET_LOAN_BY_CHECKED_OUT = """
            SELECT * FROM loans WHERE checked_out = ?
        """

GET_LOAN_BY_CHECKED_OUT_RANGE = """
            SELECT * FROM loans WHERE checked_out BETWEEN ? AND ?
        """

GET_LOAN_BY_CREATED_AT = """
            SELECT * FROM loans WHERE created_at = ?
        """

GET_LOAN_BY_UPDATED_AT = """
            SELECT * FROM loans WHERE updated_at = ?
        """

SQLITE_LOAN_QUERIES = {
    "create_loan": CREATE_LOAN,
    "update_loan": UPDATE_LOAN,
    "delete_loan": DELETE_LOAN,
    "get_loan_by_id": GET_LOAN_BY_ID,
    "get_loan_by_id_book": GET_LOAN_BY_ID_BOOK,
    "get_loan_by_id_student": GET_LOAN_BY_ID_STUDENT,
    "get_loan_by_checked_in": GET_LOAN_BY_CHECKED_IN,
    "get_loan_by_checked_out": GET_LOAN_BY_CHECKED_OUT,
    "get_loan_by_checked_out_range": GET_LOAN_BY_CHECKED_OUT_RANGE,
    "get_loan_by_updated_at": GET_LOAN_BY_UPDATED_AT,
    "get_loan_by_created_at": GET_LOAN_BY_CREATED_AT,
}
