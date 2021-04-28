def factorialEntero(numero):
    '''Calcula el factorial dado un numero entero.'''
    
    factorial = numero
    
    for i in range(1, abs(numero)):
        factorial *= i

    return factorial
