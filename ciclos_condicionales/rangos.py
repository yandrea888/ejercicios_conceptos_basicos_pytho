#for valor in range (101):
    #print (valor)

"""for valor in range (10):
    print (valor)"""

#for valor in range (1, 20):
#for valor in range (-10, 11):
"""for valor in range (1, 101, 2):
    print (valor)"""

lista = [1,2,3,4,5,6,7]

"""for indice in range(len(lista)):
    print("índice:", indice, "valor:", lista[indice])"""

for indice, valor in enumerate(lista, 10):
    print("índice:", indice, "valor:", valor)