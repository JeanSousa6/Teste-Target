
numsFibo = []

numeroLimite = int(input('Insira um valor: '))
numsFibo.append(0)
numsFibo.append(1)



i = 0 
while(numsFibo[i + 1] < numeroLimite):
    numsFibo.append(numsFibo[i] + numsFibo[i + 1])
    i += 1


if(numsFibo[len(numsFibo) - 1] == numeroLimite or numeroLimite == 0):
    print(f'O numero {numeroLimite} pertence a sequencia de Fibonacci. ')
else:
    print(f'O numero {numeroLimite} nao pertence a sequencia de Fibonacci.')
