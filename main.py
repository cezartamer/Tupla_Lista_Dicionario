from random import randint

# exercicio 72
# while True:
#     numero = int(input('Digite um número entre 0 e 20: ' ))
#     if  numero >=0 and  numero<=20:
#         break
#     else:
#         print('O número digitado não corresponde ao pedido!')

# tupla = ('zero','um','dois','três','quatro','cinco','seis','sete')

# print(tupla[numero])
# exercicio 73
# times =  ("Botafogo","Flamengo","Palmeiras","Fortaleza","Cruzeiro","São Paulo","Bahia","Athletico-PR","Bragantino","Atlético-MG","Vasco","Juventude","Internacional","Criciúma","Corinthians","Cuiabá","Vitória","Grêmio","Fluminense","Atlético-GO")

# print(times[0:5])

# print(times[-4:])

# print(sorted(times))

# print(times.index("Flamengo"))

# exercicio 74
tupla = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
ordernar = sorted(tupla)
for n in tupla:
    print(f'{n} ', end='')

print(f"\n{ordernar[0]}")
print(ordernar[-1])