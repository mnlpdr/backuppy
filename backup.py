from datetime import datetime
import os

print('### Folder Backup ###')
print('')

pastaobservada = input('Digite o caminho da pasta a ser observada para backup: ')
pastaalvo = input('Digite o caminho onde você quer salvar seu backup')

os.mkdir(f'./backup_{pastaobservada}_{datetime}')

print('Observando a pasta: ' + pastaobservada)
print('Seus arquivos serão salvos na Pasta alvo: ' + pastaalvo)

arrayarquivos = []

while True:
    for arquivo in os.listdir(pastaobservada):
        if arquivo.endswith('.txt'):
            print('Arquivo: ' + arquivo + ' foi alterado')
            print('Copiando arquivo para pasta alvo')
            os.system(f'cp {pastaobservada}/{arquivo} {pastaalvo}')
            print('Arquivo copiado com sucesso')
            arrayarquivos.append(f'arquivo foi atualizado em' + datetime.now())


