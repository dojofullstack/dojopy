
# tipo de dato diccionario

credenciales = {
    'username': 'henry',
    'password': 'xyz',
    'email': 'hola@dojopy.com',
    'coins': 10
}


print(credenciales)
print(type(credenciales))
print(dir(credenciales))

print(credenciales.get('email', ''))
print('continuando programa')


credenciales['adddress'] = 'Perú/Lima'
print(credenciales)

print(credenciales.values())


credenciales.update({'type_user': 'admin', 'rol': 'signer'})

print(credenciales)

companies = [
                ['ubber', 'ubeapp'],
                ['facebook', 'facebookapp'],
                ['rappi', 'rappiAPP']
            ]
print(dict(companies))