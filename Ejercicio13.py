def capitalizado(primeraCadena, segundaCadena):
    '''Dadas dos cadenas de caracteres, devuelve un valor booleano
    de si la primera es la version capitalizada de la segunda'''
    
    if primeraCadena == segundaCadena.upper():
        resultado = True
    else:
        resultado = False
    return resultado


primeraCadena = str(input("Ingrese la primera palabra: "))
segundaCadena = str(input("Ingrese la segunda palabra: "))

print(capitalizado(primeraCadena, segundaCadena))
