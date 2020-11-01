tupla = (1, 2, 3, 4, 5, 6)
lista = [10, 20, 30, 40]
tupla_dos = (100, 200, 300, 400)

resultado = zip(tupla, lista, tupla_dos)
#resultado = tuple(resultado)
resultado = list(resultado)
print(resultado)


#uno, dos, tres, cuatro = tupla[0], tupla[1], tupla[2], tupla[3]
#uno, dos, tres, cuatro = tupla
#uno, dos, tres, *cuatro = tupla
#uno, *dos, cinco, seis = tupla

#print (uno)
#print (dos)
#print (cinco)
#print (seis)