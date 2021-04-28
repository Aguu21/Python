def palindromo(cadena):
    '''Confirma si una cadena es palindromo, anedac es cadena al reves'''

    cadena = cadena.split(' ')
    cadenaRenovada = ""
    anedac = ""

    for i in range(0, len(cadena)):
        cadenaRenovada += cadena[i]
        
    for i in cadenaRenovada[::-1]:
       anedac += i
       
    if cadenaRenovada == anedac:
        resultado = True
    else:
        resultado = False
        
    return resultado
