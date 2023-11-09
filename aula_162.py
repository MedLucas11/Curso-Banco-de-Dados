# Escrevendo arquivos CSV

# Podemos utilizar a classe writer ou DictWriter para escrever arquivos csv em python

from csv import writer, reader

with open('filmes.csv', 'w', newline='', encoding='utf-8') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Título', 'Gênero', 'Duração'])
    while filme != 'sair':
        filme = input('Digite o nome do filme: ')
        if filme != 'sair':
            genero = input('Digite o gênero do filme: ')
            duracao = input('Digite a duração do filme: ')
            escritor_csv.writerow([filme, genero, duracao])



