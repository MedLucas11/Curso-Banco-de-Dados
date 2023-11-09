# Inserindo dados nas tabelas (departamentos)

import sqlite3

con = sqlite3.connect('empresa.db')
cur = con.cursor()

# Uma das formas de inserir dados nas tabelas

expressao_sql = 'INSERT INTO departamentos values (?, ?)'

departamentos = [(1, 'Produção'),
                 (2, 'Vendas'),
                 (3, 'Compras'),
                 (4, 'Marketing'),
                 (5, 'Informática')
                ]

for depto in departamentos:
    cur.execute(expressao_sql, depto)

con.commit()
# É necessário passar o método commit para efetivamente guardar os dados no BD

con.close()
