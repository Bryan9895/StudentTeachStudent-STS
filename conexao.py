import mysql.connector as mysql

def conectar():
    conexao = mysql.connect(
        host='localhost',
        user='bryan',
        password='9895',
        database='aula'
    )
    return conexao