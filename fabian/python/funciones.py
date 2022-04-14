import random

datos = None



def agregar_productos(**kwargs):
    productos = []
    print('hola fabian')
    for i in 'fabian':
        print(i)
        productos.append(i)
    
    # for i in productos_sin_stock:
    #     print(i)
    # print(productos_oferta)
    # print(productos)
    # for k in args:
    #     print(args.get(k))
    print(kwargs.keys())
    print(kwargs.values())
    return kwargs.keys()



items_no_stock = ['azucar', 'arroz']
productos_oferta = ['cereal', 'keke']
# agregar_productos()
# agregar_productos(
#                     productos_oferta=productos_oferta,
#                     productos_sin_stock=items_no_stock
#                 )


def agregar_productos_nuevos(*args):
    print(args)


# agregar_productos_nuevos('iphone', 1, True, ['hola', 'broo'] )


def saludar(saludo):
    print(saludo.upper())
    return saludo.upper()

# data =  saludar('hola Fab')
# print('data de la funcion: ',data)


# saludar = lambda saludo, despedida: saludo.upper() + despedida.lower()

# print(saludar('hola Fab', 'sayonara'))


valor_dado = 0
dado = [1, 2, 3, 4, 5, 6]
puntos = 0
ganador_puntos = 2


def lanzar_dado():
    valor_dado = random.choice(dado)
    return valor_dado

def leer_dado(valor):
    global puntos

    if valor >= 4:
        print('Genial sacaste 4, 5, o 6!')
        puntos += 1
    else:
        print('sacaste', valor, 'sigue intentanto')

def is_ganador():
    if ganador_puntos == puntos:
        print('game success!!')
        return True
    else:
        return False




def play_game():
    valor_dado = lanzar_dado()
    leer_dado(valor_dado)
    estado_gamer = is_ganador()
    return estado_gamer




if not play_game():
    while True:
        respuesta = input('¿Quiere interntar nuevamente?: ')
        if respuesta == 'si':
            estado_gamer = play_game()
            if estado_gamer:
                break
        else:
            print('listo nos vemos manana')
            break

else:
    print('vuelve pronto!')