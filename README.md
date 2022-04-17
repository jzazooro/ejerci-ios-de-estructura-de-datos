# ejerci-ios-de-estructura-de-datos

El enlace al repositorio de GitHub de este proyecto es el siguiente: [GitHub](https://github.com/jzazooro/ejerci-ios-de-estructura-de-datos.git)

He realizado tres ejercicios a cerca de estructurar datos y usarlos en determinadas situaciones.

### Ejercicio 1

```
class Bloque:
    def __init__(self):
        self.instrucciones=[]
    def agregarinstrucciones(self, instruccion):
        self.instrucciones.append(instruccion)

class Si:
    def __init__(self, condicion, entonces, si_no):
        self.condicion=condicion
        self.entonces=entonces
        self.si_no=si_no

class MientrasQue:
    def __init__(self, condicion, bloque):
        self.condicion=condicion
        self.bloque=bloque

class Mostrar:
    def __init__(self, mensaje):
        self.mensaje=mensaje
```

### Ejercicio 2

```
from asyncore import write
from fileinput import close


class datosdelusuario:
    def __init__(self, lineauno, lineados)->None:
        self.lineauno=lineauno
        self.lineados=lineados

class guardar():
    def __init__(self, nombredelarchivo, nuevosdatos)->None:
        self.textoarchivo=nuevosdatos
        self.nombredelarchivo=nombredelarchivo
        f=open(self.nombredelarchivo , "txt", "w", enconding="utf8")
        f=write(self.textoarchivo.lineauno , self.textoarchivo.lineados)
        f=close

class mayusculas():
    def __init__(self, datos)->None:
        self.datosprocesados=datosdelusuario
        self.datosprocesados.lineauno = datos.lineauno.upper()
        self.datosprocesados.lineados = datos.lineados.upper()
```

### Ejercicio 3

```
class naturaleza:
    def __init__(self):
        self.alimentaria=0.055
        self.servicio=20

class producto(naturaleza):
    def __init__(self, tasaiva):
        self.tasaiva=tasaiva

    def facturar(self):
        return 100 + 100*self.tasaiva

class factoryfactura(producto):
    def __init__(self):
        pass

    def crear(self):
        clase=producto(self.tasaiva)
        return clase 
```

### Main

```
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
```
