import time

passwordVerdadera = "Pineda"
password= str(input("Ingrese la contra: "))

if passwordVerdadera == password :
    print("Bienvenido Usuario.")
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
        print("Bienvenido Usuario")
    else:
        print ("Se quedo sin intentos")

