# (2)
#El self es para poder acceder a las variables locales
# importamos nuestros objetos nodo

from nodos import Nodo_Encabezado, Nodo_Interno

# Creamos nuestra lista encabezado, recordemos que esta será una lista 
# doblemente enlazada y ordenada; en decir que como las columnas tienen
# número estas deben estar ordenadas de acuerdo a este, si no se nos descompone la matriz

class Lista_encabezado:
    # Vamos a tener un primero
    def __init__(self, primero = None):
        self.primero = primero
    # Método para insertar un nodo
    def setEncabezado(self, nuevo):
        # Validaciones de una lista

        # 1. Verificamos si primero es igual a none, si lo es significa que la lista está vacia
        if self.primero == None:
            # Si lo está ahora primero va a ser igual a nuevo (el que nos están enviando)
            self.primero = nuevo
        
        # 2. Verificamos orden de los encabezados, si su número de fila o columna es menor 
        # al valor que tenía primero, significa que este debe estar antes del que ya tenía
        # establecido como primero (Rotación), Solo verificamos si este debe ser primero, por lo que
        # solo debemos ir a preguntarle a nuestro actual primero, a los otros nodos ya no, porque sabemos
        # que son mayores al actual primero.
        elif nuevo.id < self.primero.id:

            # a. Establecemos los nuevos apuntadores
            # El nuevo va a tener como siguiente al primero y primero va a tener 
            # como anterior a nuevo
            nuevo.siguiente = self.primero
            self.primero.anterior = nuevo   

            # b. Hacemos la rotación de puestos, para encontrar como primero a nuestro
            # nuevo primero
            self.primero = nuevo

        # 3. Que pasa si el número de fila o columna queda en medio o último de la lista de encabezados (osea no es primero)
        else:
            # a. Establecemos una variable auxiliar para poder recorrer la lista de encabezados
            actual = self.primero

            # b. Recorremos, recordar siempre que recorremos una lista debemos cambiar el valor
            # del actual al que le sigue, porque si no se crea un bucle infinito (Ya nos ha pasado)
            while actual.siguiente != None:
                #Le pregunto al siguiente del actual porque el actual al comenzar es el primero, y al primero
                # ya le pregunté en el elif, por lo que si llega hasta acá es porque no aplica
                if nuevo.id < actual.siguiente.id:
                    # Vamos a ir preguntandole a cada encabezado ya registrado si al nuevo es menor a el 
                    # por lo que el nuevo va a dejar atrás a todos los menores y como está ordenada, va a quedar atrás
                    # del primer mayor que encuentre. Por eso no hay peligro que quede desordenada
                    
                    # Acá es donde hacemos la rotación. Le digo al actual que el nuevo va a ser su siguiente
                    # Y al actual.siguiente que su anterior va a ser el nuevo
                    nuevo.siguiente = actual.siguiente
                    actual.siguiente.anterior = nuevo
                    nuevo.anterior = actual
                    actual.siguiente = nuevo
                    break
                    #Vamos colocando los nuevos apuntadores de dos en dos, uno por cada nodo que afecta (por hacer un anterior y un siguiente)
                actual = actual.siguiente
                    
            # Ahora que pasa si recorre toda la lista y no encuentra ningun actual.siguiente.id que sea mayor
            # Es porque es el último, cómo lo sabemos? porque nuna entró a if anterior  
            if actual.siguiente == None:
                #Acá actual quedó como el último nodo de la lista, por el while
                actual.siguiente = nuevo
                nuevo.anterior = actual

    def getEncabezado(self, id):
        # Nos va a devolver un nodo de tipo encabezado
        actual = self.primero
        no_encontrado = False
        while actual != None:
            if actual.id == id:
                no_encontrado = True
                return actual
            actual = actual.siguiente
        if no_encontrado:
            return None