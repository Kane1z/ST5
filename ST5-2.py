def achou(numero):
    maior = 0
    for digito in str(numero):
        '''vou tornar o numero em uma string e assim posso verificar 1 por 1
        print(int(digito))
        '''
        if int(digito) > maior:
            maior = int(digito)
    return maior


numero = int(input("Digite um número inteiro: "))

print("O maior algarismo em",achou(numero))
