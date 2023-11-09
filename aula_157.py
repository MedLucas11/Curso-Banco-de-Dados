# Banco de dados noSQL (MongoDB)

# Para utilizar com o python, baixamos o pacote PYMONGO com pip install.

# Importamos a função MongoClient para estabelecer conexão com o banco de dados

from pymongo import MongoClient

con = MongoClient('localhost', 27017)
print(type(con))

# Uma única instância dessa conexão pode suportar diversos bancos de dados

db = con.db_cadastro
print(type(db))

# Dentro dos BDs criados, podemos criar uma coleção, que será um grupo de documentos armazenados nesse banco de dados

collection = db.db_cadastro
print(type(collection))
