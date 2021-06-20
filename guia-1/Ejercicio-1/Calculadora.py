import math

opcion=int(input("""Ingrese la operación que desea realizar
1=suma
2=resta
3=multiplicación
4=división
5=raíz cuadrada
"""))

if opcion>0 and opcion<5:
    print("Ingrese dos números")
    num1=float(input("Número 1: "))
    num2=float(input("Número 2: "))   

    res=0
    if opcion==1:
        res=num1+num2
        print(f"El resultado de la suma es: {res}")
    if opcion==2:
        res=num1-num2
        print(f"El resultado de la resta es: {res}")
    if opcion==3:
        res=num1*num2
        print(f"El resultado de la multiplicación es: {res}")
    if opcion==4:
        if num2!=0:
            res=num1/num2
            print(f"El resultado de la división es: {res}")
        else:
            print("No se puede dividir por 0")

if opcion==5:
    num=float(input("Ingrese el número al que le desea calcular la raíz cuadrada: "))
    print("La raíz cuadrada es:")
    print(math.sqrt(num))

else:
    print("Debe seleccionar una de las opciones validas")
    
