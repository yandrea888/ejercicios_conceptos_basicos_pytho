from math import pi

3.141592653589793
diametro = 50

circunferencia = pi * diametro

print("En cada vuelta la rueda recorre", circunferencia, "cm")

"1 km = 100000 cm"
circunferencia2 = circunferencia/100000 

print("En cada vuelta la rueda recorre", circunferencia2, "km")

vueltas=1/circunferencia2

print("la rueda dará ", vueltas, "vueltas")