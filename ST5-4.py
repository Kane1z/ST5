def maior(lista):
    maior = 0
    for i in lista:
        if(i > maior):
            maior = i
    return maior

def menor(lista):
    menor = 9
    for i in lista:
        if(i < menor):
            menor = i
    return menor

def pares(lista):
    pares = []
    for i in lista:
        if(i % 2 == 0):
            pares.append(i)
    return pares

lista=[]
for i in range(10):
    lista.append(int(input(str(i+1)+" valor:")))

print("maior:",maior(lista))
print("menor:",menor(lista))
print("pares:",pares(lista))