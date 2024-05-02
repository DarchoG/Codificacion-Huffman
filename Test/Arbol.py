import heapq
import os

class nodoHuffman:

    def __init__(self, caracter, frecuencia):

        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    def __lt__(self, otro):
        
        return self.frecuencia < otro.frecuencia

class arbolHuffman:

    def __init__(self):

        self.arbol = []
        self.tabla_codigos = {}
        self.texto = ""
        self.rutaComprimido = ""
            
    def construirArbol(self, tuplas): # La tupla se encuentra ordenada de menor a mayor por lo tanto selecciono en pares los objetos a iterar.

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

    def generarCodigos(self, tuplas):

        tabla_codigos = {}

        self.arbol = self.construirArbol(tuplas)


        def explorar(nodo, codigo=''):

            if nodo is not None: # Procuro estar presente en un nodo que disponga valor, por lo tanto me indicaria que no me encuentro en un nodo padre

                if nodo.caracter is not None:

                    tabla_codigos[nodo.caracter] = codigo

                explorar(nodo.izquierda, codigo + '0') # Recursividad que explore todos los lados izquierdos
                explorar(nodo.derecha, codigo + '1') # Recursividad que explore todo los lados derechos

        explorar(self.arbol) #Dato mutable es pasado como referencia

        return tabla_codigos

    def codificarTexto(self, texto, tuplas):

        textoCodificado = ""
        self.texto = texto

        codigos = self.generarCodigos(tuplas)

        for letra in texto:
            
            textoCodificado += codigos.get(letra, "");

        return textoCodificado
    
    def comprimir(self, rutaArchivo, contenido, tuplas):
 
        rutaCarpeta = os.path.dirname(rutaArchivo)
        rutaCarpeta += "/Resultados" 

        try:
            os.makedirs(rutaCarpeta)
    
        except:
             
             print("Carpeta no creada")

        nombreArchivo = rutaCarpeta + "/codificacion.huffman"
        self.rutaComprimido = nombreArchivo

        with open(nombreArchivo, 'wb') as archivoComprimido:

            textoCodificado = self.codificarTexto(contenido, tuplas)

            # Añadir ceros al final para asegurar un múltiplo de 8 bits

            while len(textoCodificado) % 8 != 0:
                
                textoCodificado += '0'

            # Convertir el texto codificado a bytes

            bytes = bytearray([int(textoCodificado[i:i+8], 2) for i in range(0, len(textoCodificado), 8)])
            
            archivoComprimido.write(bytes)

        return archivoComprimido
    
    def descomprimir(self):

        nombreOriginal = os.path.dirname(self.rutaComprimido)
        nombreOriginal += "/archivoDescomprimido.txt"

        with open(self.rutaComprimido, 'rb') as archivoComprimido, open(nombreOriginal, 'w', encoding='utf-8') as archivoOriginal:

            bits = ''.join(format(byte, '08b') for byte in archivoComprimido.read())
            texto_descomprimido = ''
            nodo_actual = self.arbol

            for bit in bits:
                if bit == '0':
                    nodo_actual = nodo_actual.izquierda
                else:

                    nodo_actual = nodo_actual.derecha

                if nodo_actual.caracter is not None:

                    texto_descomprimido += nodo_actual.caracter
                    nodo_actual = self.arbol

            archivoOriginal.write(texto_descomprimido)

        return nombreOriginal
