for i in range(5):
    precio = 0 # Variable acomuladora
    nombre = input('Ingrese nombre del comprador: ')
    apellido = input('Ingrese apellido del comprador: ')
    marca = input('Ingrese la marca: ')
    if marca == 'Ford':
        precio = precio + 100000
    elif marca == 'Chevrolet':
        precio = precio + 120000
    elif marca == 'Fiat':
        precio = precio + 80000
    puertas = input('Ingrese cantida de puertas: ')
    if puertas == '2':
        precio = precio + 50000
    elif puertas == '4':
        precio = precio + 65000
    elif puertas == '5':
        precio = precio + 78000
    color = input('Ingrese color: ')
    if color == 'Blanco':
        precio = precio + 10000
    elif color == 'Azul':
        precio = precio + 20000
    elif color == 'Negro':
        precio = precio + 30000
    print('La persona '+nombre +' '+apellido + ' compró un auto marca '+ marca +' de ' + puertas + ' puertas y color ' + color + ' con un precio de ' +str(precio) + '€')
    

    
