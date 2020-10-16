#Ejercicio 9

import datetime

edad = int(input("ingrese la edad: "))
dia = int(input("Día de nacimiento: "))
mes = int(input("Mes de nacimiento: "))
anio = int(input("Año de nacimiento: "))


fecha_de_nacimiento = datetime.datetime(anio, mes, dia)
fecha_de_hoy = datetime.datetime.now()
diferencia = fecha_de_hoy - fecha_de_nacimiento
dias_vividos = diferencia.days
meses_vividos = 12 * edad

mensaje = "Has vivido {} día(s), y {} meses".format(
    dias_vividos , meses_vividos)  
print(mensaje)