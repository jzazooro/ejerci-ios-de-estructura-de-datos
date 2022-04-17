from clases.ejercicio1 import *



print("Ejercicio 1: ")

mostrar_ok=Mostrar('"OK"')
mostrar_ko=Mostrar('"KO"')
alternativa=Si("2+2 == 4", mostrar_ok, mostrar_ko)
bloque_alternativa=Bloque()
bloque_alternativa.agregarinstrucciones(alternativa)
bucle=MientrasQue(True, bloque_alternativa)

print("Ejercicio 2: ")

