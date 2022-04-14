# import sys
import json

# username = input('cual es tu nombre? ')
# edad = input('cual es tu edad?')
# edad = int(edad)
# print(username)
# print(edad)

# print('tu edad multiplicad x10 es: ', edad*10)

# print('Mi SDK')
# print('ingrese el nombre y seguido la edad')

# if len(sys.argv) != 3:
#     print('agrega los datos requeridos, por favor')

# print('tu nombre es: ',sys.argv[1])
# print('tu edad es: ', sys.argv[2])

# data = open('/home/henry/Downloads/credentials.txt')
# print(data.read())
# data.close()

# with open('/home/henry/Downloads/credentials.txt') as data:
#     datos = data.read()
#     print(datos.lower())

# CRUD CREATE, READ, UPDATE, DELETE

with open('./database.json') as data:
    datos = data.read()
    datos_formateado = json.loads(datos)
    print(type(datos_formateado))
    print(datos_formateado['password'])
    print(datos_formateado.get('passwordx', 'no existe'))
    datos_formateado['address'] = 'Peru/Lima'
    datos_formateado['mis_skills'] = {'python': 'django', 'javascript': 'reactJS'}
    print(datos_formateado)


with open('./database.json', 'w', encoding='utf-8') as data:
    json.dump(datos_formateado, data, indent=4)
