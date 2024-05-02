import heapq

class nodoHuffman:

    def __init__(self, caracter, frecuencia):

        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    def __lt__(self, otro):
        
        return self.frecuencia < otro.frecuencia

def construirArbol(tuplas): # La tupla se encuentra ordenada de menor a mayor por lo tanto selecciono en pares los objetos a iterar.

    arbol = [] 
    heapq.heapify(arbol)

    for i in range(len(tuplas)):

        nodoNuevo = nodoHuffman(tuplas[i][0], tuplas[i][1])
        heapq.heappush(arbol, nodoNuevo)

    while len(arbol) > 1:
        
        nodoIzquierdo = heapq.heappop(arbol)
        nodoDerecho = heapq.heappop(arbol)
        frecuenciaPadre = nodoIzquierdo.frecuencia + nodoDerecho.frecuencia

        nuevoNodo = nodoHuffman(None, frecuenciaPadre)
        nuevoNodo.izquierda = nodoIzquierdo
        nuevoNodo.derecha = nodoDerecho

        heapq.heappush(arbol, nuevoNodo)

    return arbol[0]

def generarCodigos(arbol):

    tabla_codigos = {}

    def explorar(nodo, codigo=''):

        if nodo is not None: # Procuro estar presente en un nodo que disponga valor, por lo tanto me indicaria que no me encuentro en un nodo padre

            if nodo.caracter is not None:

                tabla_codigos[nodo.caracter] = codigo

            explorar(nodo.izquierda, codigo + '0') # Recursividad que explore todos los lados izquierdos
            explorar(nodo.derecha, codigo + '1') # Recursividad que explore todo los lados derechos

    explorar(arbol) #Dato mutable es pasado como referencia

    return tabla_codigos

def codificarTexto(texto, codigos):

    textoCodificado = ""

    for letra in texto:
        
        textoCodificado.join = codigos[letra];

    return textoCodificado
