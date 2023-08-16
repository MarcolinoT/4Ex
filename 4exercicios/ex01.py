#Exercício 01 - 10/08/2023
#Dada a lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52] faça um programa que:
#a) imprima o maior elemento
#b) imprima o menor elemento
#c) imprima os números pares
#d) imprima o número de ocorrências do primeiro elemento da lista
#e) imprima a média dos elementos
#f) imprima a soma dos elementos de valor negativo

#a) imprima o maior elemento
lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
maior = max(lista)
print(f'O maior número da lista é: {maior}')


#b) imprima o menor elemento
menor = min(lista)
print(f'O menor númeoro da lista é: {menor}')

#c) imprima os números pares
pares=[]
for i in lista:
    if i%2==0:
        pares.append(i)
print(f'Os números pares da lista são: {pares}')     

#d) imprima o número de ocorrências do primeiro elemento da lista
contador= 0
for o in lista:
    if o == lista[0]:
        contador+=1
print(f'O números de ocorrencias do primeiro números na lista é: {contador}')  

#e) imprima a média dos elementos
soma = sum(lista)
media = soma/len(lista)
print(f'A média da lista é {media:.2f}')

#f) imprima a soma dos elementos de valor negativo
negativos = []
for k in lista:
    if k <=0:
        negativos.append(k)
soman=sum(negativos)        
print(f'Os numeros negativos são:{negativos}')
print(f'E a soma deles são:{soman}')        





