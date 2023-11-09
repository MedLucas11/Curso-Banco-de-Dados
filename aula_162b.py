from csv import reader

with open('filmes.csv', encoding='utf-8') as arquivo:
    leitor_csv = reader(arquivo)
    for linha in leitor_csv:
        print(f'Coluna 1: {linha[0]:10} | Coluna 2: {linha[1]:10} | Coluna 3: {linha[2]}')
