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

conexao = conectar()
cursor = conexao.cursor()

while True:
    print("\nMenu:")
    print("1. Listar alunos")
    print("2. Cadastrar aluno")
    print("3. Atualizar aluno")
    print("4. Remover aluno")
    print("5. Buscar aluno")
    print("6. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        listar_alunos()
    elif escolha == '2':
        nome = input("Digite o nome do aluno: ")
        curso = input("Digite o curso do aluno: ")
        matricula = input("Digite a matrícula do aluno: ")
        if aluno_existe (matricula):
            print("Esse aluno já está cadastrado. Tente novamente.")
        else:
            cadastrar_aluno(nome, curso, matricula)
    elif escolha == '3':

        nome = input("Digite o nome do aluno: ")
        curso = input("Digite o curso do aluno: ")
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
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")


cursor.close()
conexao.close()
