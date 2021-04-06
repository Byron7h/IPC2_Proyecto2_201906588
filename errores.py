class Error:

    def __init__(self, fecha_hora, descripcion):
        self.fecha_hora = fecha_hora
        self.descripcion = descripcion

    def getFecha_hora(self):
        return self.fecha_hora

    def getDescripcion(self):
        return self.descripcion
