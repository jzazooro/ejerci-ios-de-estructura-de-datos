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
