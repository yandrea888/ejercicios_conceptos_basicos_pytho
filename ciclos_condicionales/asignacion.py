"""calificacion = float (input("La calificación es: "))
color = None

if calificacion >=7:
    color = 'verde'
else: 
    color = 'rojo'

print(calificacion, color)"""

calificacion = float (input("La calificación es: "))
color = 'verde' if calificacion >=7 else 'rojo'
print(calificacion, color)
