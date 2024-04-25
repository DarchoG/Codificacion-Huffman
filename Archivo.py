import os
from tkinter import *
from tkinter import ttk

def generarDiccionario():
    
    Diccionario = {}

    for i in range(256):
        
        Diccionario[chr(i)] = i

    Diccionario["’"] = 256
    print(Diccionario)

    return Diccionario;   

def leerArchivo(Archivo):
    
    try:

        with open (Archivo, "r", encoding="utf8") as Documento:

            Contenido = Documento.read()
            return Contenido
        
    except FileNotFoundError:

        print("Archivo no Encontrado");
        return None;
    
def contarPalabras():

    
    #Diccionario = generarDiccionario();
    Contador = 0
    Diccionario = {};
    Archivo = leerArchivo("C:/Users/GuzDa/OneDrive/Documentos/Algoritmos/Huffman/Gullivers_Travels.txt")
    Lista = []

    for i in range(len(Diccionario)):

        Lista.append(0);

    for i in Archivo:

        #print(i);

        try: 

            Lista[Diccionario[i]] += 1;

        except:

            Lista.append(1)
            Diccionario[i] = Contador

            Contador += 1

    print(Diccionario);
    print(Lista);      
    
    return Lista

def swarp(a, b):

    Temporal = a;
    a = b;
    b = Temporal

def particion (Diccionario, Inicio, Final):

    pivote = Diccionario[Inicio].key();
    i = Diccionario[Inicio + 1].key();

    for i in range(Final - Inicio):
        if(pivote >= Diccionario[i]):
            pass
            
def quicksort(Arreglo, Diccionario):

    pass

#print(leerArchivo("C:/Users/GuzDa/OneDrive/Documentos/Algoritmos/Huffman/Gullivers_Travels.txt"));    
contarPalabras()

# os.getcwd() Retornar Directorio
# os.mkdir() Crear carpeta

#1614
#btn = ttk.Button(Frame)
#print(btn.configure().keys()) Me regresa todas las posibles configuraciones o elementos a editar de cada label

#Progres Bar (Mostrar de manera interactiva el progreso del usuario)

##print(Diccionario["’"]);
