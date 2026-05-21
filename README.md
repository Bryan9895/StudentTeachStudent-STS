# ProjetoSTS

Este projeto demonstra como conectar a um banco de dados MySQL usando Python.

## Arquivos

- `conexao.py`: helper para conectar ao banco de dados MySQL.
- `main.py`: exemplo de uso de `conexao.py` para abrir e fechar a conexão.
- `banco.sql`: script para criar a base `aula` e a tabela `alunos`.

## Instalação

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Crie o banco de dados MySQL:

```bash
mysql -u root -p < banco.sql
```

3. Ajuste as credenciais em `conexao.py` se necessário.

4. Execute o aplicativo:

```bash
python main.py
```
