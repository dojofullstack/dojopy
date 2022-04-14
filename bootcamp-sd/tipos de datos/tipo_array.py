
# tipo de dato arrray

list_users = ['henry' , 'pedro', 'aldo', 'sebastian', 'aldo']
new_users =  ['jhon', 'kevin']
new_users = []

print(list_users)
print(type(list_users))


conversion = list('dojopy')
print(conversion)
print(dir(list_users))
list_users.append('eric')
print(list_users)
list_users.extend(new_users)
print(list_users)

list_users.remove('pedro')
print(list_users)

list_users.insert(0, 'body')
print(list_users)

list_users.pop(1)
print(list_users)


print(len(list_users))