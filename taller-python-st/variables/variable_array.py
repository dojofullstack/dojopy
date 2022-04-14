# variable tipo lista o array

lista_judadores = ['henry', 'stefany', 'dojopy', 'python', 1, 5]
lista_juegos = ['pinball', 'sudoku', 10]
# print(lista_judadores)
# print(type(lista_judadores))
# print(lista_judadores[-1])
# print(lista_judadores[1: -1])

print(dir(lista_judadores))
lista_judadores.append('pablo')
lista_judadores.reverse()
lista_judadores.remove('python')

print(lista_judadores)
lista_judadores.pop(2)
print(lista_judadores)

# lista_judadores = []
# lista_judadores.clear()
lista_judadores.extend(lista_juegos)
print(lista_judadores)
# lista_judadores.sort()
print(lista_judadores)
print(len(lista_judadores))

# new_lista_judadores = lista_judadores.copy()