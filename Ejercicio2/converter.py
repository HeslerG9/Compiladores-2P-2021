print("*********CONVERTIDOR DE NUMEROS**************")
#Función para obtener valores de tipo caracter hexadecimal
def obtener_caracter_hexadecimal(valor):
    valor = str(valor)
    equivalencias = {
        "10": "a",
        "11": "b",
        "12": "c",
        "13": "d",
        "14": "e",
        "15": "f",
    }
    if valor in equivalencias:
        return equivalencias[valor]
    else:
        return valor

#Función para convertir de Decimal a Hexadecimal
def decimal_a_hexadecimal(decimal):
    hexadecimal = ""
    while decimal > 0:
        residuo = decimal % 16
        verdadero_caracter = obtener_caracter_hexadecimal(residuo)
        hexadecimal = verdadero_caracter + hexadecimal
        decimal = int(decimal / 16)
    return hexadecimal

#Función para obtener el valor decial de los caracteres en hexadecimal 
def obtener_valor_real(caracter_hexadecimal):
    equivalencias = {
        "f": 15,
        "e": 14,
        "d": 13,
        "c": 12,
        "b": 11,
        "a": 10,
    }
    if caracter_hexadecimal in equivalencias:
        return equivalencias[caracter_hexadecimal]
    else:
        return int(caracter_hexadecimal)

#Función para convertir de Hexadecimal a Decimal
def hexadecimal_a_decimal(hexadecimal):
    hexadecimal = hexadecimal.lower()
    hexadecimal = hexadecimal[::-1]
    decimal = 0
    posicion = 0
    for digito in hexadecimal:
        valor = obtener_valor_real(digito)
        elevado = 16 ** posicion
        equivalencia = elevado * valor
        decimal += equivalencia
        posicion += 1
    return decimal

#Función para convertir de Decimal a Octal
def decimal_a_octal(decimal):
    octal = ""
    while decimal > 0:
        residuo = decimal % 8
        octal = str(residuo) + octal
        decimal = int(decimal / 8)
    return octal

#Función para convertir de Octal a Decimal 
def octal_a_decimal(octal):
    decimal = 0
    posicion = 0
    octal = octal[::-1]
    for digito in octal:
        valor_entero = int(digito)
        numero_elevado = int(8 ** posicion)
        equivalencia = int(numero_elevado * valor_entero)
        decimal += equivalencia
        posicion += 1
    return decimal

#Función para convertir de Decimal a Binario
def decimal_a_binario(decimal):
    if decimal <= 0:
        return "0"
    binario = ""
    while decimal > 0:
        residuo = int(decimal % 2)
        decimal = int(decimal / 2)
        binario = str(residuo) + binario
    return binario

#Función para convertir de Binario a Decimal 
def binario_a_decimal(binario):
    posicion = 0
    decimal = 0
    binario = binario[::-1]
    for digito in binario:
        multiplicador = 2**posicion
        decimal += int(digito) * multiplicador
        posicion += 1
    return decimal

#Funcion para interactuar con el Usuario y solocitar datos 
def solicitar_datos_a_usuario():
    bases_soportadas = ["2", "8", "10", "16", ]
    base_origen = input("""
2 -  Binario
8 -  Octal
10 - Decimal
16 - Hexadecimal
Elige la base de tu entrada: [2, 8, 10, 16]:""") #Se espera que el usuario ingrese una opción
    if base_origen not in bases_soportadas: #En esta sección se verifica que el dato ingresado sea soportado
        print("La base que ingresaste no está soportada")
        return
    numero = input(
        f"--------------------------------------------------------------------------------\n"
        f"Ok, la base seleccionada es {base_origen}. Ingresa el número a convertir: ")
    base_destino = input("""
--------------------------------------------------------------------------------
2 -  Binario
8 -  Octal
10 - Decimal
16 - Hexadecimal
Elige la base a la que conviertes: [2, 8, 10, 16]: """) #Se espera que el usuario ingrese una opción
    if base_destino not in bases_soportadas: #Se verifica que la opcion ingresada por el usuario sea soportada 
        print("La base de destino no está soportada")
        return
    return (base_origen, numero, base_destino)

#Funcion para obtener el valor en decimal
def obtener_numero_decimal(base_origen, numero):
    if base_origen == "2":
        return binario_a_decimal(numero)
    elif base_origen == "8":
        return octal_a_decimal(numero)
    elif base_origen == "10":
        return int(numero)
    elif base_origen == "16":
        return hexadecimal_a_decimal(numero)

#Funcion para convertir a deciamal el valor ingresado 
def convertir(numero, base_destino):
    if base_destino == "2":
        return decimal_a_binario(numero)
    elif base_destino == "8":
        return decimal_a_octal(numero)
    elif base_destino == "10":
        return int(numero)
    elif base_destino == "16":
        return decimal_a_hexadecimal(numero)


if __name__ == '__main__':
    datos = solicitar_datos_a_usuario()
    if datos:
        base_origen, numero, base_destino = datos
        numero_decimal = obtener_numero_decimal(base_origen, numero)
        resultado = convertir(numero_decimal, base_destino)
        print("--------------------------------------------------------------------------------\n"
              "El resultado es:")  #Se imprime el resultado 
        print(resultado)

