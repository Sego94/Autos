#Se crea una función para realizar el cálculo del precio
def calcular_precio(marca, puerta, color, venta):
    marcas = {'ford': 100000, 'chevrolet': 120000, 'fiat': 80000}
    colores = {'blanco': 10000, 'azul': 20000, 'negro': 30000}
    puertas = {2: 50000, 4: 65000, 5: 78000}
    precio = marcas[marca] + colores[color] + puertas[puerta]
    if venta >5 and venta <11:
        precio = precio*0.9
    if venta >10 and venta <51:
        precio = precio*0.85
    if venta >50:
        precio = precio*0.82
    return precio


#Se crea un bucle preguntándo si hay más clientes
mas_clientes = 'si'
ventas = []
marcas = ['ford', 'chevrolet', 'fiat']
puertas = [2, 4, 5]
colores = ['blanco', 'azul', 'negro']

while mas_clientes == 'si':
    nombre = input('Igrese nombre: ')
    apellido = input('Ingrese apellido: ')
    marca = ''
    puerta = 0
    color = ''
    #Se comprueba si la marca introducida es correcta
    while marca not in marcas:
        marca = input('Ingrese marca: ')
        marca = marca.lower()
    #Se comprueba si el número de puertas introducido es correcto
    while puerta not in puertas:
        puerta = int(input('Ingrese número de puertas: '))
    #Se comprueba si el color introducido es correcto
    while color not in colores:
        color = input('Ingrese color: ')
        color = color.lower()
    #Los datos de cada bucle se van añadiendo a la lista ventas
    ventas.append({'nombre': nombre, 'apellido': apellido, 'marca': marca, 'puertas': puerta, 'color': color})
    mas_clientes = input('¿Hay más clientes?: ')


venta = len(ventas)
for i in ventas:
    precio = calcular_precio(i['marca'], i['puertas'], i['color'], venta)
    print('La persona '+i['nombre'] +' '+i['apellido'] + ' compró un auto marca '+ i['marca'] +' de ' + str(i['puertas']) + ' puertas y color ' + i['color'] + ' con un precio de ' +str(precio) + '€')


