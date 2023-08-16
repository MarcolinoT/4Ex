#3- Faça um programa que preencha por leitura um vetor de 5 posições, 
#e informe a posição em que um valor x (lido do teclado) aparece pela primeira 
#vez no vetor. Caso o valor x não seja encontrado, o programa deve imprimir o valor -1
vetor = []
for i in range(5):
    num=int(input(f'Digite o {i+1} valor:'))
    vetor.append(num)
print(vetor)
x = int(input(f'Qual numero solicitado?'))
for i,n in enumerate(vetor):
    if x ==n:
        print(f'esse numero está na {i}° posição')
    
if x not in vetor:
    print(-1)
            
    