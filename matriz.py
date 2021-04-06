#(3)
# Importamos lo que vamos a utilizar
from nodos import Nodo_Encabezado, Nodo_Interno
from encabezado import Lista_encabezado

class Matriz:
    def __init__(self):
    #Acá bamos a tener nuestros stributos de tipo lista_Encabezados
        self.Encabezado_Filas = Lista_encabezado()
        self.Encabezado_Columnas = Lista_encabezado()

    def Insertar(self, fila, columna, valor):
        #Acá bamos a recibir toda la info que va a tener la matriz -> Nodo_Interno
        # Vamoa a hacer una inseción por fila y por columna, porque desde ambos se 
        # podrá acceder
        #(1) Creamos en nodo interno que vamos a ingresar a l matriz
        nuevo = Nodo_Interno(fila, columna, valor)

        #(2) Insecion por fila
        eFila = self.Encabezado_Filas.getEncabezado(fila)
        #(2.1) Validación 1
        #Si getEncabezado nos devuelve None, es que aún no se ha registrado la fila
        # eso quiere decir que debemos crear el encabezado
        if eFila == None:

            #(2.1.1) Creamos un nuevo nodo encabezado, ya que no existe aún
            eFila = Nodo_Encabezado(fila)

            #(2.1.2)
            # Le damos el acceso al nodo_interno (apuntador del 
            # encabezado hacia el nodo interno más próximo a la derecha)(flechita negra de nuestro dibujito)
            eFila.acceso = nuevo
            # Acá le estamos diciendo que su apuntador hacia adentro va a apuntar hacia
            # El nodo que acabamod de crear, va a apuntar hacia este porque es el primero que 
            # Se inserta, recordemos que acabamos de crear también el encabezado 

            # Este nuevo nodo lo ingresamos a la lista de encabezados
            self.Encabezado_Filas.setEncabezado(eFila)

        #(2.2) Validación 2
        # Si no nos devuelve None quiere decir que el nodo_Encabezado ya existe 
        #En nuestra lista de encabezados,Vamos a ubicarlo donde corresponde (Siendo primero, segundo etc) y a colocar los apuntadores adecuados
        else:

            # Si la posición de columna del nodo nuevo es menor a la del acceso 
            # quiere decis que se insertará a antes de este, por lo que
            # el apuntuntador acceso al nodo cambiaría, y apuntaría al nuevo nodo
            if nuevo.columna < eFila.acceso.columna:

                # Manejamos los apuntadores
                nuevo.derecha =  eFila.acceso
                eFila.acceso.izquierda = nuevo
                # Colocamos el nuevo acceso del nodo_Encabezado
                eFila.acceso = nuevo

            #Si no entra en el if significa que el nodo acceso sigue siendo el mismo
            else:
                #Recorremos comenzando por el acceso 
                actual = eFila.acceso

                while actual.derecha != None:
                    #Si es menor debemos ingresarlo en esa posición, recordemos que es una lista ordenada
                    if nuevo.columna < actual.derecha.columna:
                        nuevo.derecha = actual.derecha
                        actual.derecha.izquierda = nuevo
                        nuevo.izquierda = actual
                        actual.derecha = nuevo
                        break
                    actual = actual.derecha
                
                # Si el ciclo termina y el actual.derecha = none quiere decir
                # que este nodo no tiene un posterior, esde es el último porque nunca entró
                # al if, redordemos que al terminar de recorrer  y no entrar al if el actual es el último
                if actual.derecha == None:
                    actual.derecha = nuevo
                    nuevo.izquierda = actual



        #(3) Insecion por columna
        eColumna = self.Encabezado_Columnas.getEncabezado(columna)
        #(3.1) Validación 1
        #Si getEncabezado nos devuelve None, es que aún no se ha registrado la columna
        # eso quiere decir que debemos crear el encabezado
        if eColumna == None:

            #(2.1.1) Creamos un nuevo nodo encabezado, ya que no existe aún
            eColumna = Nodo_Encabezado(columna)

            #(2.1.2)
            # Le damos el acceso al nodo_interno (apuntador del 
            # encabezado hacia el nodo interno más próximo a la derecha)(flechita negra de nuestro dibujito)
            eColumna.acceso = nuevo
            # Acá le estamos diciendo que su apuntador hacia adentro va a apuntar hacia
            # El nodo que acabamod de crear, va a apuntar hacia este porque es el primero que 
            # Se inserta, recordemos que acabamos de crear también el encabezado 

            # Este nuevo nodo lo ingresamos a la lista de encabezados
            self.Encabezado_Columnas.setEncabezado(eColumna)

        #(2.2) Validación 2
        # Si no nos devuelve None quiere decir que el nodo_Encabezado ya existe 
        #En nuestra lista de encabezados,Vamos a ubicarlo donde corresponde (Siendo primero, segundo etc) y a colocar los apuntadores adecuados
        else:

            # Si la posición de fila del nodo nuevo es menor a la del acceso 
            # quiere decis que se insertará a antes de este, por lo que
            # el apuntuntador acceso al nodo cambiaría, y apuntaría al nuevo nodo
            if nuevo.fila < eColumna.acceso.fila:

                # Manejamos los apuntadores
                nuevo.abajo =  eColumna.acceso
                eColumna.acceso.arriba = nuevo
                # Colocamos el nuevo acceso del nodo_Encabezado
                eColumna.acceso = nuevo

            #Si no entra en el if significa que el nodo acceso sigue siendo el mismo
            else:
                #Recorremos comenzando por el acceso 
                actual = eColumna.acceso

                while actual.abajo != None:
                    #Si es menor debemos ingresarlo en esa posición, recordemos que es una lista ordenada
                    if nuevo.fila < actual.abajo.fila:
                        nuevo.abajo = actual.abajo
                        actual.abajo.arriba = nuevo
                        nuevo.arriba = actual
                        actual.abajo = nuevo
                        break
                    actual = actual.abajo
                
                # Si el ciclo termina y el actual.derecha = none quiere decir
                # que este nodo no tiene un posterior, este es el último porque nunca entró
                # al if, redordemos que al terminar de recorrer  y no entrar al if el actual es el último
                if actual.abajo == None:
                    actual.abajo = nuevo
                    nuevo.arriba = actual

    def recorrerFilas(self):
        #Nos colocamos en el primero
        eFila = self.Encabezado_Filas.primero
        print("\n****************** Recorrido por filas ******************")

        while eFila != None:

            actual = eFila.acceso
            print("\nFila "+str(actual.fila))
            print("Columna   Valor")
            while actual != None:
                print(str(actual.columna)+"         "+actual.valor)
                actual = actual.derecha
            
            eFila = eFila.siguiente        
        print("****************** Fin recorrido por filas ******************\n")


    def recorrerColumnas(self):
        eColumna = self.Encabezado_Columnas.primero
        print("\n****************** Recorrido por columnas ******************")

        while eColumna != None:

            actual = eColumna.acceso
            print("\nColumna "+str(actual.columna))
            print("Fila   Valor")
            while actual != None:
                print(str(actual.fila)+"      "+actual.valor)
                actual = actual.abajo
            
            eColumna = eColumna.siguiente            
        print("****************** Fin recorrido por columnas ******************\n")




