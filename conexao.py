import mysql.connector as mysql

def conectar():
    conexao = mysql.connect(
        host='localhost',
        user='bryan',
        password='toor',
        database='aula'
    )
    return conexao