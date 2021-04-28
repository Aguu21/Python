def palabrasA(cadena):
    '''Dada una cadena, solo las palabras que comiencen con A son devueltas'''
    
    cadena = cadena.split(' ')
    resultado = ''

    for i in range(0, len(cadena)):
        palabra = cadena[i]
        if palabra[0] in ["a", "A"]:
            if i != (len(cadena)-1):
                resultado += cadena[i] + " "
            else:
                resultado += cadena[i]
                
    return resultado
