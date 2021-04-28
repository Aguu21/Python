def cortadorLetras(cadena, longitudMax, costoCorta, costoLarga):
    '''Corta de una cadena aquellas palabras con mas de x letras, dejandolas
    con x caracteres y un @ al final, ademas de eliminar espacios extras'''
    
    cadenaCortada = cadena.split(' ')
    costoCortaCant = 0
    costoLargaCant = 0
    
    for i in range(0, len(cadenaCortada)):
        if len(cadenaCortada[i]) > (longitudMax):
            cadenaAux = cadenaCortada[i]
            cadenaAux = cadenaAux[0:(longitudMax)] + "@"
            cadenaCortada[i] = cadenaAux
            costoCortaCant += 1
        else:
            costoLargaCant += 1
            
    cadena = ''

    for i in range(0, len(cadenaCortada)-1):
        cadena += cadenaCortada[i] + ' '

    cadena += cadenaCortada[len(cadenaCortada) - 1]
    resultado = [cadena, (costoCortaCant*costoCorta)
                 + (costoLargaCant*costoLarga)]

    return resultado
