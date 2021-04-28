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


def validadorFecha(dia, mes, year):
    '''Define si una fecha es valida en el formato (dia, mes, year)'''
    
    if year >= 0:
        resultadoYear = True
    else:
        resultadoYear = False
        
    if mes >= 1 and mes < 13:
        if mes in [1, 3, 5, 7, 8, 10, 12]:
            if dia > 0 and dia < 32:
                resultadoMesDia = True
            else:
                resultadoMesDia = False
        else:
            if mes == 2:
                if yearBisiestoVoF(year) == True:
                    if dia >= 1 and dia < 30:
                        resultadoMesDia = True
                    else:
                        resultadoMesDia = False
                else:
                    if dia >= 1 and dia < 29:
                        resultadoMesDia = True
                    else:
                        resultadoMesDia = False
            else:
                if dia > 0 and dia < 31:
                    resultadoMesDia = True
                else:
                    resultadoMesDia = False
    else:
        resultadoMesDia = False
        
    if resultadoYear == True and resultadoMesDia == True:
        resultado = True
    else:
        resultado = False
        
    return resultado

