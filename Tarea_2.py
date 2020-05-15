#TRABAJO DE CLASE 2: Autos.
#Dada una concesionaria de autos, 5 clientes van a pedir un auto, debe preguntarsele:
#*Nombre y apellido del comprador.
#*Marca
#*Puertas
#*Color

#Marcas posibles y sus precios:
#-Ford $100000
#-Chevrolet: $120000
#-Fiat: $80000

#Por la cantidad de puertas se añade un precio:
#-2: $50000
#-4: $65000
#-5: $78000

#Dependiendo del color, se deben sumar:
#-Blanco: $10000
#-Azul: $20000
#-Negro: $30000

#Deben imprimirse los datos de cada compra y el precio total.




presupuesto = '\n\nPresupuestos:\n'

# Número de presupuestos a realizar. Pedir datos de compra
for i in range(5):
    nombre = input('Introduzca su Nombre: ')
    apellidos = input('Introduzca sus Apellidos: ')
    #Se comprueba la marca:
    comprobar_marca = True
    while comprobar_marca == True:
        marca = input('Marca del Vehículo a elegir: \nFord \nChevrolet \nFiat \nIntroduzca la marca elegida: ')
        if marca == 'Ford':
            comprobar_marca = False
        elif marca == 'Chevrolet':
            comprobar_marca = False
        elif marca == 'Fiat':
            comprobar_marca = False
    
        else:
            print('\nEl dato introducido no es válido.')

    #Se comprueba el número de puertas:
    comprobar_pruertas = True
    while comprobar_pruertas == True:      
        puertas = input('Número de puertas a elegir: \n2 \n4 \n5 \nIntrozca el número de puertas elegidas: ')
        if puertas == '2':
            comprobar_pruertas = False
        elif puertas == '4':
            comprobar_pruertas = False
        elif puertas == '5':
            comprobar_pruertas = False
        else:
            print('\nEl dato introducido no es válido.')

    #Se comprueba el color:
    comprobar_color = True
    while comprobar_color == True:
        color = input('Colores a elegir: \nBlanco \nAzul \nNegro \nIntroduzca el color elegido: ')
        if color == 'Blanco':
            comprobar_color = False
        elif color == 'Azul':
            comprobar_color = False
        elif color == 'Negro':
            comprobar_color = False
        else:
            print('\nEl dato introducido no es válido.')
    
  
    #Se elige la marca:
    if marca == 'Ford':
        precio_marca = 100000
    elif marca == 'Chevrolet':
        precio_marca = 120000
    elif marca == 'Fiat':
        precio_marca = 80000
        

    #Se elige el número de puertas:
    if puertas == '2':
        precio_puertas = 50000
    elif puertas == '4':
        precio_puertas = 65000
    elif puertas == '5':
        precio_puertas = 78000
    

    #Se elige el color:
    if color == 'Blanco':
        precio_color = 10000
    elif color == 'Azul':
        precio_color = 20000
    elif color == 'Negro':
        precio_color = 30000
        
    presupuesto = presupuesto + '\nNombre: ' + nombre + '\nApellidos: ' + apellidos + '\nMarca: ' + marca + '\nNúmero de puertas: ' + puertas + '\nColor: ' + color + '\nPrecio total: ' + str(precio_marca + precio_puertas + precio_color) + ' $\n'

print(presupuesto)