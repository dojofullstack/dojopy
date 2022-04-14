import time

is_login = True
lista_users = ['stefny', 'henry', 'erick']
# contador = 0

while lista_users:
    time.sleep(1)
    # contador += 1
    lista_users.pop()

    print('usuario inicio sesion')
    if len(lista_users) == 1:
        print('rompiendo while con break')
        break

print('saliendo del while')