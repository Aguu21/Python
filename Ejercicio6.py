def mayorProducto (primero, segundo, tercero, cuarto):
    '''Encuentra el mayor producto entre dos numeros, dados cuatro numeros.'''
    
    resultado = primero * segundo
    resultadosegundo = primero * tercero
    resultadotercero = primero * cuarto
    
    if (resultado > resultadosegundo):
        if (resultado > resultadotercero):
            total = resultado
        else:
            total = resultadotercero
    else:
        if resultadosegundo > resultadotercero:
            total = resultadosegundo
        else:
            total = resultadotercero
    
    resultado = segundo * tercero
    resultadosegundo = segundo * cuarto

    if (resultado > resultadosegundo):
        if (total < resultado):
            total = resultado
    else:
        if (total < resultadosegundo):
            total = resultadosegundo
            
    resultado = tercero * cuarto

    if resultado > total:
        total = resultado
    return total
