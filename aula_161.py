# Manipulando arquivos CSV
# Utilizamos o pacote built_in "csv"

from csv import reader

with open('exemplo.csv') as arquivo:
    leitor_csv = reader(arquivo)
    for linha in leitor_csv:
        print(f'Coluna 1: {linha[0]:18} | Coluna 2: {linha[1]:16} | Coluna 3: {linha[2]}')

