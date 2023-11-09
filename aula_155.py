# Consultando dados nas tabelas (utilizando fetchone())

import sqlite3

con = sqlite3.connect('empresa.db')
cur = con.cursor()


expressao_sql = """
    SELECT matricula, nome FROM funcionarios
    WHERE sexo = 'M'
"""

cur.execute(expressao_sql)

# O fetchone() recupera um registro de cada vez, não sobrecarregando a memória
linha = cur.fetchone()
print(f'Matrícula: {linha[0]} | Nome: {linha[1]}')

# A segunda execução traz outro resultado
linha = cur.fetchone()
print(f'Matrícula: {linha[0]} | Nome: {linha[1]}')

con.close()
