import random
numRandom = int(random.randrange(1, 1000))
numJugador = int(input("Ingrese un numero: "))
while numJugador != numRandom:
    if numJugador > numRandom:
        numJugador = int(input("Ingrese un numero menor al anterior: "))
    elif numJugador < numRandom:
        numJugador = int(input("Ingrese un numero mayor al anterior: "))
print("Ha adivinado el numero!")

