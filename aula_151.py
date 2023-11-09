# Estabelecendo conexão com banco de dados SQLite

import sqlite3

con = sqlite3.connect('empresa.db')

print(type(con))

# Após estabelecer a conexão, realizamos as operações de banco de dados

con.close()
