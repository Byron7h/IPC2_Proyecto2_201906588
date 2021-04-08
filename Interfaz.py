# https://docs.python.org/es/3/library/tkinter.html#tkinter-modules
# https://www.youtube.com/watch?v=Nn0AVbGVMhk
# https://docs.hektorprofe.net/python/interfaces-graficas-con-tkinter/widget-label-etiqueta-de-texto/
# https://www.delftstack.com/es/howto/python-tkinter/how-to-create-dropdown-menu-in-tkinter/
# destroy https://www.youtube.com/watch?v=A6m7TmjuNzw
# Vamos a usar Tkinter 

#(1) Importamos tkinter y todo lo que tiene su librería
from tkinter import *

# (2) Creamos nuestra raiz, nuestra "Ventana Principal" Tk de tkinter
#       el no 3 está hasta abajo, es importante verlo desde el inicio


def destruir_widgets():
    for widget in fram.winfo_children():
        widget.destroy()

root = Tk()

#(4) Le agregamos un título a nuestra root . title y le pasamos una cadena
root.title("Graficador a partir de matrices")

#(5) Podemos agregarle un icono, pero en esta ocación no lo vamos a hacer, 
# Podemos ver cómose hace ne el 2do link

#(6) Describir si podemos redimensionar o no la ventana, (ancho, alto) 0=Flase 1=true 
# Podemos colocar las palabras o los número que funciona igual
root.resizable(0,0)

#(7) Definir en ancho y alto, le enviamos una cadena
root.geometry("1000x720")

#(8) Algunas configuraciones extras --> Usamos .config
#   •background color (bg="color") acepta el nombre en inglés o el hexa



#(9) Agregamos un frame, un contendedor, un marco
# Lo primero que hacemos es hacer que el frame sea un hijo de la raiz
frame = Frame(root)
#ahora vamos a empaquetar el frame dentro de la raiz, porque aún no lo agregamos, solo lo creamos
#le agregamos tamaño, porque si no solo es un puntito, le pasamos ints
frame.config(width=900, height=30)
frame.pack()




frame_botones_1 = Frame(root)
#ahora vamos a empaquetar el frame dentro de la raiz, porque aún no lo agregamos, solo lo creamos
frame_botones_1.config(bg="blue")
#le agregamos tamaño, porque si no solo es un puntito, le pasamos ints
frame_botones_1.config(width=800, height=40)
frame_botones_1.pack()


def boton_1():
    print("holi")

boton1= Button(master=frame_botones_1, text="Cargar Archivo", font=12, padx = 92, command=boton_1)
boton2= Button(master=frame_botones_1, text="Reportes" , font=12, padx = 92 , command=boton_1)
boton3= Button(master=frame_botones_1, text="Ayuda",font=12, padx = 92 , command=boton_1)
boton1.grid(row=0, column = 0)
boton2.grid(row=0, column = 1)
boton3.grid(row=0, column = 2)






frame_espace_1 = Frame(root)
#ahora vamos a empaquetar el frame dentro de la raiz, porque aún no lo agregamos, solo lo creamos
#le agregamos tamaño, porque si no solo es un puntito, le pasamos ints
frame_espace_1.config(width=900, height=30)
frame_espace_1.pack()






frame_botones_2 = Frame(root)
#ahora vamos a empaquetar el frame dentro de la raiz, porque aún no lo agregamos, solo lo creamos
frame_botones_2.config(bg="blue")
#le agregamos tamaño, porque si no solo es un puntito, le pasamos ints
frame_botones_2.config(width=800, height=40)
frame_botones_2.pack()


Etiqueta1 = Label(master=frame_botones_2 , text="Elige la operación a realizar", font=('Helvetica', 12))
Etiqueta1.grid(row=1, column =0)

Etiqueta2 = Label(master=frame_botones_2 , text="___________________________________________________________________", font=('Helvetica', 12))
Etiqueta2.grid(row=1, column =1)


OptionList = [
"1 Matriz - Rotación horizontal",
"1 Matriz - Rotación vertical",
"1 Matriz - Transpuesta",
"1 Matriz - Limpiar zona",
"1 Matriz - Agregar línea horizonta",
"1 Matriz - Agregar línea vertica",
"1 Matriz - Agregar rectángulo",
"1 Matriz - Agregar triángulo rectángulo"
] 
variable = StringVar(root)
variable.set("Elija la opción deseada")

opt = OptionMenu(root, variable, *OptionList)
opt.config(width=126)
opt.pack()




fram0 = Frame(root)
#ahora vamos a empaquetar el frame dentro de la raiz, porque aún no lo agregamos, solo lo creamos
fram0.config(bg="red")
#le agregamos tamaño, porque si no solo es un puntito, le pasamos ints
fram0.config(width=900, height=200)
fram0.pack()


Etiqueta1 = Label(master=fram0 , text="Rellene los parámetros", font=('Helvetica', 12))
Etiqueta1.grid(row=2, column =0)
Etiqueta2 = Label(master=fram0, text="_______________________________________________________________________", font=('Helvetica', 12))
Etiqueta2.grid(row=2, column =1)


framee = Frame(root)
#ahora vamos a empaquetar el frame dentro de la raiz, porque aún no lo agregamos, solo lo creamos
#le agregamos tamaño, porque si no solo es un puntito, le pasamos ints
framee.config(width=800, height=200)
framee.pack()

fram = Frame(framee)
fram.config(bg="red")
fram.config(width=800, height=200)
fram.pack()
        



def callback(*args):

    if str(variable.get()) == "1 Matriz - Rotación horizontal":
        destruir_widgets()
        Etiqueta1 = Label(master=fram , text="opcion1", font=(12))
        Etiqueta1.grid(row=3, column =0)
   
    elif str(variable.get()) == "1 Matriz - Rotación vertical":
        destruir_widgets()
        Etiqueta1 = Label(master=fram , text="opcion2", font=(12))
        Etiqueta1.grid(row=3, column =0)

    elif str(variable.get()) == "1 Matriz - Transpuesta":
        destruir_widgets()
        Etiqueta1 = Label(master=fram , text="opcion3", font=(12))
        Etiqueta1.grid(row=3, column =0)


variable.trace("w", callback)





frame_espace_2 = Frame(root)
#ahora vamos a empaquetar el frame dentro de la raiz, porque aún no lo agregamos, solo lo creamos
frame_espace_2.config(bg="red")
#le agregamos tamaño, porque si no solo es un puntito, le pasamos ints
frame_espace_2.config(width=900, height=30)
frame_espace_2.pack()


frame_graficas = Frame(root)
#ahora vamos a empaquetar el frame dentro de la raiz, porque aún no lo agregamos, solo lo creamos
frame_graficas.config(bg="green")
#le agregamos tamaño, porque si no solo es un puntito, le pasamos ints
frame_graficas.config(width=800, height=400)
frame_graficas.pack()










# (3) Ejecutamos el bucle infinito
#      Con esto le estamos diciendo que esté recibiendo de forma permanente
#      todo lo que esté arriba del mainloop, como python
#      es un lenguaje interpretado( que va linea por linea) debemos aclararle esto
#      para wue no se ejecute una sola vez  
#      Siempre va al final del doc, escuchando tododos los eventos hasta que se cierre
#      la ventana
root.mainloop()