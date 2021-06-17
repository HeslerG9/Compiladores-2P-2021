import re
import sys

class Reader:
    def __init__(self) : pass

    def read(self):
        params = sys.argv[1:] # Obtener parametros de la consola
        self.fileName = params[0] # Obteniendo el nombre del archivo
        f = open(self.fileName,'r') # Abrir el archivo
        self.text = f.read() # Leer la completitud del archivo 
        f.close() # Cerrar la conexion del archivo

        return self # Retornar el objeto

    def processText(self):
        # tokens = [] # Declarando arreglo de Tokens
        text = self.text # Guardar texto en variable local
        text = re.sub(r'\s+',' ',self.text) # Eliminar los espacios por un espacio
        tokens = re.split(r'\s',text)
        return tokens

