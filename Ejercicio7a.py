def yearBisiestoVoF(year):
    '''Decide si un year es o no bisiesto'''
    
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                total = True
            else: False
        else:
            total = True
    else:
        total = False
        
    return total
