import re
from typing import Pattern

class IdentifyPatterns:
    def __init__(self) : pass

    def identify(self, tokens):
        patterns = []

        for token in tokens:
            token = ('%s'.strip() % token).strip() #Limpiar el token
            
            if len(token) > 0:

                #Identificar secuencia de numeros
                if re.match(r'^\d+$',token):
                    patterns.append([token,'Secuencia de numeros'])
                
                #Identificar numeros seguidos de letras y numeros
                elif re.match(r'^\d+[a-zA-Z]+$',token):
                    patterns.append([token,'Secuencia de numeros seguido de secuencia de letras'])

                #Identificar vocales iguales
                elif re.match(r'^.*(aaa|eee|iii|ooo|uuu).*$',token):
                    patterns.append([token,'tres o mas vocales iguales en una palabra'])

                #Identificar caracteres especiales
                elif re.match(r'^.*(\&|\*).*$',token):
                    patterns.append([token,'caracteres especiales'])

                #Identificar palabras con 3 vocales
                elif re.match(r'^(.*(a).*(a).*(a).*)|(.*(e).*(e).*(e).*)|(.*(i).*(i).*(i).*)|(.*(o).*(o).*(o).*)|(.*(u).*(u).*(u).*)$',token):
                    patterns.append([token,'tres o mas vocales iguales en una palabra'])
                else:
                    pass

        return patterns

