'''   1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.'''

print("Hola Mundo")

'''2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
realizar la impresión por pantalla.'''

Nombre = str(input("Escriba su Nombre:"))
print(f"Hola, {Nombre}, Como estas?")

'''3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
la impresión por pantalla.
'''

Apellido = str(input("Apellido: "))
Edad = int(input("Edad: "))
Pais = str(input("Pais de Origen: "))
print(f"Hola soy {Nombre} {Apellido}, Mi edad es {Edad} Años, Soy Originario de {Pais}")

''' 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
su perímetro.'''

import math
Radio = int(input("Ingrese Radio de la circunferencia: "))
Perimetro = 2*math.pi*Radio
Area = math.pi*Radio**2
print(f"El Perimetro del circulo es: {Perimetro} y El area es: {Area}")

''' 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
cuántas horas equivale.
'''

Segundo = int(input("Ingrese Cantidad de segundos: "))
Horas = float(Segundo/3600)
print(f"{Segundo} Son {Horas} horas")

'''6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
multiplicar de dicho número.
'''

def TablaDeMultiplicar():
    Numero = int(input("Escriba un numero del 1 al 10: "))
    for i in range (1,11):
        x=Numero*i
        print(f"{Numero}*{i} = {x}")
TablaDeMultiplicar()

'''7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos'''

def DosNumerosEnteros():
    Num1 = int(input("Número 1: "))
    Num2 = int(input("Número 2: "))

    if Num1 != 0 and Num2 != 0:
        sumar = Num1 + Num2
        dividir = Num1 / Num2
        multiplicar = Num1 * Num2
        restar = Num1 - Num2
        
        print(f"La suma es: {sumar}")
        print(f"La división es: {dividir}")
        print(f"La multiplicación es: {multiplicar}")
        print(f"La resta es: {restar}")
    else:
        print("Los números tienen que ser distintos de 0")
DosNumerosEnteros()

'''8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
modo:'''

def IMC():
    Peso = float(input("Peso en Kilogramos: "))
    Altura = float(input("Altura en Metros: "))
    IMC= Peso / (Altura**2)
    print(f"Su IMC es: {IMC}")
IMC()

'''9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit. '''

Celsius = float(input("Temperatura en Celsius: "))
Fahrenheit = 9/5 * Celsius + 32
print(f"En {Celsius} grados Celsius son {Fahrenheit} grados Fahrenheit.")

'''10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
dichos números.
'''
def Promedio():
    Num1 = float(input("Número 1: ")) 
    Num2 = float(input("Número 2: "))
    Num3 = float(input("Número 3: "))

    promedio = (Num1 + Num2 + Num3) / 3 

    print(f"El Promedio es: {promedio}")

Promedio()






