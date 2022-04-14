import time

alarma = 15

# while alarma:
#     time.sleep(1)
#     print('iterando', alarma)
#     alarma -= 1


while True:
    name =  input('¿Cual es tu nombre?')
    print(name)
    if name == 'Elon Musk':
        print('genial!')
        break
    else:
        print('sigue intentando ;D')

print('siguiente ejecucion')


