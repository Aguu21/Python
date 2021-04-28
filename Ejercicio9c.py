import time

passwordVerdadera = "Pineda"
password = str(input("Ingrese la contra: "))
    
def validadorPassword(password):
    '''Devuelve un valor booleano si la password es correcta.'''

    resultado = True
    
    if passwordVerdadera == password :
        print("Bienvenido Usuario.")
        resultado = True
    else:
        for i in range (1, 6):
            if password != "Pineda":
                print ("Tiene " + str(5 - i) + " intentos mas. Ahora espere " +
                       str(i * 5) + " segundos mas")

                time.sleep(i * 5)
                password = str(input("Intente otra vez: "))
            else:
                break
            
        if passwordVerdadera == password :
            print("Bienvenido Usuario.")
            resultado = True
        else:
            print ("Se quedo sin intentos.")
            resultado = False
    return resultado

print(validadorPassword(password))
