
misLenguajes = False
experience_year = 5
movies = ['spiderman', 'batman']

# [] # esto es falso
# '' # esto es falso
# {} # es falso
# () #es falso
# 0 # es falso

if misLenguajes or experience_year > 4:
    print('hola dev!')

if misLenguajes and experience_year > 4:
    print('hola coder!')

if not misLenguajes:
    print('usanto operador de negacino!')    

if movies:
    print('mis pelis favoritas')


if len(movies) >= 2:
    print('mis pelis favoritas mas de 2')
else:
    print('agrega mas pelis')



if len(movies) == 1:
    print('mis pelis favoritas mas de 2')
elif movies[0] == 'spiderman':
    print('genial viste spiderman')
elif 'spiderman' in movies:
    print('genial viste spiderman x2')
else:
    print(':D')

#false or false and false
# false and false
# false

if experience_year > 4 and len(movies) > 2 or 'harryPotter' in movies and not experience_year % 2:
    print('se cumplio!')
else:
    print('no se cumple')
