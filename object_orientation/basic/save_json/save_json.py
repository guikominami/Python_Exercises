import os

# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json

CAMINHO_ARQUIVO = '.\.\.\arquivo.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

os.system('cls')

p1 = Pessoa('Gui', 46)
p2 = Pessoa('Lara', 46)
p3 = Pessoa('Otto', 12)
bd = [vars(p1), p2.__dict__, vars(p3)]

with open(CAMINHO_ARQUIVO, 'w') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)