**Funcionamiento**

La ventana es generada a partir de un porcentaje del tamaño del display en orden para crear widgets con valores relativos y ajustarse mejor a la dimensione de los dispositivos, al momento de estirar o modificar el tamaño de la ventana la posición y proporción se mantienen iguales.

Fue empleado grid para empaquetar los frames y widgets, los botones disponen de funciones que pueden ser alteradas.

**Inputs**

La interfaz cuenta con tres botones los cuales son contemplados para realizar las siguientes actividades:

**- Examinar:** Abre el explorador de archivos, modifica el widget de texto superior y retorna la dirección absoluta del archivo para trabajarlo posteriormente.

**- Comprimir:** Ejecuta los algoritmos necesarios para comprimir el archivo, para incorporar dichos elementos es requerido modificar su argumento **"None"** donde tendrá que ser incorporado la función deseada a realizar, es sugerido cambiar el contenido del contendor del texto por la estructura de datos empleada para la representación de los caracteres repetidos.

**- Descomprimir:** Regresa el archivo a documento de texto, de igual manera su funcionalidad se encuentra inicializada en **"None"** lista para ser sustituida.

**Outputs**

El frame "contenidoPalabras" es susceptible de ser modificado y muestra en primera instancia el contenido del archivo seleccionado con una barra de navegación (scroll).
