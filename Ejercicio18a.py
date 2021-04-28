
lista = ["Di","buen","dia","a","papa"]

def inversorListas(lista):
    '''Dada una lista, entrega una nueva con las mismas cadenas pero
    con el orden invertido'''
    
    aux = 0
    listaInvertida = lista
    
    for i in range(0, int(len(listaInvertida)/2)):
        
        aux = listaInvertida[i]
        listaInvertida[i] = listaInvertida[-i-1]
        listaInvertida[-i-1] = aux

    return listaInvertida

