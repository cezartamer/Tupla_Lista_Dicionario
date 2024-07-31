import random

## Faça um programa que leia a média de um aluno

# hist = dict()

# hist['nome'] = (input("Digite seu nome: "))
# hist['media'] = (input("Digite sua média: "))

# if float(hist['media']) >= 7:
#     hist['situacao'] = 'aprovado'
# else:
#     hist['situacao'] = 'reprovado'

# print(hist)

## 4 jogadores jogando 1 dado, guardar em um dic e ordenar

jogadores = {}
lista = []

for c in range(1,5):
    nome = "Jogador" + str(c)
    jogadores[nome] = random.randint(1,6)


for j in sorted(jogadores, key = jogadores.get, reverse=True):
    print(j, jogadores[j])