# (1)

class Nodo_Interno:
# Este va tener los atributos de fila, columna, valor
    def __init__(self, fila, columna, valor):
        self.fila = fila
        self.columna = columna
        self.valor = valor

        # Apuntadores, estos los debemos especificar porque estos van a ir variando
        # al irse llenando la matriz
        self.derecha = None
        self.izquierda = None
        self.arriba = None
        self.abajo = None

class Nodo_Encabezado:
    # id será el número de fila o columna
    def __init__(self, id):
        self.id = id

        # Apuntadores, recordemos que es una lista doblemente enlazada, apuntador
        # hacia el siguiente y otro hacia anterior además de un acceso a los nodos internos
        self.siguiente = None
        self.anterior = None
        # Acceso, hacia el primer nodo interno de la fila o columna 
        self.acceso = None

