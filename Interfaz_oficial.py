from tkinter import *


def destruir_widgets():
    for widget in frame_op3.winfo_children():
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
boton1= Button(master=frame_botones_1, text="Cargar Archivo", font=12, padx = 92, command=boton_1)
boton2= Button(master=frame_botones_1, text="Reportes" , font=12, padx = 92 , command=boton_1)
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
    if str(variable.get()) == "1 Matriz - Rotación horizontal" or str(variable.get()) == "1 Matriz - Rotación vertical" or str(variable.get()) == "1 Matriz - Transpuesta":
        destruir_widgets()
        Etiqueta1 = Label(master=frame_op3 , text="Nombre", font=12)
        Etiqueta1.grid(row=2, column =0)
        #Entrada de texto
        entrada_nombre= Entry(frame_op3)
        entrada_nombre.grid(row=2,column=1, padx=5, pady=5)
        

    elif str(variable.get()) == "1 Matriz - Limpiar zona":
        destruir_widgets()
        Etiqueta1 = Label(master=frame_op3 , text="Nombre", font=12)
        Etiqueta1.grid(row=2, column =0)
        #Entrada de texto
        entrada_nombre= Entry(frame_op3)
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

    elif str(variable.get()) == "1 Matriz - Agregar línea horizontal" or str(variable.get()) == "1 Matriz - Agregar línea vertical" :
        destruir_widgets()
        Etiqueta1 = Label(master=frame_op3 , text="Nombre", font=12)
        Etiqueta1.grid(row=2, column =0)
        #Entrada de texto
        entrada_nombre= Entry(frame_op3)
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

    elif str(variable.get()) == "1 Matriz - Agregar rectángulo" or str(variable.get()) == "1 Matriz - Agregar triángulo rectángulo":
        destruir_widgets()
        Etiqueta1 = Label(master=frame_op3 , text="Nombre", font=12)
        Etiqueta1.grid(row=2, column =0)
        #Entrada de texto
        entrada_nombre= Entry(frame_op3)
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
        pass

variable.trace("w", callback)





root.mainloop()