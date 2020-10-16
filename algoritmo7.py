import math

cateto_opuesto= 20
angulo_elevacion= math.radians(22)

"Cateto adyacente: es la longitud de la sombra"

tan = math.tan(angulo_elevacion)

cateto_adyacente = cateto_opuesto/tan

print("la longitud de la sombra", cateto_adyacente)