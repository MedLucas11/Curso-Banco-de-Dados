# Fazendo consultas ao banco de dados noSQL

import pymongo

con = pymongo.MongoClient()
# Se não passar nenhum parâmetro de host e port ele utiliza o default 'localhost' e 27017

db = con.cadastrodb
print(con.collection.names)

# Criando uma coleção

"""db.create_collection('minhacolecao')"""
print(con.collection_names)

# Inserindo dados na segunda coleção

"""db.minhacolecao.insert_one({
    'Título': 'Curso de Python',
    'Descrição': 'Curso completo da Linguagem Python',
    'by': 'pyPRO',
    'url': 'www.pypro.com.br',
    'tags': ['python', 'profissional', 'pyPRO'],
    'likes': 200
})"""

print(db.list_collection_names())
# Para listar as coleções presentes no banco de dados

# Para consultar utilizamos find_one()
print(db.minhacolecao.find_one())
