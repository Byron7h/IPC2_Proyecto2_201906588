class Matriz:
    
    #CONSTRUCTOR
    def __init__(self, nombre, filas, columnas, matriz_ortogonal, vacios, llenos , fecha_hora):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.matriz_ortogonal = matriz_ortogonal
        self.vacios = vacios
        self.llenos = llenos
        self.fecha_hora = fecha_hora
       
    def getNombre(self):
        return self.nombre

    def getFilas(self):
        return self.filas
    
    def getColumnas(self):
        return self.columnas
    
    def getmatriz_ortogonal(self):
        return self.matriz_ortogonal
    
    def getVacios(self):
        return self.vacios
    
    def getLlenos(self):
        return self.llenos

    def getFecha_hora(self):
        return self.fecha_hora