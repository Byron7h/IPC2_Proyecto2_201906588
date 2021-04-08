if __name__ == '__main__':

    import xml.etree.ElementTree as ET
    import numpy as np

    from errores import Error
    from Pila import Pila
    from datetime import datetime
    now = datetime.now()


    matrices=[]
    errores=[]

    def Read_File():
        print("Ingrese la dirección del archivo que desea leer")
        ruta = str(input())
        archivo_valido = True
        print("Buscando archivo...") 
        try:
            archivo_xml = ET.parse(ruta)
            print("Leyendo archivo...")
        except:
            archivo_valido = False
            

        if archivo_valido:
            # Vamos a llenar de en un bloque los datos de nombre, filas, columnas y
            # matriz_llena (matriz con los datos originales) haciendo la verificación
            # por nombre primero, y luego por número de filas, si ambas se pasan se
            # crea un objeto de tipo Nodo_info Y luego se agrega a la lista circular

            #Obtenemos raiz del xml, ese nos permitirá ubicarnos y obtener la info
            # del xml 
            raiz=archivo_xml.getroot()
            
            nombre = None
            filas = None
            columnas = None
            imagen = None
            numero = 1
            for elemento in raiz:
                for subelemento in elemento:
                    if str(subelemento.tag) == "nombre" :
                        nombre = str(subelemento.text)

                    elif str(subelemento.tag) == "filas":
                        filas = int(subelemento.text)

                    elif str(subelemento.tag) == "columnas":

                        columnas = int(subelemento.text)

                    elif str(subelemento.tag) == "imagen":
                        imagen = str(subelemento.text)

                numero = numero + 1


                # Primera validación, existencia de todos los datos
                if nombre != None and filas != None and columnas != None and imagen != None:
                
                # Segunda validacion, Nombre ya registrado
                    matriz_existe = False
                    if len(matrices) != 0:
                        for i in range(len(matrices)):
                            if nombre == matrices[i].getNombre():
                                matriz_existe = True           
                                break
                
                    if matriz_existe:
                        fecha_hora = str(now.date()) + " - " + str(now.hour) + "." + str(now.minute) + "." + str(now.second)
                        descripcion = "Error en la matriz No." + str(numero)+ " El nombre" + str(nombre) + " ya se encuentra registrado"
                        nuevo = Error(fecha_hora, descripcion)
                        errores.append(nuevo)
        
                    else:
                        # Tercera validación, numero de filas y columnas
                        matriz_madre=np.zeros((int(filas),int(columnas)))
                        matriz_madre[:][:]=-1
                        nueva_pila = Pila()
                        f = 0
                        c = 0
                        pos = 0

                        imagen = imagen.strip()

                        while (pos < len(imagen)):
                            char = imagen[pos] # El caracter en la posición actual, lo pasamos a char por cualquier cosa
                            char_code = ord(imagen[pos])

                            if char_code == 42: #*
                                nueva_pila.add(char)

                            elif char_code == 45: #-
                                nueva_pila.add(char)
                            pos= pos + 1
                        print(len(nueva_pila))
                       

                        try:  
                            pos=0
                            while (pos < len(imagen)):
                                char = imagen[pos] # El caracter en la posición actual, lo pasamos a char por cualquier cosa
                                char_code = ord(imagen[pos])
                                if char_code == 45: #-
                                    matriz_madre[f][c] = 0
                                    nueva_pila.remove()
                                    c = c + 1
                                if char_code == 42: #*
                                    matriz_madre[f][c] = 1
                                    nueva_pila.remove()
                                    c = c + 1
                                elif char_code == 10: #Salto de línea
                                    c = 0
                                    f = f + 1
                                pos= pos + 1
                        except:
                            pass

                        print(matriz_madre)









                else:
                    if nombre == None:
                        nombre = "número " + str(numero)
                    fecha_hora = str(now.date()) + " - " + str(now.hour) + "." + str(now.minute) + "." + str(now.second)
                    descripcion = "Falta de datos en matriz " + str(nombre)
                    nuevo = Error(fecha_hora, descripcion)
                    errores.append(nuevo)
        else:
            print('No se pudo abrir el xml')

Read_File()
for error in errores:
    print(error.getDescripcion())
    print(error.getFecha_hora())