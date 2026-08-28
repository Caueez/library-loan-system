
CREATE_STUDENT = """
            INSERT INTO students (id_student, name, cpf, matriculation, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?)
        """

UPDATE_STUDENT = """
            UPDATE students
            SET name = ?, cpf = ?, matriculation = ?, updated_at = ?
            WHERE id_student = ?
        """

DELETE_STUDENT = """
            DELETE FROM students WHERE id_student = ?
        """

GET_STUDENT_BY_ID = """
            SELECT * FROM students WHERE id_student = ?
        """

GET_STUDENT_BY_CREATED_AT = """
            SELECT * FROM students WHERE created_at = ?
        """

GET_STUDENT_BY_UPDATED_AT = """
            SELECT * FROM students WHERE updated_at = ?
        """

GET_STUDENT_BY_NAME = """
            SELECT * FROM students WHERE name = ?
        """

GET_STUDENT_BY_CPF = """
            SELECT * FROM students WHERE cpf = ?
        """

GET_STUDENT_BY_MATRICULATION = """
            SELECT * FROM students WHERE matriculation = ?
        """


SQLITE_STUDENT_QUERIES = {
    "create_student": CREATE_STUDENT,
    "update_student": UPDATE_STUDENT,
    "delete_student": DELETE_STUDENT,
    "get_student_by_id": GET_STUDENT_BY_ID,
    "get_student_by_created_at": GET_STUDENT_BY_CREATED_AT,
    "get_student_by_updated_at": GET_STUDENT_BY_UPDATED_AT,
    "get_student_by_name": GET_STUDENT_BY_NAME,
    "get_student_by_cpf": GET_STUDENT_BY_CPF,
    "get_student_by_matriculation": GET_STUDENT_BY_MATRICULATION
}
