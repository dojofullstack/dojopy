
# condiciones

is_offer = False
username = 'fabian'


if len(username) > 5 and username.islower() or username.isdigit():
    print('es valido :D')
else:
    print('no es valido')


print('###'*50)
if len(username) > 10:
    # print('es mayo a 10')
    pass
elif not username.islower():
    print('es minus')
elif username.isdigit():
    print('digitos')
elif username == 'fabian':
    print('es fabian')
else:
    print('ninguna se cumplio')


try:
    if username == 'fabian':
        print('hola fabian')
    else:
        print('no fabian')
except TypeError as t:
    print('tipor de error', t)
except Exception as e:
    print(e)
finally:
    print('proceso finalizado')



if __name__ == '__main__':
    print('modulo principal')