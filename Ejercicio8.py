def enteroRomano(entero):
    '''Convierte un numero entero dado en uno romano'''
    
    numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romanos = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L',
               'XL', 'X', 'IX', 'V', 'IV', 'I']
    
    total = ''
    posicion = 0
    
    while entero > 0:
        for i in range(entero // numeros[posicion]):
            total += romanos[posicion]
            entero -= numeros[posicion]
            
        posicion += 1
        
    return total
