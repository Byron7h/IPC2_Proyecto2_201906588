class Pila:

    # El constructor de nuesta pila con
    # El Stack es una lista donde guardaremos los elementos que se agregen a la pila
    def __init__(self):
        self.top = None
        self.stack=[]

    # Método que devuelve el elemento en el top
    def getTop(self):
        return self.top

    # Método que agrega un elemento a la pila y lo coloca en el top
    # Como en las funciones que retorna lo que se elimina, acá podríamos colocarle 
    #   un retun self.top para que nos devolviera el elemento que agregamos
    #   recordemos que el append agrega un elemento al final de la lista
    def add(self, elemento):
        self.top = elemento
        self.stack.append(elemento)

    # Método para eliminar el elemento que está en el top, no recibimos ni una
    #   dirección, ni el dato a eliminar porque siempre será el top
    # Recordemos que el método pop, si no le pasamos ningún parámetro como en 
    #   este caso, elimina el elemento al final de la lista
    # También cambiaremos el top al elemento que ahora se encuentra al final 
    # de la lista [-1], acá también podríamos retornar si es que quiere
    def remove(self):
        self.stack.pop()
        #self.top= self.stack[-1]

    # Añadimos el método STR que es el que se ejecuta cuando le damos el print
    def __str__(self):
        return str(self.stack)

    # Añadimos el método que nos devuelve la longitud de la pila, comienza
    # sa contar desde 0
    def __len__(self):
        return len(self.stack) 


    
