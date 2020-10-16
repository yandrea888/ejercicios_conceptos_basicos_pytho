
nombre = input("¿Cuál es tu nombre?\n")

edad = int(input("¿Cuál es tu edad?\n"))

peso = float(input("¿Cuál es tu peso?\n"))

autorizado = input("¿Estás autorizado?(si/no)\n") == "si"

print("Hola", nombre)
print("Edad", edad)
print("Peso", peso)
print("Autorizado", autorizado)