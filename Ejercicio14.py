import random

numRandom = [0, 0, 0, 0, 0]
aciertos = 0
coincidencias = 0

for i in range (0, 4):
    numRandom[i] = random.randrange(0,10)

while numRandom[0] in [numRandom[1], numRandom[2], numRandom[3]]:
    numRandom[0] = random.randrange(0, 10)
    
while numRandom[1] in [numRandom[2], numRandom[3]]:
    numRandom[1] = random.randrange(0,10)
    
while numRandom[2] == numRandom[3]:
    numRandom[2] = random.randrange(0,10)

numRandom[4] = str(str(numRandom[0]) + str(numRandom[1]) +
                   str(numRandom[2]) + str(numRandom[3]))

numJugador = str(input("Ingrese un numero de cuatro caracteres"+
                       " no repetidos, entre comillas: "))

while numJugador != numRandom[4]:
    for i in range (0,4):
        if numJugador[i] == str(numRandom[i]):
            aciertos += 1
        else:
            if numJugador[i] in [str(numRandom[0]), str(numRandom[1]),
                                 str(numRandom[2]), str(numRandom[3])]:
                coincidencias += 1
        
    print("Tiene " + str(aciertos) + " aciertos y " +
          str(coincidencias) + " coincidencias.")
    
    numJugador = str(input("Ingrese un numero con las mismas condiciones: "))
    aciertos = 0
    coincidencias = 0
    
print ("Encontro el numero!")
