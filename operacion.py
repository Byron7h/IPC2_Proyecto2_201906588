class Operacion:
    def __init__(self):
        self.tipo = None
        self.nombre_matriz = None
        self.XO= None
        self.Y0 = None
        self.XF = None
        self.YF = None
        self.cantidad = None
        self.filas = None
        self.columnas = None

    def __init__(self, tipo, nombre_matriz):
        self.tipo = tipo
        self.nombre_matriz = nombre_matriz