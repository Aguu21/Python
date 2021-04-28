def revisionExamen(cantidad, porcentaje):
    '''Dada la cantidad de ejercicios de un examen y porcentaje necesario,
    entrega un grupo de examenes revisados'''
    
    valorCentinela = ""
    cantidadPorcentaje = (cantidad * porcentaje)//100
    numAlumno = 0
    
    while valorCentinela != "Finish":
        cantidadResueltos = input("Ingrese la cantidad de ejercicios hechos: ")
        if cantidadResueltos > cantidad or cantidadResueltos < 0:
            print("Valores erroneos")
        else:
            if cantidadResueltos >= cantidadPorcentaje:
                total = "Aprobado"
            else:
                total = "Desaprobado"
            numAlumno += 1
            print("El alumno " + str(numAlumno) + " ha " + total)
            
        valorCentinela = str(input("Ingrese 'Finish' si desea terminar: "))
        
    return numAlumno
