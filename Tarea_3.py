#TRABAJO DE CLASE 3: Autos Parte 2.
#1-Ya no sabemos cuantos clientes tendremos,
#2-Si el pedido no es uno de los autos en venta, entonces debe volver a preguntar hasta que si lo sea
#3-Lo mismo con la cantidad de puertas y los colores.
#4-Al final se pregunta si hay otro cliente o no, si hay otro cliente, entonces vuelve a preguntar todo.
#5-Si la cantidad de clientes fue:
#--5.1: 0 a 5 personas no hay descuento
#--5.2: 6 a 10 personas: hay un descuento del 10%
#--5.3: 11 a 50 personas: hay un descuento del 15%
#--5.4: Más de 50 personas: El descuento es del 18%
#6-Solo se va a mostrar que se vendió al final del programa



pedido = True
#Se crean listas vacias para ir añadiendo los datos insertados en cada iteración del "while"
count = [ ]
presu = [ ]
title = '\n\nLista de ventas:\n'

# Se piden los datos del presupuesto
while pedido == True:
    nombre = input('Introduzca su Nombre: ')
    apellidos = input('Introduzca su Apellidos: ')
    
    i = ['Ford', 'Chevrolet', 'Fiat']
    marca = ''
    # Se comprueba que los datos insertados son válidos
    while marca not in i:
        marca = input('Marca del vehículo a elegir: ' + str(i) + ': ')
    
    j = ['2', '4', '5']
    puertas = ''
    while puertas not in j:
        puertas = input('Número de puertas a elegir: ' + str(j) + ': ')
    
    k = ['Blanco', 'Azul', 'Negro']
    color = ''
    while color not in k:
        color = input('Color a elegir: ' + str(k) + ': ')
    
    presupuesto = 0 # Variable acomuladora
    # Se calcula el precio del vehículo
    if marca == 'Ford':
        presupuesto = presupuesto + 100000
    elif marca == 'Chevrolet':
        presupuesto = presupuesto + 120000
    elif marca == 'Fiat':
        presupuesto = presupuesto + 80000
    if puertas == '2':
        presupuesto = presupuesto + 50000
    elif puertas == '4':
        presupuesto = presupuesto + 65000
    elif puertas == '5':
        presupuesto = presupuesto + 78000
    if color == 'Blanco':
        presupuesto = presupuesto + 10000
    elif color == 'Azul':
        presupuesto = presupuesto + 20000
    elif color == 'Negro':
        presupuesto = presupuesto + 30000  
    
    # Se pregunta si hay que añadir un nuevo cliente
    n_cliente = input('¿Insertar nuevo presupuesto?: (S/N) ')
    if n_cliente == 'S':
        pedido = True
        if n_cliente != 'S':
            print('Por favor indique S ó N')
    elif n_cliente == 'N':
        pedido = False
     
    # Se añade el importe del presupuesto a la lista "count"
    count.append(presupuesto)
    
    # Se añaden los datos del presupuesto a la lista "presu"
    datos = 'La persona '+nombre +' '+apellidos + ' compró un vehículo marca '+ marca +' de ' + puertas + ' puertas y color ' + color
    presu.append(datos)


# Dependiendo del número de presupuestos, se realiza un descuento en el importe del vehículo
if len(count) <= 5:
    # Recorremos las listas por índices e imprimimos cada uno de ellos
    print(title)
    for x in range(0,len(count)):   
        presupuestos = count[x]
        print(str(presu[x]) + ' con un precio de ' + str(presupuestos) +'€. No se aplica descuento.')
elif len(count) >= 6 and len(count) <= 10:
    print(title)
    for x in range(0,len(count)):
        presupuestos = count[x]-(count[x]*0.1)
        print(str(presu[x]) + ' con un precio de ' + str(presupuestos) +'€. Se ha aplicado un descuento del 10%.')
elif len(count) > 10 and len(count) <= 50:
    print(title)
    for x in range(0,len(count)):
        presupuestos = count[x]-(count[x]*0.15)
        print(str(presu[x]) + ' con un precio de ' + str(presupuestos) +'€. Se ha aplicado un descuento del 15%.')
elif len(count) > 50:
    print(title)
    for x in range(0,len(count)):
        presupuestos = count[x]-(count[x]*0.18)
        print(str(presu[x]) + ' con un precio de ' + str(presupuestos) +'€. Se ha aplicado un descuento del 18%.')
        
        