import tkinter as tk
from tkinter import filedialog
import Huffman

def examinar():

    global Direccion

    archivo_path = filedialog.askopenfilename(filetypes=[("Archivo de texto", "*.txt")])
    if archivo_path:
        frecuencia = caracteresRepeticiones(archivo_path)
        for char, count in frecuencia.items():
            txt_lista.insert(tk.END, f"{char}: {count}\n")

    caracteresRepeticiones(archivo_path) 

    Direccion = archivo_path

def caracteresRepeticiones(archivo):
    repeticiones = {}
    with open(archivo, 'r', encoding='utf-8') as file:
        texto = file.read()
        for car in texto:
            repeticiones[car] = repeticiones.get(car, 0) + 1
    #ordenar el diccionario de mayor a menor (cantidad de repeticiones)
    repeticiones_ordenadas = dict(sorted(repeticiones.items(), key=lambda x: x[1], reverse=True))
    return repeticiones_ordenadas

def comprimir(Direccion):

    Huffman.comprimir(Direccion)

def descomprimir():

    Huffman.descomprimir()

global Direccion

#ventana
ventana = tk.Tk()
ventana.title("Actividad 7 - Huffman")
#tamaño de la ventana
ventana.geometry("900x900")  # pixeles ancho x alto
ventana.configure(bg="#C1F7E5")

etiqueta = tk.Label(ventana, text="Actividad 7 - Huffman")
etiqueta.pack(pady=10)

#botones
btn_examinar = tk.Button(ventana, text="Examinar", command = lambda : examinar())
btn_examinar.pack(pady=10)

btn_comprimir = tk.Button(ventana, text="Comprimir", command = lambda : comprimir(Direccion))
btn_comprimir.pack(pady=5)

btn_descomprimir = tk.Button(ventana, text="Descomprimir", command = lambda : descomprimir())
btn_descomprimir.pack(pady=5)

#widget de texto para mostrar la lista de caracteres
txt_lista = tk.Text(ventana, height=40, width=30)
txt_lista.pack(pady=10)

ventana.mainloop()
