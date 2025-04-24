'''1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.'''
for i in range(0,101):
    print(i)

    '''O tambien podria ser'''
x=0 
while x<=100:
    print(x)
    x +=1
'''2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
dígitos que contiene. '''


z=int(input("ingrese un numero: "))
z1=z
cont=0
while z>0:
    z=z//10
    cont +=1
print(f"El numero ", z1, "tiene ", cont," digitos")

'''3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
dados por el usuario, excluyendo esos dos valores. '''

x=int(input("Ingrese Numero1: "))
y=int(input("Ingrese Numero2: "))

menor=min(x,y)
mayor=max(x,y)

suma=0
for i in range(menor+1,mayor):
    suma += i

print(f"La suma de los números entre {x} y {y}, excluyéndolos, es: {suma}")

'''4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
un 0. '''

Suma=0
Num=int(input("Ingrese Numeros Enteros: "))
while Num !=0:
    Suma += Num
    Num=int(input("Ingrese Numeros Enteros: "))
print(Suma)

'''5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.'''

import random
Acertijo=random.randint(0,9)
Num=int(input("Adivine Numero del 0 al 9: "))
Intentos=1
if Num <0 or Num >9:
    print("El numero no esta en el Rango 0 al 9")
    Num=int(input("Adivine Numero del 0 al 9: "))
while Num != Acertijo:
    Intentos += 1
    Num=int(input("Ese no es el Numero, Intente nuevamente: "))
print("intentos: ",Intentos,"\nEl numero es: ",Acertijo)

''' 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
entre 0 y 100, en orden decreciente. '''

for i in range(100,-1,-1):
    print(i)

'''8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
menor, pero debe estar preparado para procesar 100 números con un solo cambio). '''


Cnumeros = 0
Cnegativos = 0
Cpositivos = 0
Pares = 0
Impares = 0
while Cnumeros <= 10:
    try:
        numero = int(input("Ingrese un número: "))
        
        if abs(numero) % 2 == 0:
            Pares += 1
        else:
            Impares += 1

        if numero >= 0:
            Cpositivos += 1
        else:
            Cnegativos += 1

        Cnumeros += 1 

    except ValueError:
        print("Ingrese un número entero válido.")
print(f"Cantidad de positivos: {Cpositivos}")
print(f"Cantidad de Negativos: {Cnegativos}")
print(f"Pares: {Pares}")
print(f"Impares: {Impares}")


'''9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
poder procesar 100 números cambiando solo un valor). '''

Cnumeros = 0
Suma = 0
while Cnumeros < 10:
    try:
        numero = int(input("Ingrese un número: "))
        Suma +=numero
        Cnumeros += 1 
    except ValueError:
        print("Ingrese un número entero válido.")
print(Cnumeros)
print(Suma)
Media = (Suma/Cnumeros)
print(f"La media es:{Media} ")

'''10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. '''

numero = input("Ingrese un número: ")

if numero.isdigit():  # para verifica que sea un número positivo
    invertido = numero[::-1]
    print(f"El número invertido es: {invertido}")
else:
    print("Por favor, ingrese solo números positivos enteros.")

