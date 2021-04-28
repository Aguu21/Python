def cortadorLetras(cadena, longitudMax, costoCorta, costoLarga):
    '''Corta de una cadena aquellas palabras con mas de x letras, dejandolas
    con x caracteres y un @ al final de cada palabra cortada,
    ademas de eliminar espacios extras y reemplazar los '.' por STOP y agregar
    al final un STOPSTOP haya o no punto final'''
    
    cadenaCortada = cadena.split(' ')
    costoCortaCant = 0
    costoLargaCant = 0
    auxSTOP=''
    for i in range(0, len(cadenaCortada)):
        
        if len(cadenaCortada[i]) > (longitudMax):
            for x in range(0, len(cadenaCortada[i])):
                palabra = cadenaCortada[i]
                if palabra[x] == '.':
                    auxSTOP = ' STOP'
                else:
                    auxSTOP = ''
                    
            cadenaAux = cadenaCortada[i]
            cadenaAux = cadenaAux[0:(longitudMax)] + '@'
            costoCortaCant += 1   
            if i != (len(cadenaCortada)-1):
                cadenaCortada[i] = cadenaAux + auxSTOP
            else:
                cadenaCortada[i] = cadenaAux
        else:
            costoLargaCant += 1

    cadena = ''
    for i in range(0, len(cadenaCortada)):
        if cadenaCortada[i] != '':
            cadena += cadenaCortada[i] + ' '
    cadena += 'STOPSTOP'
    resultado = [cadena, (costoCortaCant*costoCorta)
                 + (costoLargaCant*costoLarga)]
    return resultado

