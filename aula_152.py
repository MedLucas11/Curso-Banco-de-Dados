import sqlite3

con = sqlite3.connect('empresa.db')

cur = con.cursor()
# O cursor é o ponteiro de navegação pelo banco de dados

expressao_sql = """
    CREATE TABLE IF NOT EXISTS departamentos(
        id      INTEGER NOT NULL PRIMARY KEY,
        nome    varchar(20) NOT NULL
    )
"""

cur.execute(expressao_sql)

expressao_sql = """
    CREATE TABLE IF NOT EXISTS funcionarios(
        matricula   decimal(5) NOT NULL,
        nome        char(30) NOT NULL,
        rg          decimal(9) NOT NULL UNIQUE,
        sexo        char(1) CHECK(sexo in ('M', 'F')),
        depto       INTEGER,
        endereco    varchar(50),
        cidade      char(20) DEFAULT 'São Paulo',
        salario     decimal(10,2),
        PRIMARY KEY (matricula),
        FOREIGN KEY (depto) REFERENCES departamentos(id)
    )
"""

cur.execute(expressao_sql)

expressao_sql = """
    CREATE TABLE IF NOT EXISTS competencias(
        id    INTEGER NOT NULL,
        nome  varchar(30),
        area  varchar(20) CHECK(area in 
            ('ENGENHARIA',
             'PRODUÇÃO',
             'MARKETING',
             'VENDAS',
             'OUTRA')
        ),
        PRIMARY KEY (id AUTOINCREMENT)
    )
"""

cur.execute(expressao_sql)


expressao_sql = """
    CREATE TABLE IF NOT EXISTS funcionarios_competencias(
        matricula   decimal(5),
        id          INTEGER,
        data        date NOT NULL,
        FOREIGN KEY (matricula) REFERENCES funcionarios(matricula),
        FOREIGN KEY (id) REFERENCES competencias(id)
    )
"""

cur.execute(expressao_sql)

con.close()
# Criado o banco de dados, fechamos a conexão
