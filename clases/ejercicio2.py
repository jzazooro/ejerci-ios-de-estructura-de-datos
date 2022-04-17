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