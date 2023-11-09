# Codificando e Decodificando JSON

# Utilizamos o módulo Built_in JSON

from dados import *
import json

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
dados_json = json.dumps(lista)
print(dados_json)
print(type(dados_json))

dados_json2 = json.dumps(pessoas_dicionario, indent=4)
print(dados_json2)
print(type(dados_json2))
# Passamos o parâmetro indent para gerar o arquivo com uma estrutura mais adequada


# Convertendo um objeto JSON para dict

dados_dict = json.loads(pessoas_json)

for chave, valor in dados_dict.items():
    print(f'{chave} : {valor}')
    

