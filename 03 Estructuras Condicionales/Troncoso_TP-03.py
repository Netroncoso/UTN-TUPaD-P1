'''1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. '''

def MayorDeEdad():
    Edad=int(input("Ingrese Su Edad: "))
    if Edad >= 18:
        print(f" Usted Es Mayor de edad")
    else:
     print(f"Usted es Menor")
MayorDeEdad()

'''2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
mensaje “Desaprobado”. '''

def Aprobado_Desaprovado():
   Nota=int(input("Ingrese Nota:"))
   if Nota >=6:
      print(f"Aprobado")
   else:
      print(f"Desaprobado")
Aprobado_Desaprovado()

''' 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
operador de módulo (%) en Python para evaluar si un número es par o impar. '''

def Ingrese_Numeros_Pares():
    Num = 0
    while Num != 1:
        Num = int(input("Ingresá un número par (1 para salir): "))
        if Num != 1:
            if Num % 2 == 0:
                print(f"El número {Num} es par.")
            else:
                print("¡Ese número no es par!")

    print("Saliste del programa.")

Ingrese_Numeros_Pares()

'''4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
siguientes categorías pertenece: 
● Niño/a: menor de 12 años. 
● Adolescente: mayor o igual que 12 años y menor que 18 años. 
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
● Adulto/a: mayor o igual que 30 años. '''

def RangosEtarios():
    Edad = int(input("Ingrese su edad: "))
    
    if Edad < 12:
        print("Niño/a")
    elif Edad >= 12 and Edad < 18:
        print("Adolescente")
    elif Edad >= 18 and Edad < 30:
        print("Adulto/a joven")
    else:
        print("Adulto/a")

RangosEtarios()

'''5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
como una lista o un string.'''

def Contraseña():
    Pass=str(input("Ingrese Una Contraseña: "))
    Caracteres=len(Pass)
    if Caracteres in range(8,15):
        print("Ha Ingresado una contraseña correcta")
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
Contraseña()


'''6) El paquete statistics de python contiene funciones que permiten tomar una lista de números 
y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el 
siguiente: 
from statistics import mode, median, mean 
mi_lista = [1,2,5,5,3] 
mean(mi_lista) 
En la documentación oficial se puede encontrar más información sobre este paquete: 
https://docs.python.org/es/3.8/library/statistics.html.  
La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se 
pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio: 
● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la 
mediana es mayor que la moda. 
● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, 
la mediana es menor que la moda. 
● Sin sesgo: cuando la media, la mediana y la moda son iguales. 
Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista 
numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 
Definir la lista numeros_aleatorios de la siguiente forma: 
import random 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 
Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de 
forma aleatoria.'''

import random
from statistics import mean, median, mode

''' Generar la lista de 50 números aleatorios entre 1 y 100 '''
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

''' Calcular media, mediana y moda '''
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

''' Mostrar valores calculados '''
print(f"Números aleatorios: {numeros_aleatorios}")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

''' Analizar sesgo '''
if media > mediana > moda:
    print("Sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("Sesgo negativo (a la izquierda)")
elif media == mediana == moda:
    print("Distribución sin sesgo")
else:
    print("No se puede determinar un sesgo claro con estos valores")

'''7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
pantalla.'''

def UltimaVocal():
    Palabra = str(input("Ingrese una palabra o frase: "))
    UltimaLetra = Palabra[-1].lower()
    if UltimaLetra in ['a', 'e', 'i', 'o', 'u']:
        print(f"{Palabra}!")
    else:
        print(f"{Palabra}")

UltimaVocal()

'''8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
dependiendo de la opción que desee: 
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
lower() y title() de Python para convertir entre mayúsculas y minúsculas. '''

def Mayus_Minusculas():
    Nombre=str(input("Ingrese su Nombre: "))
    Opcion=int(input("1. Si quiere su nombre en mayúsculas.\n2. Si quiere su nombre en minúsculas.\n3. Si quiere su nombre con la primera letra mayúscula. \n Ingrese Opcion: " ))
    if Opcion==1:
        Nombre=Nombre.upper()
    elif Opcion==2:
        Nombre=Nombre.lower()
    elif Opcion==3:
        Nombre=Nombre.title()
    else: print("Opcion Invalida")
    print(Nombre)

Mayus_Minusculas()

'''9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
por pantalla: 
● Menor que 3: "Muy leve" (imperceptible). 
● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
generalmente no causa daños). 
● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
débiles). 
● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). '''
def Categorizar_Sismo():
    magnitud = float(input("Ingrese la magnitud del sismo según la escala de Richter: "))

    if magnitud < 3:
        print("Muy leve (imperceptible)")
    elif magnitud >= 3 and magnitud < 4:
        print("Leve (ligeramente perceptible)")
    elif magnitud >= 4 and magnitud < 5:
        print("Moderado (sentido por personas, pero generalmente no causa daños)")
    elif magnitud >= 5 and magnitud < 6:
        print("Fuerte (puede causar daños en estructuras débiles)")
    elif magnitud >= 6 and magnitud < 7:
        print("Muy Fuerte (puede causar daños significativos)")
    else:
        print("Extremo (puede causar graves daños a gran escala)")

Categorizar_Sismo()

'''Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
si el usuario se encuentra en otoño, invierno, primavera o verano. '''

def Estacion_Segun_Fecha():
    hemisferio = input("¿En qué hemisferio estás? (N/S): ").upper()
    mes = int(input("¿Qué mes es? (1-12): "))
    dia = int(input("¿Qué día es? (1-31): "))

    if mes == 12 and dia >= 21 or mes in [1, 2] or (mes == 3 and dia <= 20):
        estacion_norte = "Invierno"
        estacion_sur = "Verano"
    elif mes == 3 and dia >= 21 or mes in [4, 5] or (mes == 6 and dia <= 20):
        estacion_norte = "Primavera"
        estacion_sur = "Otoño"
    elif mes == 6 and dia >= 21 or mes in [7, 8] or (mes == 9 and dia <= 20):
        estacion_norte = "Verano"
        estacion_sur = "Invierno"
    elif mes == 9 and dia >= 21 or mes in [10, 11] or (mes == 12 and dia <= 20):
        estacion_norte = "Otoño"
        estacion_sur = "Primavera"
    else:
        print("Fecha inválida.")
        return

    if hemisferio == "N":
        print(f"Estás en el hemisferio norte. La estación es {estacion_norte}.")
    elif hemisferio == "S":
        print(f"Estás en el hemisferio sur. La estación es {estacion_sur}.")
    else:
        print("Hemisferio no válido. Por favor, escribí N o S.")

Estacion_Segun_Fecha()

