# Podemos utilizar o método DictReader do módulo csv também, que irá transformar o arquivo em um dicionário

from csv import DictReader

with open('exemplo.csv') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        print(f'Coluna 1: {linha["Continente"]:18} | Coluna 2: {linha["Pais"]:16} | Coluna 3: {linha["Capital"]}')

# Com o DictReader, as informações da primeira linha se tornam as chaves dos dicionários
