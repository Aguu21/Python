def primerasLetras(cadena):
    '''Dada una lista de palabras, entrega las primeras letras'''

    cadena = cadena.split(' ')
    resultado = ''

    for i in range(0, len(cadena)):
        palabra = cadena[i]
        resultado += palabra[0]
        
    return resultado
