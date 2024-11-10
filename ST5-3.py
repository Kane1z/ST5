def achou(numero):
    maior = 9
    for digito in str(numero):
        '''copiei o ST5-2 aumentei o max e comapro por < menor
        '''
        if int(digito) < maior:
            maior = int(digito)
    return maior

numero = int(input("Digite um número inteiro: "))

print("O menor algarismo em",achou(numero))