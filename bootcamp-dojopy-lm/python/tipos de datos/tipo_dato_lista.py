
# tipo de dato lista

mis_lenguajes = ['python', 'javacript]

print(mis_lenguajes)
print(type(mis_lenguajes))
# print(dir(mis_lenguajes))

mis_lenguajes.append('cobol')
mis_lenguajes.append('ruby')
print(mis_lenguajes)
mis_lenguajes.remove('ruby')
print(mis_lenguajes)

mis_lenguajes.pop()
print(mis_lenguajes)
mis_lenguajes.pop(0)
print(mis_lenguajes)

mis_lenguajes.reverse()

print(mis_lenguajes)

mis_lenguajes2 = mis_lenguajes.copy()
