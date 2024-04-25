import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def inicio(ventana):
    
    ventana.title("Coodificacion Huffman");

    Ancho = ventana.winfo_screenwidth();
    Largo = ventana.winfo_screenheight();
   
    anchoPorcentaje = 60
    largoPorcentaje = 60

    anchoVentana = int(Ancho * anchoPorcentaje / 100);
    largoVentana = int(Largo * largoPorcentaje / 100);

    ventana.geometry(str(anchoVentana)+ "x" + str(largoVentana))
    ventana.configure(bg = '#19191a')

    textoFrame = tk.Frame(ventana, width = proporcionAncho(50, ventana, anchoVentana), height = proporcionLargo(70, ventana, largoVentana), background="red")
    textoFrame.grid(row = 0, column = 0, sticky="nswe")

    contenidoPalabras = tk.Text(textoFrame, wrap="word", state="disabled")
    contenidoPalabras.grid(row=0, column=0, sticky="nswe")
    contenidoPalabras.grid_rowconfigure(0, weight=1)  # Hacer que la fila se expanda
    contenidoPalabras.grid_columnconfigure(0, weight=1)

    scrollbar = tk.Scrollbar(ventana, command=contenidoPalabras.yview)
    scrollbar.grid(row=0, column=1, sticky='ns')
    contenidoPalabras.config(yscrollcommand=scrollbar.set)

    graficaFrame = tk.Frame(ventana, width = proporcionAncho(50, ventana, anchoVentana), height = proporcionLargo(70, ventana, largoVentana), background="blue")
    graficaFrame.grid(row = 0, column = 1,)

    botonesFrame = tk.Frame(ventana, width = proporcionAncho(100, ventana, anchoVentana), height = proporcionLargo(20, ventana, largoVentana), background='#19191a', pady = 45)
    botonesFrame.grid(row = 1, column = 0, columnspan= 2)

    boton = crearBoton(botonesFrame, "Examinar", examinarArchivo);
    boton.grid(row = 0, column = 0,);

    boton2 = crearBoton(botonesFrame, "Comprimir", None); #None es suceptible de ser remplazado por cualquier otro evento.
    boton2.grid(row = 0, column = 1, padx=20);

    boton3 = crearBoton(botonesFrame, "Descomprimir", None); #None es susceptible de ser remplazado por cualquier otro evento.
    boton3.grid(row=0, column=2);

    ventana.mainloop();

def proporcionAncho(X, Ventana, Ancho = None):

    if(Ancho is None):

        Ancho = Ventana.winfo_screenwidth(); #Brinda el ancho de la pantalla actual, a fin de calcular proporciones
        return int((Ancho * X)/100);

    return int((Ancho * X)/100);

def proporcionLargo(X, Ventana, Largo = None):

    if(Largo is None):

        Largo = Ventana.winfo_screenheight(); #Brinda el largo de la pantalla actual, a fin de calcular proporciones
        return int((Largo * X)/100);

    return int((Largo * X)/100);

def crearBoton(ventana, texto, comando = None):

    boton = tk.Button(
        ventana, #Ventana  o frame de pertenencia
        text = texto,
        background="#373739", #Fondo
        foreground="white", # Color de la letra
        font=("Helvetica", 12, "bold"),
        width = proporcionAncho(1.5, ventana), #Obtener Proporciones
        height = proporcionLargo(0.3, ventana), #Obtener Proporciones
        borderwidth=1,
        cursor = "hand2",
        relief = tk.RAISED,
        command = comando 
    )

    return boton

def examinarArchivo():
    # Abrir el explorador de archivos
    rutaArchivo = filedialog.askopenfilename()
    
    if rutaArchivo:
        print("Ruta del archivo seleccionado:", rutaArchivo)
    else:
        print("No se seleccionó ningún archivo.")

    return rutaArchivo    

ventana = tk.Tk();
inicio(ventana)
