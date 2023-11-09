# Inserindo documentos no banco de dados noSQL

import datetime
from pymongo import MongoClient

con = MongoClient('localhost', 27017)

db = con.db_cadastro

collection = db.db_cadastro

# Dados no MongoDB são representados usando JSON (Java Script Object Notation)
# Com o PyMongo utilizamos dicionários para representar os documentos

post1 = {
    "autor": 'Piva Jr.',
    "texto": 'Linguagem de Programação',
    "tags": ['Python', "C/C++", 'Java'],
    'data': datetime.datetime.utcnow()
}
print(type(post1))

colecao = db.posts

post_id = colecao.insert_one(post1).inserted_id
print(post_id)
# Além de inserir um post (Registro/Coleção), com o método inserted_id é criado uma chave especial _id.
# A chave é adicionada automaticamente ao documento.

post2 = {
    "autor": 'Piva Jr.',
    "texto": 'Estruturas de Dados',
    "tags": ['Listas', 'Pilhas', 'Árvores'],
    'data': datetime.datetime.utcnow()
}

colecao = db.posts
post_id = colecao.insert_one(post2).inserted_id
print(post_id)

# A função find() retorna um cursor e podemos então navegar pelos dados

for post in colecao.find():
    print(post)

# Para verificar o nome o Banco de Dados
print(db.name)

# Listando as coleções disponíveis
print(db.collection.names)
