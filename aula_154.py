# Consultando dados nas tabelas

import sqlite3

con = sqlite3.connect('empresa.db')
cur = con.cursor()

# Faço a expressão na linguagem sql
expressao_sql = """
    SELECT matricula, nome FROM funcionarios
    WHERE sexo = 'M'
"""

# Executo o comando sql
cur.execute(expressao_sql)

# Recupero os dados e guardo em uma variável
dados = cur.fetchall()

# Imprimo as informações desejadas
for linha in dados:
    print(f'Matrícula: {linha[0]} | Nome: {linha[1]}')

con.close()
