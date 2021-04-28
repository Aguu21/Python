def fahrenheitCelsius(fahrenheit):
    '''Convierte un valor dado en Fahrenheit a Celsius.'''

    celsius = (fahrenheit - 32) * 5/9
    
    return celsius


print ("Fahrenheit  |  Celsius")
print ('------------|----------')

for i in range (0, 121):
    if (i % 10) == 0:
        if i == 0:
            print ( '      ' +str(i)+ '     |    ' + str(fahrenheitCelsius(i)))
        elif i >= 100:
            print ( '     ' +str(i)+ '    |    ' + str(fahrenheitCelsius(i)))
        else:
            print ( '     ' +str(i)+ '     |    ' + str(fahrenheitCelsius(i)))
        print ('------------|----------')
