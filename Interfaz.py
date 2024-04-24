import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def inicio(ventana):
    
    ventana.title("Coodificacion Huffman");

    Ancho = ventana.winfo_screenwidth();
    Largo = ventana.winfo_screenheight();
    ventana.geometry(str(int(Ancho * 60 / 100))+ "x" + str(int(Largo * 60 / 100)))
    ventana.configure(bg = '#19191a')

    gris = tk.Frame(ventana, bg = '#19191a')

    boton = crearBoton(ventana, "Examinar", examinarArchivo);
    boton.grid(row = 0, column = 0);

    boton2 = crearBoton(ventana, "Comprimir");
    
    boton2.grid(row = 1, column = 0);

    boton3 = crearBoton(ventana, "Descomprimir");
    boton3.grid(row=2, column=0);
    
    boton2.grid(row = 1, column = 0);
    
    ventana.mainloop();

def proporcionAncho(X, Ventana):

    Ancho = Ventana.winfo_screenwidth(); #Brinda el ancho de la pantalla actual, a fin de calcular proporciones

    return int((Ancho * X)/100);

def proporcionLargo(X, Ventana):

    Largo = Ventana.winfo_screenheight(); #Brinda el largo de la pantalla actual, a fin de calcular proporciones

    return int((Largo * X)/100);

def crearBoton(ventana, texto, comando = None):

    boton = tk.Button(
        ventana, #Ventana pertenencia
        text = texto,
        background="#373739", #Fondo
        foreground="white", # Color de la letra
        font=("Helvetica", 12, "bold"),
        width = proporcionAncho(2, ventana), #Obtener Proporciones
        height = proporcionLargo(0.3, ventana), #Obtener Proporciones
        borderwidth=0,
        cursor = "hand2",
        relief = tk.RAISED,
        command = comando 
    )

    return boton

def examinarArchivo():
    # Abrir el explorador de archivos
    ruta_archivo = filedialog.askopenfilename()

    # Mostrar la ruta del archivo seleccionado
    if ruta_archivo:
        print("Ruta del archivo seleccionado:", ruta_archivo)
    else:
        print("No se seleccionó ningún archivo.")

ventana = tk.Tk();
inicio(ventana)
