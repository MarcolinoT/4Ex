#4- Um dado é lançado 50 vezes, e o valor correspondente é armazenado em um vetor. 
#Faça um programa que simule o lançamento do dado e determine o percentual de ocorrências de face 6 do dado dentre esses 50 lançamentos.
lançamentos = 50
vetor = []
for i in range(lançamentos):
    jogada = int(input(f'{i+1}° jogada: '))
    vetor.append(jogada)
print(vetor)
faces6=0
for i in vetor:
    if i ==6:
        faces6+=1
porcentagem = (faces6/lançamentos)*100
print(f'{porcentagem}%')