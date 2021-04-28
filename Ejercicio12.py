def cantidadVocales(cadenaUsuario):
    '''Dada una cadena de caracteres devuelve la cantidad de vocales
    en la misma'''
    
    vocales = 0
    cadenaUsuario = cadenaUsuario.upper()
    
    for i in range (0, len(cadenaUsuario)):
        if cadenaUsuario[i] in ["A", "E", "I", "O", "U"]:
            vocales += 1
    return vocales


cadenaUsuario = str(input("Ingrese una cadena de caracteres: "))

print ("La frase tiene : " + str(cantidadVocales(cadenaUsuario)) + " vocales.")
