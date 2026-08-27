
from db import BancoDeDadosEmprestimos



banco = BancoDeDadosEmprestimos()

banco.cadastrar_livro('Como ser gay', 'Autor 1', '123456789')
banco.cadastrar_livro('Sera que sou viado', 'Autor 2', '987654321')
banco.cadastrar_aluno('pablo', 'Y8fHt@example.com', '123456789')
banco.cadastrar_aluno('joao', 'Y8fHt@example.com', '123456789')

banco.emprestar_livro('pablo', 'Como ser gay')
banco.emprestar_livro('joao', 'Sera que sou viado')

banco.devolver_livro('Como ser gay')

print("ALUNOS")
print("ID\tNOME\tEMAIL\tCPF")
for aluno in banco.listar_alunos():
    print(aluno)

print("\n\n\nLIVROS")
print("ID\tNOME\tAUTOR\tISBN")
for livro in banco.listar_livros():
    print(livro)

print("\n\n\nEMPRESTIMOS")
print("ID\tDATA_DEVOLUCAO\tDATA_EMPRESTIMO\tID_LIVRO\tID_USUARIO")
for emprestimo in banco.listar_emprestimos():
    print(emprestimo)

