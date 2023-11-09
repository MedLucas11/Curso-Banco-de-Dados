import pymongo
con = pymongo.MongoClient()

db = con.cadastrodb

documento1 = {'nome': 'Lucas', 'sobrenome': 'Medeiros', 'twitter': 'MedLucas11'}

documento2 = {'site': 'http://www.pypro.com.br', 'youtube': 'http://www.youtube.com/@pypro_br'}

db.minhacolecao.insert_one(documento1)
db.minhacolecao.insert_one(documento2)

# Retornando todos os documentos da coleção

for doc in db.minhacolecao.find():
    print(doc)
