import tkinter as tk
from tkinter import ttk

def inicio(ventana):
    
    ventana.title("Coodificacion Huffman");

    Ancho = ventana.winfo_screenwidth();
    Largo = ventana.winfo_screenheight();
    ventana.geometry(str(int(Ancho * 60 / 100))+ "x" + str(int(Largo * 60 / 100)))
    ventana.configure(bg = '#19191a')

    gris = tk.Frame(ventana, bg = '#19191a')
    ventana.mainloop();


ventana = tk.Tk();
inicio(ventana)
