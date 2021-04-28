
lista = ["Di","buen","dia","a","papa"]

def inversorListas(lista):
    '''Dada una lista, entrega la misma con las mismas cadenas pero
    con el orden invertido'''
    
    for i in range(0, int(len(lista)/2)):
        lista[i], lista[-i-1] = lista[-i-1], lista[i]
    
    return lista
