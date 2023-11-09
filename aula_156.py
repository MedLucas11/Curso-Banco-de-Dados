# Consultando dados utilizando input
import sqlite3

con = sqlite3.connect('empresa.db')
cur = con.cursor()

# Coloco um LIKE :arg como uma variável que será preenchida a partir do input, isso é particular do SQLite
expressao_sql = """
    SELECT matricula, nome FROM funcionarios
    WHERE nome LIKE :arg
"""
# Em outros BDs como o MySQL, coloco um %s na condição, o 's' sendo de 'string'

nome = input('Digite o nome do funcionário que quer localizar: ')
arg = (f'%{nome}%',)  # Faço um argumento (nesse formato para evitar sql injection) e com a vírgula para "ser" uma tupla
cur.execute(expressao_sql, arg)  # Executo a expressão buscando o argumento

dados = cur.fetchall()

for linha in dados:
    print(f'Matrícula: {linha[0]} | Nome: {linha[1]}')
