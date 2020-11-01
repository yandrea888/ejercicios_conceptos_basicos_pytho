diccionario = {"a":1, "b":2, "c":3, "a":4}

#resultado = diccionario["a"]
#resultado = "z" in diccionario
#resultado = "b" in diccionario
#resultado = diccionario.get("z", "La llave no existe")
#resultado = diccionario.get("a")
#resultado = diccionario.get("z", {}) # forma recomendada para obtener valores de los diccionarios

resultado = diccionario.setdefault("z", {})

print (resultado)
print (diccionario)