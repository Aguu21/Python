def fahrenheitCelsius(fahrenheit):
    '''Convierte un valor dado en Fahrenheit a Celsius.'''

    celsius = (fahrenheit - 32) * 5/9
    
    return celsius


fahrenheit = int(input("Ingrese el valor en Fahrenheit a convertir: "))

print("Su valor en Celsius es: " + str(fahrenheitCelsius(fahrenheit)))
