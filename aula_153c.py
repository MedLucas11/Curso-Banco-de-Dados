# Inserindo dados de competências nas tabelas

import sqlite3

con = sqlite3.connect('empresa.db')
cur = con.cursor()

expressao_sql = 'INSERT INTO competencias (nome, area) values (?, ?)'

competencias = [
    ('Configurar linha de produção', 'PRODUÇÃO'),
    ('Elaborar plano de marketing', 'MARKETING'),
    ('Vender para Mercosul', 'VENDAS'),
    ('Realizar a manutenção da linha de produção', 'PRODUÇÃO'),
    ('Operar CAD e CAM', 'ENGENHARIA')
]

for competencia in competencias:
    cur.execute(expressao_sql, competencia)

con.commit()
con.close()
