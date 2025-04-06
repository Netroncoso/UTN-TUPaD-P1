'''1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. '''

def MayorDeEdad():
    Edad=int(input("Ingrese Su Edad"))
    if Edad >= 18:
        print(f"Es Mayor de edad")
    else print (f"usted es menor de Edad")

