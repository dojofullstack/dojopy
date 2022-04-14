import time
""" iteradores """

# For 
products = ['appel', 'xiamoi', 'samsung', 'lg']
products_sin_stock = []




for item in products:
    print(item)
    # if len(products_sin_stock) < 2:
    #     products_sin_stock.append(item)

    if 'appel' in products:
        print('si stock')
        products_sin_stock.append('appel')
    
    if len(products_sin_stock) == 2:
        print('saliendo del bucle for')
        break

# numeros = range(1, 100)

for item in [1, 2, 3]:
    if item % 2 == 1:
        print(item, 'es par')


print(products_sin_stock)



elementos = [ item for item in range(1, 100) if item % 2 == 0 ]

print(elementos)



""" bucle While """

cont = 0
estado = 20

while estado:
    time.sleep(0.5)
    print('hola')
    estado += 1
