class bloque:
    def __init__(self):
        self.instrucciones=[]
    def agregarinstrucciones(self, instruccion):
        self.instrucciones.append(instruccion)
class Si:
    def __init__(self, condicion, entonces, si_no):
        self.condicion=condicion
        self.entonces=entonces
        self.si_no=si_no
