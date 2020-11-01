lenguajes = "Python; Java; Ruby; Php; Swift; JavaScrip; C#; C; C++"

separador = "; "
#resultado = lenguajes.split()
#resultado = lenguajes.split(";")
resultado = lenguajes.split(separador) #resultado es una lista
#nuevo_string = " ".join(resultado)
#nuevo_string = "_".join(resultado)
nuevo_string = separador.join(resultado)
#print (resultado)
#print (nuevo_string)

texto = """Este es un texto
con 
saltos 
de 

línea"""
resultado =texto.splitlines()
print (resultado)