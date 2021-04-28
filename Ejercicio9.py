passwordVerdadera = "Pineda"
password = str(input("Ingrese la contra: "))

if passwordVerdadera == password :
    print("Bienvenido Usuario")

else:
    while password != "Pineda":
        password = str(input("Intente otra vez: "))
        
    print ("Bienvenido Usuario")
