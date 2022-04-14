
# variable dict o diccionario

usuario = {
    'nombre': 'stefany',
    'skill': 'python'
}

pais = {
    'country': 'colombia'
}

print(usuario)
print(type(usuario))
print(len(usuario))

# print(dir(usuario))
# print(usuario['1skill'])
print(usuario.get('1skill'))
print(usuario.items())
print(usuario.keys())
print(usuario.values())
print(usuario.pop('skill'))
usuario.update(pais)
print(usuario)

# usuario['nombre'] = 'pepe'
# print(usuario)

new_usuario = usuario.copy()

new_usuario['nombre'] = 'erick'
print(new_usuario)
print(usuario)