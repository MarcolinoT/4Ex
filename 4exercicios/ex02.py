#2- Faça um programa que preencha por leitura um vetor de 10 posições, e conta quantos valores diferentes existem no vetor.
vetor =[]
for i in range(10):
    num=int(input(f'Digite o {i+1}° número:'))
    vetor.append(num)
print(vetor)    
diferente = []
for n in vetor:
    if n not in diferente:
        diferente.append(n)
print(f'Numeros distintos da lista:{diferente}')
print(f'A quantidade de números diferentes:{len(diferente)}')        
