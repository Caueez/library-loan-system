import sqlite3

from sqlite3 import Connection

from datetime import datetime


class BancoDeDadosEmprestimos:

    def __init__(self):
        self.conn = self.connect()
        self.create_tables()
        

    def connect(self) -> Connection:
        conn = sqlite3.connect('db.db')
        return conn

    def listar_livros(self):
        cursor = self.conn.cursor()

        cursor.execute(f"""
            SELECT * FROM livros
        """)

        return cursor.fetchall()

    def listar_alunos(self):
        cursor = self.conn.cursor()

        cursor.execute(f"""
            SELECT * FROM alunos
        """)

        return cursor.fetchall()

    def listar_emprestimos(self):
        cursor = self.conn.cursor()

        cursor.execute(f"""
            SELECT * FROM emprestimos
        """)

        return cursor.fetchall()

    def cadastrar_livro(self, nome: str, autor: str, ISBN: str):
        cursor = self.conn.cursor()

        cursor.execute(f"""
            INSERT INTO livros (nome, autor, ISBN) VALUES ('{nome}', '{autor}', '{ISBN}')
        """)

        self.conn.commit()
        cursor.close()

    def cadastrar_aluno(self, nome: str, email: str, CPF: str):
        cursor = self.conn.cursor()

        cursor.execute(f"""
            INSERT INTO alunos (nome, email, CPF) VALUES ('{nome}', '{email}', '{CPF}')
        """)

        self.conn.commit()
        cursor.close()


    def emprestar_livro(self, nome_aluno: str, nome_livro: str):
        cursor = self.conn.cursor()

        disponivel = cursor.execute(f"""
            SELECT * FROM emprestimos WHERE id_livro = (SELECT id_livro FROM livros WHERE nome = '{nome_livro}') AND data_devolucao IS NULL
        """).fetchall()

        if disponivel:
            print('Livro indisponivel')
            return

        id_livro = cursor.execute(f"""
            SELECT id_livro FROM livros WHERE nome = '{nome_livro}'
        """).fetchall()[0][0]

        id_aluno = cursor.execute(f"""
            SELECT id_usuario FROM alunos WHERE nome = '{nome_aluno}'
        """).fetchall()[0][0]

        cursor.execute(f"""
            INSERT INTO emprestimos (data_devolucao, data_emprestimo, id_livro, id_usuario) 
            VALUES (NULL, {datetime.now().strftime('%d-%m-%Y')}, {id_livro}, {id_aluno})
        """)

        self.conn.commit()
        cursor.close()

    def devolver_livro(self, nome_self.conn.commit()
        cursor.close()livro: str):
        cursor = self.conn.cursor()

        id_livro = cursor.execute(f"""
            SELECT id_livro FROM livros WHERE nome = '{nome_livro}'
        """).fetchall()[0][0]

        id_emprestimo = cursor.execute(f"""
            SELECT id_emprestimo FROM emprestimos WHERE id_livro = '{id_livro}' AND data_devolucao IS NULL
        """).fetchall()[0][0]

        cursor.execute(f"""
            UPDATE emprestimos SET data_devolucao = {datetime.now().strftime('%d-%m-%Y')} WHERE id_emprestimo = '{id_emprestimo}'
        """)

        self.conn.commit()
        cursor.close()