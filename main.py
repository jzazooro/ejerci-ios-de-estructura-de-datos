from clases.ejercicio1 import *
from clases.ejercicio2 import *
from clases.ejercicio3 import *

print("Ejercicio 1: ")

mostrar_ok=Mostrar('"OK"')
mostrar_ko=Mostrar('"KO"')
alternativa=Si("2+2 == 4", mostrar_ok, mostrar_ko)
bloque_alternativa=Bloque()
bloque_alternativa.agregarinstrucciones(alternativa)
bucle=MientrasQue(True, bloque_alternativa)

print("Ejercicio 2: ")

lineauno=input("Por favor introduzca una oracion: ")
lineados=input("Por favor introduzca una oracion: ")
nombredelarchivo=input("Por favor introduzca el nombre con el que se guardara el archivo: ")
datosdelusuario=datosdelusuario(lineauno , lineados)
nuevosdatos=mayusculas(datosdelusuario).datosprocesados
guardar(nombredelarchivo, nuevosdatos)

print("Ejercicio 3: ")

naturaleza=naturaleza()

producto=producto(naturaleza.alimentaria)
precioneto=factoryfactura.crear(producto).facturar()
print("El precio neto del producto sera: ", precioneto)

producto=producto(naturaleza.servicio)
precioneto=factoryfactura.crear(producto).facturar()
print("El precio neto del producto sera: ", precioneto)
