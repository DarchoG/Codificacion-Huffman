import tkinter as tk
from tkinter import filedialog

def inicio(ventana):
    
    ventana.title("Coodificacion Huffman");

    #Obtiene la dimension de la pantalla del dispositivo en orden de adaptarse un poco a diferentes proporcones.

    Ancho = ventana.winfo_screenwidth();
    Largo = ventana.winfo_screenheight();
   
    #Valores predefinidos para el tamaño y color de fondo.

    anchoPorcentaje = 60
    largoPorcentaje = 40
    colorFondo = '#19191a'

    #Valores empleados para calcular en % de frames o widgets sobre el % total de la pantalal previamente definida.

    anchoVentana = int(Ancho * anchoPorcentaje / 100);
    largoVentana = int(Largo * largoPorcentaje / 100);

    #Atributos de la ventana.

    ventana.geometry(str(anchoVentana)+ "x" + str(largoVentana))
    ventana.configure(bg = colorFondo)

    #Frame que encapusula el cuadro de texto que muestra el archivo cargado.

    textoFrame = tk.Frame(ventana, width = proporcionAncho(100, ventana, anchoVentana), height = proporcionLargo(90, ventana, largoVentana), background="red")
    textoFrame.grid(row = 0, column = 0, sticky="nswe", padx=20, pady=10)
    textoFrame.grid_propagate(False) # Evita desbordarse del tamaño prestablecido.

    #Agregar una scrollbar de navegación.

    scrollbarx = tk.Scrollbar(textoFrame, orient=tk.HORIZONTAL)
    scrollbarx.pack(side=tk.BOTTOM, fill=tk.X)
    scrollbary = tk.Scrollbar(textoFrame, orient=tk.VERTICAL)
    scrollbary.pack(side=tk.RIGHT, fill=tk.Y)

    #Contenedor de texto del widget principal ################ Si es deseado alterar su contenido es requerido modificarlo con un insert ################

    contenidoPalabras = tk.Text(textoFrame, wrap="none", state="normal", padx=10, pady=10, xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)
    contenidoPalabras.pack(expand=True, fill=tk.BOTH)
    contenidoPalabras.insert(tk.END, "Texto Documento: ")
    contenidoPalabras.config(width=proporcionAncho(11.6, ventana, anchoVentana), height = proporcionLargo(3, ventana, largoVentana))

    #Creacion de los botones, al cumplir con las mismas caracteristicas se emplea una misma función, la diferencia radica en algunos parametros.
    
    botonesFrame = tk.Frame(ventana, width = proporcionAncho(100, ventana, anchoVentana), height = proporcionLargo(20, ventana, largoVentana), background='#19191a', pady = 45)
    botonesFrame.grid(row = 1, column = 0)

    boton = crearBoton(botonesFrame, "Examinar", lambda : examinarArchivo(contenidoPalabras));
    boton.grid(row = 0, column = 0,);

    boton2 = crearBoton(botonesFrame, "Comprimir", None); 
    boton2.grid(row = 0, column = 1, padx=20);
    
    #None es suceptible de ser remplazado por cualquier otro evento.
    #Es recomendado crear una funcion para eliminar el contenido previo del contendor y actualizarlo con la estrucutra de datos empleada para contar los caracteres. 
    #El contenedor esta diseñado para no colapsar con grandes contenidos de datos, es suceptible de ser probado con textos demasiado largos.

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

def examinarArchivo(texto): #Explora el archivo y retorna su direccion absoluta, puedes comprobarlo al mandar la direccion por consola.

    # Abrir el explorador de archivos
    rutaArchivo = filedialog.askopenfilename()
    
    if rutaArchivo: # Alterar el contenido del widget de texto
          
          with open(rutaArchivo, 'r') as archivo:

            contenido = archivo.read()
            texto.delete("1.0", tk.END)  # Limpiar el contenido anterior
            texto.insert(tk.END, contenido)

            print("Ruta del archivo seleccionado:", rutaArchivo)

    else:

        print("No se seleccionó ningún archivo.")

    return rutaArchivo 

ventana = tk.Tk();
inicio(ventana)
