from core.reader import Reader
from core.identify_patterns import IdentifyPatterns
from tabulate import tabulate

tokens = Reader().read().processText()
patterns = IdentifyPatterns().identify(tokens)

print('Lectura del Archivo:')
print((Reader()).read().text)
print('\n\n')

print('Patrones encontrados:')
if len(patterns) > 0:
    print(tabulate(patterns))
else:
    print('No se encontraron ocurrencias')


