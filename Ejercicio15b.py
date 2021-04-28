def cadenaTitulo(cadena):
    '''Dada una lista de palabras, entrega las primeras letras en mayuscula'''

    cadena = cadena.split(' ')
    resultado = ''

    for i in range(0, len(cadena)):
        palabra = cadena[i]
        palabra = palabra[0:1].upper()+ palabra[1:len(palabra)]
        
        if i != (len(cadena)-1):
            resultado += palabra + " "
        else:
            resultado += palabra
            
    return resultado
