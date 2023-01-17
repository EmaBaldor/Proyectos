from random import randint

opciones = ["piedra", "papel", "tijera"]

print("Bienvenido a Piedra, Papel y Tijera!")

jugar = True

while jugar:

    maq = opciones[randint(0,2)]
    usuario = input("Ingrese su opcion: \n").lower()

    print("Usted elegió: " + usuario)
    print("La maquina elegió: " + maq)

    if usuario == maq:
        print("Hubo un empate")
    elif (usuario == "piedra" and maq == "papel") or (usuario == "tijera" and maq == "piedra") or (usuario == "tijera" and maq == "piedra"):
        print("La maquina ganó")
    elif (maq == "piedra" and usuario == "papel") or (maq == "tijera" and usuario == "piedra") or (maq == "tijera" and usuario == "piedra"):
        print("Usted ganó")

    res = input("Desea jugar nuevamente? si/no \n").lower()
    if res == "no":
        jugar = False
        print("Adios!.")


