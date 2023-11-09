# Salvando e lendo arquivos JSON

from dados import *
import json

with open('pessoas.json', 'w') as arquivo:
    json.dump(pessoas_dicionario, arquivo, indent=4)


