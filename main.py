if __name__ == '__main__':

    import xml.etree.ElementTree as ET
    import numpy as np
    import webbrowser
    from tkinter import *
    from tkinter import filedialog
    from tkinter import messagebox

    from errores import Error
    from Pila import Pila
    from matriz_original import Matriz_Original
    from matriz import Matriz
    from nodos import Nodo_Encabezado, Nodo_Interno
    from encabezado import Lista_encabezado
    from operacion import Operacion

    from PIL import Image
    from datetime import datetime
    now = datetime.now()

    matrices=[]
    errores=[]
    operaciones=[]
    

    def crear_imagen(matriz_madre ,filas , columnas, nombre):
        lista_1 =[]
        lista_2 =[]
        for n in range(int(filas)):
            for m in range(int(columnas)):
                if matriz_madre[n][m] == 1:
                    for a in range(25):
                        lista_1.append([39, 39, 39])
                
                if matriz_madre[n][m] == 0:
                    for a in range(25): 
                        lista_1.append([224, 224, 224])
            for a in range(25):            
                lista_2.append(lista_1)
            lista_1 =[]

        np_array = np.array(lista_2)  
        image = Image.fromarray(np_array.astype('uint8'), 'RGB')
        image.save(str(nombre))

    def Read_File(ruta):
        archivo_valido = True 
        try:
            archivo_xml = ET.parse(ruta)
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
            
            numero = 1
            for elemento in raiz:
                nombre = None
                filas = None
                columnas = None
                imagen = None
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
                        descripcion = "Error en la matriz No." + str(numero)+ " El nombre " + str(nombre) + " ya se encuentra registrado"
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

                        llenos = 0
                        vacios= 0
                        while (pos < len(imagen)):
                            char = imagen[pos] # El caracter en la posición actual, lo pasamos a char por cualquier cosa
                            char_code = ord(imagen[pos])
                            if char_code == 42: #*
                                llenos = llenos + 1
                                nueva_pila.add(char)
                            elif char_code == 45: #-
                                vacios = vacios + 1
                                nueva_pila.add(char)
                            pos= pos + 1
                    
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
                        sin_posiciones_vacias = True
                        for n in range(int(filas)):
                            for m in range(int(columnas)):
                                if matriz_madre[n][m] == -1:
                                    #print("se encontró un acasilla vacía")
                                    sin_posiciones_vacias = False
                                    break                       
                        if (len(nueva_pila) == 0 and sin_posiciones_vacias ):
                        #Acá cumplió todas las validaciones                        
                            # Creando matriz ortogonal:
                            matriz_ortogonal = Matriz()
                            for n in range(int(filas)):
                                for m in range(int(columnas)):
                                    if matriz_madre[n][m] == 1:

                                        #parametros fila, columna, valor
                                        matriz_ortogonal.Insertar(n, m, "*")
                            print(nombre)
                            matriz_ortogonal.recorrerFilas()

                            #Creando el objeto
                            fecha_hora = str(now.date()) + " - " + str(now.hour) + "." + str(now.minute) + "." + str(now.second)
                            nueva = Matriz_Original(nombre, filas, columnas, matriz_ortogonal, vacios, llenos, fecha_hora)
                            #Agregando a la lista
                            matrices.append(nueva)
                        

                        else:
                            fecha_hora = str(now.date()) + " - " + str(now.hour) + "." + str(now.minute) + "." + str(now.second)
                            descripcion = "La matriz " + str(nombre) +" tiene dimensiones incorrectas"
                            nuevo = Error(fecha_hora, descripcion)
                            errores.append(nuevo)

                else:
                    if nombre == None:
                        nombre = "número " + str(numero)
                    fecha_hora = str(now.date()) + " - " + str(now.hour) + "." + str(now.minute) + "." + str(now.second)
                    descripcion = "Falta de datos en matriz " + str(nombre)
                    nuevo = Error(fecha_hora, descripcion)
                    errores.append(nuevo)

            if len(errores)>0:        
                Alerta_tkinter('El archivo leido contiene errores, puede verlos en el área de reportes')
            else:
                Alerta_tkinter('El archivo fue leido sin errores')
        
        else:
            Alerta_tkinter('No se pudo abrir el xml')

    def Alerta_tkinter(mensaje):
        messagebox.showinfo(message= mensaje , title="Alerta")

    def Documento():

        f = open('Reporte.html','w')

        mensaje = """
        <link href="estilo.css" rel="stylesheet">
        """
        f.write(mensaje)

        if len(matrices)>0:
            f.write("""<h1>Matrices Registradas</h1>\n""")
            for n in range(len(matrices)):
                string = str(matrices[n].getFecha_hora()) + "   -   Nombre: " + str(matrices[n].getNombre()) + "   -   Espacios llenos: " + str(matrices[n].getLlenos())  + "   -   Espacios vacios: " + str(matrices[n].getVacios())
            
                f.write("""<div class="cols-3">\n""")
                f.write("""  <div class="cols-span-3">\n""")
                f.write("""    <div class="box">""")
                f.write("Contenido:")
                f.write(string)
                f.write("""</div>\n""")
                f.write("""  </div>\n""")
                f.write("""</div>\n""")


        if len(errores)>0:
            f.write("""<h1>Errores Registrados</h1>\n""")
            for n in range(len(errores)):
                string = str(errores[n].getFecha_hora()) + "   -   Descripción: " + str(errores[n].getDescripcion())
            
                f.write("""<div class="cols-3">\n""")
                f.write("""  <div class="cols-span-3">\n""")
                f.write("""    <div class="box">""")
                f.write("Contenido:")
                f.write(string)
                f.write("""</div>\n""")
                f.write("""  </div>\n""")
                f.write("""</div>\n""")

        f.close()
        webbrowser.open_new('Reporte.html')

    def interfaz():

        def cambio( img_antes, img_despues):

            img_antes_now = PhotoImage(file="antes.png")
            ima.configure(image=img_antes_now)
            ima.image = img_antes_now

            img_despues_now = PhotoImage(file="despues.png")
            iman.configure(image=img_despues_now)
            iman.image = img_despues_now

        def hecho(nueva_OP):
            # analizando que no vengan vacios
            contiene_vacios = False
            for clave in nueva_OP:
                if nueva_OP[clave] == "":
                    contiene_vacios = True
            if contiene_vacios:
                Alerta_tkinter("Existen campos sin llenar")
            else:

                # Viendo si la matriz existe
                matriz_existe = False
                for w in range(len(matrices)):
                    if matrices[w].getNombre() == nueva_OP['nombre_matriz']:
                        matriz_existe = True
                        break
                if matriz_existe:

                #Operaciones
                    if str(nueva_OP['operacion']) == "1 Matriz - Rotación horizontal":
                        
                        matriz_ortogonal = matrices[w].getmatriz_ortogonal()
                        filas = matrices[w].getFilas()
                        columnas = matrices[w].getColumnas()
                        matriz_madre=np.zeros((int(filas),int(columnas)))

                        #Extraemos los datos de la matriz ortogonal
                        eFila = matriz_ortogonal.Encabezado_Filas.primero
                        while eFila != None:
                            actual = eFila.acceso
                            while actual != None:
                                matriz_madre[actual.fila][actual.columna]=1
                                actual = actual.derecha           
                            eFila = eFila.siguiente        

                        print(matriz_madre)

                        # Hacemos el cambio
                        matriz_producto=np.zeros((int(filas),int(columnas)))

                        for n in range(int(filas)):
                            for m in range(int(columnas)):
                                if matriz_madre[n][m]==1:
                                    matriz_producto[n][int(columnas)-1-m]=1
                        print(matriz_producto)

                        img_antes = crear_imagen(matriz_madre ,int(filas) , int(columnas),"antes.png")
                        img_despues = crear_imagen(matriz_producto ,int(filas) , int(columnas), "despues.png")

                        cambio( img_antes, img_despues)


                    elif str(nueva_OP['operacion']) == "1 Matriz - Rotación vertical":
                        
                        matriz_ortogonal = matrices[w].getmatriz_ortogonal()
                        filas = matrices[w].getFilas()
                        columnas = matrices[w].getColumnas()
                        matriz_madre=np.zeros((int(filas),int(columnas)))

                        #Extraemos los datos de la matriz ortogonal
                        eFila = matriz_ortogonal.Encabezado_Filas.primero
                        while eFila != None:
                            actual = eFila.acceso
                            while actual != None:
                                matriz_madre[actual.fila][actual.columna]=1
                                actual = actual.derecha           
                            eFila = eFila.siguiente        

                        print(matriz_madre)

                        # Hacemos el cambio
                        matriz_producto=np.zeros((int(filas),int(columnas)))

                        for n in range(int(filas)):
                            for m in range(int(columnas)):
                                if matriz_madre[n][m]==1:
                                    matriz_producto[int(filas)-1-n][m]=1
                        print(matriz_producto)

                        img_antes = crear_imagen(matriz_madre ,int(filas) , int(columnas),"antes.png")
                        img_despues = crear_imagen(matriz_producto ,int(filas) , int(columnas), "despues.png")

                        cambio( img_antes, img_despues)


                        
                    elif str(nueva_OP['operacion']) == "1 Matriz - Transpuesta":
                        
                        matriz_ortogonal = matrices[w].getmatriz_ortogonal()
                        filas = matrices[w].getFilas()
                        columnas = matrices[w].getColumnas()
                        matriz_madre=np.zeros((int(filas),int(columnas)))

                        #Extraemos los datos de la matriz ortogonal
                        eFila = matriz_ortogonal.Encabezado_Filas.primero
                        while eFila != None:
                            actual = eFila.acceso
                            while actual != None:
                                matriz_madre[actual.fila][actual.columna]=1
                                actual = actual.derecha           
                            eFila = eFila.siguiente        

                        print(matriz_madre)

                        # Hacemos el cambio
                        matriz_producto=np.zeros((int(filas),int(columnas)))

                        for n in range(int(filas)):
                            for m in range(int(columnas)):
                                if matriz_madre[n][m]==1:
                                    matriz_producto[m][n]=1
                        print(matriz_producto)

                        img_antes = crear_imagen(matriz_madre ,int(filas) , int(columnas),"antes.png")
                        img_despues = crear_imagen(matriz_producto ,int(filas) , int(columnas), "despues.png")

                        cambio( img_antes, img_despues)


                    elif str(nueva_OP['operacion']) == "1 Matriz - Limpiar zona":
                        

                        XO = int(nueva_OP['XO']) -1
                        YO = int(nueva_OP['YO']) -1
                        XF = int(nueva_OP['XF']) -1
                        YF = int(nueva_OP['YF']) -1


                        matriz_ortogonal = matrices[w].getmatriz_ortogonal()
                        filas = matrices[w].getFilas()
                        columnas = matrices[w].getColumnas()
                        matriz_madre=np.zeros((int(filas),int(columnas)))

                        #Extraemos los datos de la matriz ortogonal
                        eFila = matriz_ortogonal.Encabezado_Filas.primero
                        while eFila != None:
                            actual = eFila.acceso
                            while actual != None:
                                matriz_madre[actual.fila][actual.columna]=1
                                actual = actual.derecha           
                            eFila = eFila.siguiente        

                        print(matriz_madre)

                        # Hacemos el cambio
                        matriz_producto=np.zeros((int(filas),int(columnas)))

                        for n in range(int(filas)):
                            for m in range(int(columnas)):
                                if matriz_madre[n][m]==1:
                                    if m >= XO and m <= XF and n >= YO and n <= YF:
                                        pass
                                    else:
                                        matriz_producto[n][m]=1
                                    
                        print(matriz_producto)

                        img_antes = crear_imagen(matriz_madre ,int(filas) , int(columnas),"antes.png")
                        img_despues = crear_imagen(matriz_producto ,int(filas) , int(columnas), "despues.png")

                        cambio( img_antes, img_despues)



                else:
                    Alerta_tkinter("No se encontró la matriz")
                
        def operaciones():

            img = PhotoImage(file="tutor de programacion.gif")
            can = Canvas(win)
            can.pack(fill=BOTH)
            can.create_image(20, 20, image=img, anchor=NW)



            frame_imagenes

            if str(variable.get()) == "1 Matriz - Rotación horizontal":
                destruir_widgets()

            elif str(variable.get()) == "1 Matriz - Rotación vertical" :
                destruir_widgets()

            elif str(variable.get()) == "1 Matriz - Transpuesta":
                destruir_widgets()

            elif str(variable.get()) == "1 Matriz - Limpiar zona":
                destruir_widgets()

            elif str(variable.get()) == "1 Matriz - Agregar línea horizontal" :
                destruir_widgets()

            elif str(variable.get()) == "1 Matriz - Agregar línea vertical" :
                destruir_widgets()

            elif str(variable.get()) == "1 Matriz - Agregar rectángulo" :
                destruir_widgets()

            elif str(variable.get()) == "1 Matriz - Agregar triángulo rectángulo":
                destruir_widgets()
            
        def selector_archivos():
            archivo_valido = True 
            try:
                nombre_archivo =  filedialog.askopenfilename(title = "Select file")
                Read_File(nombre_archivo)
            except:
                pass

        def destruir_widgets():
            for widget in frame_op3.winfo_children():
                widget.destroy()

        def imagenes():
            
            def callback(e):
                img_antes_now = PhotoImage(file="image.png")
                ima.configure(image=img_antes_now)
                ima.image = img_antes_now

            root.bind("<Return>", callback)

        def destruir_widgets2():
            for widget in frame_imagenes.winfo_children():
                widget.destroy()

        def boton_1():
            print("holi")

        root = Tk()
        root.title("Graficador a partir de matrices")
        root.resizable(0,0)
        root.geometry("1000x720")

        #espacio_1
        frame = Frame(root)
        frame.config(width=900, height=30)
        frame.pack()

        #Frame para botones principales
        frame_botones_1 = Frame(root)
        frame_botones_1.config(width=800, height=40)
        frame_botones_1.pack()

        #Botones Principales
        boton1= Button(master=frame_botones_1, text="Cargar Archivo", font=12, padx = 92, command=selector_archivos)
        boton2= Button(master=frame_botones_1, text="Reportes" , font=12, padx = 92 , command= Documento )
        boton3= Button(master=frame_botones_1, text="Ayuda",font=12, padx = 92 , command=boton_1)
        boton1.grid(row=0, column = 0)
        boton2.grid(row=0, column = 1,padx=5, pady=5)
        boton3.grid(row=0, column = 2)

        #espacio_2
        frame2 = Frame(root)
        frame2.config(width=900, height=50)
        frame2.pack()

        #frame operaciones1
        frame_op1= Frame(root)
        frame_op1.config(width=800, height=5)
        frame_op1.pack()

        #Contenido operaciones1
        Etiqueta1 = Label(master=frame_op1 , text="Elige la operación a realizar", font=('Helvetica', 12))
        Etiqueta1.grid(row=1, column =0)
        Etiqueta2 = Label(master=frame_op1 , text="___________________________________________________________________", font=('Helvetica', 12))
        Etiqueta2.grid(row=1, column =1)

        #frame operaciones2
        frame_op2= Frame(root)
        frame_op2.config(width=800, height=20)
        frame_op2.pack()

        #Contenido operaciones2
        OptionList = [
        "1 Matriz - Rotación horizontal",
        "1 Matriz - Rotación vertical",
        "1 Matriz - Transpuesta",
        "1 Matriz - Limpiar zona",
        "1 Matriz - Agregar línea horizontal",
        "1 Matriz - Agregar línea vertical",
        "1 Matriz - Agregar rectángulo",
        "1 Matriz - Agregar triángulo rectángulo"
        ] 
        variable = StringVar(root)
        variable.set("Elija la opción deseada")

        opt = OptionMenu(root, variable, *OptionList)
        opt.config(width=126)
        opt.pack()

        #espacio_2
        frame2 = Frame(root)
        frame2.config(width=900, height=20)
        frame2.pack()

        #Frame operacion escogida
        frame_op3= Frame(root)
        frame_op3.config(width=800, height=200)
        frame_op3.pack()

        # elementos de la operacion escogida
        def callback(*args):
            name = ""
            if str(variable.get()) == "1 Matriz - Rotación horizontal" or str(variable.get()) == "1 Matriz - Rotación vertical" or str(variable.get()) == "1 Matriz - Transpuesta":
                destruir_widgets()
                Etiqueta1 = Label(master=frame_op3 , text="Nombre", font=12)
                Etiqueta1.grid(row=2, column =0)
                #Entrada de texto
                entrada_nombre= Entry(frame_op3, textvariable= name)
                entrada_nombre.grid(row=2,column=1, padx=5, pady=5)
              
                boton_hecho= Button(master=frame_op3, text="Hecho", font=12, padx = 92, command=lambda:hecho( {'operacion' : str(variable.get()), 'nombre_matriz' : str(entrada_nombre.get())}))
                boton_hecho.grid(row=5,column=3, padx=5, pady=15)


            elif str(variable.get()) == "1 Matriz - Limpiar zona":
                destruir_widgets()
                Etiqueta1 = Label(master=frame_op3 , text="Nombre", font=12)
                Etiqueta1.grid(row=2, column =0)
                #Entrada de texto
                entrada_nombre= Entry(frame_op3, textvariable= name)
                entrada_nombre.grid(row=2,column=1, padx=5, pady=5)

                Etiqueta2 = Label(master=frame_op3 , text="Coordena Inicial  •x", font=12)
                Etiqueta2.grid(row=3, column =0)

                #Entrada de texto
                entrada_XO= Entry(frame_op3)
                entrada_XO.grid(row=3,column=1, padx=5, pady=5)

                Etiqueta2_1 = Label(master=frame_op3 , text="•y", font=12)
                Etiqueta2_1.grid(row=3, column =2)

                #Entrada de texto
                entrada_YO= Entry(frame_op3)
                entrada_YO.grid(row=3,column=3, padx=5, pady=5)

                Etiqueta3 = Label(master=frame_op3 , text="Coordena Final   •x", font=12)
                Etiqueta3.grid(row=4, column =0)

                #Entrada de texto
                entrada_XF= Entry(frame_op3)
                entrada_XF.grid(row=4,column=1, padx=5, pady=5)

                Etiqueta3_1 = Label(master=frame_op3 , text="•y", font=12)
                Etiqueta3_1.grid(row=4, column =2)

                #Entrada de texto
                entrada_YF= Entry(frame_op3)
                entrada_YF.grid(row=4,column=3, padx=5, pady=5)

                boton_hecho= Button(master=frame_op3, text="Hecho", font=12, padx = 92, command=lambda:hecho( {'operacion' : str(variable.get()), 'nombre_matriz' : str(entrada_nombre.get()), 'XO' : str(entrada_XO.get()), 'YO' : str(entrada_YO.get()),'XF' : str(entrada_XF.get()), 'YF' : str(entrada_YF.get())}))
                boton_hecho.grid(row=5,column=3, padx=5, pady=15)



            elif str(variable.get()) == "1 Matriz - Agregar línea horizontal" or str(variable.get()) == "1 Matriz - Agregar línea vertical" :
                destruir_widgets()
                Etiqueta1 = Label(master=frame_op3 , text="Nombre", font=12)
                Etiqueta1.grid(row=2, column =0)
                #Entrada de texto
                entrada_nombre= Entry(frame_op3, textvariable= name)
                entrada_nombre.grid(row=2,column=1, padx=5, pady=5)

                Etiqueta2 = Label(master=frame_op3 , text="Coordena Inicial  •x", font=12)
                Etiqueta2.grid(row=3, column =0)

                #Entrada de texto
                entrada_XO= Entry(frame_op3)
                entrada_XO.grid(row=3,column=1, padx=5, pady=5)

                Etiqueta2_1 = Label(master=frame_op3 , text="•y", font=12)
                Etiqueta2_1.grid(row=3, column =2)

                #Entrada de texto
                entrada_YO= Entry(frame_op3)
                entrada_YO.grid(row=3,column=3, padx=5, pady=5)

                Etiqueta3 = Label(master=frame_op3 , text="Cantidad", font=12)
                Etiqueta3.grid(row=4, column =0)

                #Entrada de texto
                cantidad= Entry(frame_op3)
                cantidad.grid(row=4,column=1, padx=5, pady=5)

                boton_hecho= Button(master=frame_op3, text="Hecho", font=12, padx = 92, command=lambda:hecho( {'operacion' : str(variable.get()), 'nombre_matriz' : str(entrada_nombre.get()), 'XO' : str(entrada_XO.get()), 'YO' : str(entrada_YO.get()),'cantidad' : str(cantidad.get())}))
                boton_hecho.grid(row=5,column=3, padx=5, pady=15)


            elif str(variable.get()) == "1 Matriz - Agregar rectángulo" or str(variable.get()) == "1 Matriz - Agregar triángulo rectángulo":
                destruir_widgets()
                Etiqueta1 = Label(master=frame_op3 , text="Nombre", font=12)
                Etiqueta1.grid(row=2, column =0)
                #Entrada de texto
                entrada_nombre= Entry(frame_op3, textvariable= name)
                entrada_nombre.grid(row=2,column=1, padx=5, pady=5)

                Etiqueta2 = Label(master=frame_op3 , text="Coordena Inicial  •x", font=12)
                Etiqueta2.grid(row=3, column =0)

                #Entrada de texto
                entrada_XO= Entry(frame_op3)
                entrada_XO.grid(row=3,column=1, padx=5, pady=5)

                Etiqueta2_1 = Label(master=frame_op3 , text="•y", font=12)
                Etiqueta2_1.grid(row=3, column =2)

                #Entrada de texto
                entrada_YO= Entry(frame_op3)
                entrada_YO.grid(row=3,column=3, padx=5, pady=5)

                Etiqueta3 = Label(master=frame_op3 , text="Filas", font=12)
                Etiqueta3.grid(row=4, column =0)

                #Entrada de texto
                filas= Entry(frame_op3)
                filas.grid(row=4,column=1, padx=5, pady=5)

                Etiqueta3_1 = Label(master=frame_op3 , text="Columnas", font=12)
                Etiqueta3_1.grid(row=4, column =2)

                #Entrada de texto
                columnas= Entry(frame_op3)
                columnas.grid(row=4,column=3, padx=5, pady=5)

                boton_hecho= Button(master=frame_op3, text="Hecho", font=12, padx = 92, command=lambda:hecho( {'operacion' : str(variable.get()), 'nombre_matriz' : str(entrada_nombre.get()), 'XO' : str(entrada_XO.get()), 'YO' : str(entrada_YO.get()),'filas' : str(filas.get()), 'columnas' : str(columnas.get())}))
                boton_hecho.grid(row=5,column=3, padx=5, pady=15)


        frame_imagenes= Frame(root)
        frame_imagenes.config(width=800, height=600 , bg= "blue")
        frame_imagenes.pack()

        img_antes = PhotoImage(file="original.png")
        img_despues = PhotoImage(file="original.png")
        
        ima=Label(frame_imagenes, image=img_antes, bd=0)
        ima.grid(row=6,column=1, padx=5, pady=15)

        iman=Label(frame_imagenes, image=img_despues, bd=0)
        iman.grid(row=6,column=3, padx=5, pady=15)



        variable.trace("w", callback)
        root.mainloop()
interfaz()