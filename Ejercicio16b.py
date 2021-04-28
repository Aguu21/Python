def vocalesLetras(cadena):
    '''Dada una cadena, entrega las vocales'''

    cadena = cadena.split(' ')
    consonantes = ''
    resultado = ''
    
    for i in range(0, len(cadena)):
        palabra = cadena[i]
        
        for x in range(0, len(palabra)):
            if palabra[x] in ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]:
                resultado += palabra[x]
            
        if i != (len(cadena)-1):
            resultado += " "      
            
    return resultado
