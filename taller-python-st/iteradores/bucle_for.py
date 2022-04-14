
lista_usuarios = ['stefany', 'henry', 'erick']

result = []
for index, item in enumerate(lista_usuarios):
    try:
        # print(index, item)
        result.append({'indice': index, 'user': item})
    except:
        pass
print(result)

# lista comprimida
result2 = [
    {'indice': index, 'user': item}
    for index, item in enumerate(lista_usuarios)
    if index >= 1
    ]

print(result2) 
