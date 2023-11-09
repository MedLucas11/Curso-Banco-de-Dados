# Podemos criar o arquivo também com o DictWriter, que irá receber as informações no formato de dicionário

from csv import DictWriter

with open('filmes2.csv', 'w', newline='', encoding='utf-8') as arquivo:
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)  # Preciso passar a informação do cabeçalho para o método
    escritor_csv.writeheader()  # Escrevo o cabeçalho no arquivo
    filme = None
    while filme != 'sair':
        filme = input('Digite o nome do filme: ')
        if filme != 'sair':
            genero = input('Digite o gênero do filme: ')
            duracao = input('Digite a duração do filme: ')
            escritor_csv.writerow({'Título': filme, 'Gênero': genero, 'Duração': duracao})
            # writerow() deve ser um dict
