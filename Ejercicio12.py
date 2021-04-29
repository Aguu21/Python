def cantidadVocales(cadenaUsuario):
    '''Dada una cadena de caracteres devuelve la cantidad de cada una de las
    vocales en la misma'''
    
    cadenaUsuario = cadenaUsuario.upper()
    cantidadAEIOU = [0, 0, 0, 0, 0]

    for i in range (0, len(cadenaUsuario)):
        
        if cadenaUsuario[i] == "A":
            cantidadAEIOU[0] += 1
            
        elif cadenaUsuario[i] == "E":
            cantidadAEIOU[1] += 1
            
        elif cadenaUsuario[i] == "I":
            cantidadAEIOU[2] += 1
            
        elif cadenaUsuario[i] == "O":
            cantidadAEIOU[3] += 1
            
        elif cadenaUsuario[i] == "U":
            cantidadAEIOU[4] += 1
    return cantidadAEIOU

cadenaUsuario = str(input("Ingrese una cadena de caracteres: "))
vocales = cantidadVocales(cadenaUsuario)

print("La frase tiene " + str(vocales[0]) + " A's, " +
      str(vocales[1]) + " E's, " + str(vocales[2]) + " I's, " +
      str(vocales[3]) + " O's, " + str(vocales[4]) + " U's")
