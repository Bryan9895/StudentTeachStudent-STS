import email
from conexao import conectar

conexao = conectar()
cursor = conexao.cursor()

def buscar_aluno(matricula):
    cursor.execute("select * from alunos where matricula = %s", (matricula,))
    aluno = cursor.fetchone()
    if aluno:
        print(aluno)
    else:
        print("Aluno não encontrado.")

def atualizar_aluno(matricula):
    cursor.execute("select * from alunos where matricula = %s", (matricula,))
    aluno = cursor.fetchone()
    if aluno:
        nome = input("Digite o novo nome do aluno: ")
        curso = input("Digite o novo curso do aluno: ")
        cursor.execute("update alunos set nome = %s, curso = %s where matricula = %s", (nome, curso, matricula))
        conexao.commit()
        print("Aluno atualizado com sucesso!")
    else:
        print("Aluno não encontrado.")
def remover_aluno(matricula):
    cursor.execute("select * from alunos where matricula = %s", (matricula,))
    conexao.commit()
    aluno = cursor.fetchone()
    if aluno:
        cursor.execute("delete from alunos where matricula = %s", (matricula,))
        conexao.commit()
        print("Aluno removido com sucesso!")
    else:
        print("Aluno não encontrado.")

def aluno_existe(matricula):
    sql = "SELECT * FROM alunos WHERE matricula = %s"
    cursor.execute(sql, (matricula,))
    resultado = cursor.fetchone()
    return resultado is not None

def listar_alunos():

    cursor.execute("SELECT * FROM alunos")
    resultado = cursor.fetchall()
    for aluno in resultado:
        print(aluno)

def cadastrar_aluno(nome, curso, matricula):
    sql = "INSERT INTO alunos (nome, curso, matricula) VALUES (%s, %s, %s)"
    valores = (nome, curso, matricula)
    cursor.execute(sql, valores)
    conexao.commit()
    print("Aluno cadastrado com sucesso!")

def aluno_github_existe(matricula):
    sql = "SELECT GitHub FROM alunos WHERE matricula = %s"
    cursor.execute(sql, (matricula,))
    resultado = cursor.fetchone()
    if resultado:
        print(f"O GitHub do aluno é: {resultado}")
    else:
        print("Aluno não encontrado.")

def procurar_email(matricula):
    sql = "SELECT email FROM alunos WHERE matricula = %s"
    cursor.execute(sql, (matricula,))
    resultado = cursor.fetchone()
    if resultado:
        print(f"O email do aluno é: {resultado}")
    else:
        print("Aluno não encontrado.")

def procurar_matricula(nome):
    sql = "SELECT matricula FROM alunos WHERE nome like %s"
    cursor.execute(sql, (nome,))
    resultado = cursor.fetchone()
    if resultado:
        print(f"A matrícula do aluno é: {resultado}")
    else:
        print("Aluno não encontrado.")

def presenca(matricula, data, num_faltas):
    if aluno_existe(matricula):
        sql = "insert into presenca (matricula, data, num_faltas) values (%s, %s, %s)"
        valores = [matricula, data, 0]
        cursor.execute(sql, valores)
        conexao.commit()
        print("Presença adicionada com sucesso")
    else:
        print("Aluno não existe")

conexao = conectar()
cursor = conexao.cursor()

while True:
    print("\nMenu:")
    print("1. Listar alunos")
    print("2. Cadastrar aluno")
    print("3. Atualizar aluno")
    print("4. Remover aluno")
    print("5. Buscar aluno")
    print("6. Procurar GitHub")
    print("7. Procurar email")
    print("8. Procurar matrícula")
    print("9. Adicionar falta")
    print("x. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        listar_alunos()
    elif escolha == '2':
        nome = input("Digite o nome do aluno: ")
        curso = input("Digite o curso do aluno: ")
        email = input("Digite o email do aluno: ")
        github = input("Digite o GitHub do aluno: ")
        matricula = input("Digite a matrícula do aluno: ")
        if aluno_existe (matricula):
            print("Esse aluno já está cadastrado. Tente novamente.")
        else:
            cadastrar_aluno(nome, curso, matricula, email, github)
    elif escolha == '3':
        nome = input("Digite o nome do aluno: ")
        curso = input("Digite o curso do aluno: ")
        email = input("Digite o email do aluno: ")
        github = input("Digite o GitHub do aluno: ")
        matricula = input("Digite a matrícula do aluno: ")
        if atualizar_aluno(matricula) == True:
            print("Aluno atualizado com sucesso!")
        else:
            print("Aluno não encontrado. Tente novamente.")

    elif escolha == '4':
        matricula = input("Digite a matrícula do aluno: ")
        remover_aluno(matricula)
    elif escolha == '5':
        buscar_aluno(matricula=input("Digite a matrícula do aluno: "))
    elif escolha == '6':
        aluno_github_existe(matricula=input("Digite a matrícula do aluno: "))
    elif escolha == '7':
        procurar_email(matricula=input("Digite a matrícula do aluno: "))
    elif escolha == '8':
       procurar_matricula(nome=input("Digite o nome do aluno: "))
    elif escolha == '9':

        matricula = input("Digite a matrícula do aluno: ")
        data = input("Digite a data da falta (YYYY-MM-DD): ")
        faltas = int(input("Digite o número de faltas: "))
        presenca(matricula, data, faltas)
    
    elif escolha == 'x':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")


cursor.close()
conexao.close()
