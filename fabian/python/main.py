
import json
import control_flujos 

# tipos de datos en Python

""" tipos de datos string  """


username = 'henry men'

print(username)

#print(dir(username))

print(username.upper())
print(username.lower())

username = username.replace('henry', 'erick')
print(username)

print('join')
username2 = ' fabian '
print(username2.join(['me', 'hola']))

#me fabian hola

print(username2.islower())

data = 10

data2 = str(data)
print(type(data2))


movie = ' spiderman'
movie2 = movie

print(movie2.strip())

# email = ''
# email = str()

##########################################

""" tipo de dato numerico """
# int() float()
number_users =  10
price = 10.5
print(type(number_users))
print(type(price))

print(number_users + 20)
print(price / 2)
print(price // 2)


################################

""" tipo de dato array o lista """

# list()

autos = ['audy', 'renol', 'mazda', 'tesla']

print(autos)
print(dir(autos))
print(autos.pop(0))

autos.append('volsagen')

autos.remove('renol')

print(autos)


autos_copia = autos.copy()
print(autos_copia ,'line 72')
print(autos_copia.pop(0))
print(autos_copia)

print(autos)

print(list('fabian'))
# """ tipo de dato diccionario """"


""" tipo de tupla """
tokens = ('andhd123', 'user@gmail.com')
print(type(tokens))
print(tuple(['a', 'b']))


print(""" Tipo de dato booleano """)
# puder tomar los valores True o False

is_user_new = False
print(is_user_new)
print(type(is_user_new))

print(is_user_new + 2)



# tipo de dato diccionarios
Cv = {
    'experiencia': '5 years'
}

perfil = {
            'user': 'fabian',
            'email': 'fab@gmail.com',
            'age': 18,
            'is_admin': True,
        }

print(perfil)
print(type(perfil))


# parseo de Python a Json
# data = json.dumps(perfil, indent=4)
# # print(data)


# # parseo de Json  a Python
# filedata = open('dataDB.json').read()

# data = json.loads(filedata)
# print(data.get('stacks'))

print(perfil['user'])
print(perfil.get('user2', 'no existe'))


print('modulo continua')

# print(dir(perfil))

print(perfil.keys())


print(perfil.update(Cv))
print(perfil)

# conjuntos

languajes = {'python', 'javascript', 'kotlin', 'python', 12, True }

print(languajes)
print(type(languajes))
print(dir(languajes))

languajes.add('C++')
print(languajes)

languajes.remove('kotlin')
print(languajes)

print(languajes.intersection({'python', 'scala'}))



