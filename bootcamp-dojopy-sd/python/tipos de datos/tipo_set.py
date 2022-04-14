
# tipo de dato set

mi_conjunto_acciones = {'amazon', 'google', 'netflix', 'amazon', 'rappi'}

print(mi_conjunto_acciones)
print(type(mi_conjunto_acciones))

emails = ['pepe@gmail.com', 'michell@gmail.com', 'pepe@gmail.com']
print(set(emails))

print('amazon' in mi_conjunto_acciones)

print(dir(mi_conjunto_acciones))

mi_conjunto_acciones.add('xiaomi')
# print(mi_conjunto_acciones.pop())
mi_conjunto_acciones.remove('google')
print(mi_conjunto_acciones.union({'1', '2'}))
print(mi_conjunto_acciones.intersection({'amazon', 'xiaomi'}))
