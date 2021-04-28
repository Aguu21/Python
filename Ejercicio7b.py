def cantidadDias(mes):
    '''Devuelve cuantos dias tiene el mes dado en spanish.'''
    
    mes = mes.upper()
    if mes in ["ABRIL", "JUNIO", "SEPTIEMBRE", "NOVIEMBRE"]:
        dias = "30"
    elif mes in ["ENERO", "MARZO", "MAYO", "JULIO",
                 "AGOSTO", "OCTUBRE", "DICIEMBRE"]:
        dias = "31"
    elif mes in ["FEBRERO"]:
        dias = "28"
    else:
        dias = "Error"
        
    return dias

