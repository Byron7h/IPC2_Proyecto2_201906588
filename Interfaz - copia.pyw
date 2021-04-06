# https://docs.python.org/es/3/library/tkinter.html#tkinter-modules
# https://www.youtube.com/watch?v=Nn0AVbGVMhk
#  Para que no se abra la terminal al ejecutarla desde fuera, solo se cambia la extensión de py a pyw


# Vamos a usar Tkinter 

#(1) Importamos tkinter y todo lo que tiene su librería
from tkinter import *

# (2) Creamos nuestra raiz, nuestra "Ventana Principal" Tk de tkinter
#       el no 3 está hasta abajo, es importante verlo desde el inicio

root = Tk()

#(4) Le agregamos un título a nuestra root . title y le pasamos una cadena
root.title("Graficador a partir de matrices")

#(5) Podemos agregarle un icono, pero en esta ocación no lo vamos a hacer, 
# Podemos ver cómose hace ne el 2do link

#(6) Describir si podemos redimensionar o no la ventana, (ancho, alto) 0=Flase 1=true 
# Podemos colocar las palabras o los número que funciona igual
root.resizable(0,0)

#(7) Definir en ancho y alto, le enviamos una cadena
root.geometry("900x600")

#(8) Algunas configuraciones extras --> Usamos .config
#   •background color (bg="color") acepta el nombre en inglés o el hexa
root.config(bg="#202020") 


# (3) Ejecutamos el bucle infinito
#      Con esto le estamos diciendo que esté recibiendo de forma permanente
#      todo lo que esté arriba del mainloop, como python
#      es un lenguaje interpretado( que va linea por linea) debemos aclararle esto
#      para wue no se ejecute una sola vez  
#      Siempre va al final del doc, escuchando tododos los eventos hasta que se cierre
#      la ventana
root.mainloop()