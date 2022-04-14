
import json

# esto es un comentario en Python 
print('hola mundo'); 

""" tipo de datos en Python """

# String: 'hola mundo'
# Numeral (int o float): 10, 10.5
# Array o listas: ['python', 'javascript']
# Booleano: true/false
# Diccionario: {'usuario': 'henry', 'email': 'contacto@gmail.com'}
# Conjunto o set: ('c++', 'java')
# Tupla o tuple: ('pablo', 'rosa')

""" tipo de dato String """
mystack_favorito = 'python'

print(type(mystack_favorito))

print(dir(mystack_favorito))

print(mystack_favorito.upper())
print(mystack_favorito.lower())
print(mystack_favorito.replace('py','00'))
print(mystack_favorito.find('xyz'))
print(mystack_favorito.isnumeric())


conversion_string = str(12)

print(type(conversion_string))


# """" ARRAY O LISTA """
# lista_frutas  = ['manzana', 'naranja', 'uvas' ]

# print(type(lista_frutas))

# print(dir(lista_frutas))

# lista_frutas.append('cereza')

# print(lista_frutas)

# lista_frutas.insert(1, 'coco')

# print(lista_frutas)

# print(lista_frutas[0:2])

# lista_frutas.remove('naranja')

# print(lista_frutas)

# lista_verduras = ['zanahoria', 'brocoli']

# lista_frutas.extend(lista_verduras)

# print(lista_frutas)

# print(list('Dilva'))


# """" TIPO DE DATOS BOOLEANOS """

# is_active = True 

# print(is_active)
# print(type(is_active))
# print(bool(lista_frutas))

# print(is_active + 1)

""" TIPO DE DATO DICT """

perfil_usuario = {
    'nombre': 'Dilva',
    'email': 'dilva@gmail.com',
    'edad': '28',
    'lista_stack': [
        'python', 'react' ]
}

print(perfil_usuario['nombre'])

print(perfil_usuario.get('email', 'contacto@hotmail.com' ))

print(dir(perfil_usuario))

print(perfil_usuario.keys())

print(perfil_usuario.values())


print(perfil_user.items())


data_json = open('/home/henry/dojopy/bootcamp-lunes-miercoles/bootcamp-python/data.json').read()

data_product = json.loads(data_json)


print('data del JSON')
print(data_product[0].get('producto'))
print(data_product[1].get('precio'))


""" TIPO DE DATO SET O CONJUNTOS """

mis_lenguajes_favoritos = {'python', 'javascript', 'flutter', 'python'}

print(mis_lenguajes_favoritos)
print(type(mis_lenguajes_favoritos))
print(dir(mis_lenguajes_favoritos))
print(len(mis_lenguajes_favoritos))

mis_lenguajes_favoritos.add('reactJS')
print(mis_lenguajes_favoritos)
mis_lenguajes_favoritos.remove('flutter')
print(mis_lenguajes_favoritos)

lenguajes_bajo_nivel = {'C++', 'C', 'asembler'}
print(lenguajes_bajo_nivel)

mis_lenguajes_favoritos.update(lenguajes_bajo_nivel)
print(mis_lenguajes_favoritos)

print(mis_lenguajes_favoritos.intersection({'python', '.net'}))


""" TIPO DE DATOS TUPLAS """
#Son datos inmutables, no se pueden modificar. Ejemplo: token, contraseñas

credentials = ('0109291gyete', 'ppoi3736363')

print(credentials)
print(type(credentials))
print(dir(credentials))

print(credentials.index('ppoi3736363'))



