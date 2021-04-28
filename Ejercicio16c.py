   
def vocalesContinuas(cadena):
    '''Dada una cadena, entrega la cadena con las vocales cambiadas
    por la siguiente'''

    cadena = cadena.lower()
    vocales=['a','e','i','o','u']
    total = ""
    
    for i in range (0, len(cadena)):
        palabra = cadena[i]
    
        if palabra in vocales:
            for x in range (0, 5):
                if palabra == vocales[x]:
                    if x != 4:
                        palabra = vocales[x+1]
                    else:
                        palabra = vocales[0]
                    total += palabra
                    break
        else:
            total += cadena[i]
            
    return total



