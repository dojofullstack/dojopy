"""
DIA 1"""
"""
#Comentario para probar

#Imprimr mensaje
print('hola mundo')


#Tipos de datos en python

#Tipo de dato String 'hola mundo' str()
#tipo de dato Numeral: (int o float) 10, 10.5 int() float()
#Tipo de dato array o listas: ['python', 'javascript'] list()
#Tipo de dato booleano: True/False bool()
#Tipo de dato Diccionario: {'usuario': 'henry', 'email':'hola@dojopy.com'} dict()
#Tipo de dato conjunto o set :{'c++', 'java'}
#Tipo de dato tupla o tuple: ('pablo', 'rosa')

#Tipo de dato string

mystack='python'

type(mystack) 

#Imprimr uppercase
print(mystack.upper())
print(mystack.lower())
print(mystack.replace('py', '00'))
print(mystack.find(('thon')))
print(mystack.isnumeric())

conversion_string=str(12)
print(type(conversion_string))
"""

#DIA 2
"""TIPO DE DATO STRING"""
username_new="pedro"

"""tipo de dato array o lista"""
list_tareas=['Aprender python','aprender javascript', 100]
#imprimir la lista
print(len(list_tareas))
print('mi lista tiene: ',len(list_tareas),' elementos')
print (f'mi lista tiene{len(list_tareas)} elementos')
print(type(list_tareas))
print(dir(list_tareas))
list_tareas.append('aprender React Native')

print(list_tareas)

list_tareas.insert(1, 'aprender Django')

print(list_tareas)

print(list_tareas[0])

#Imprimir nombre
mi_nombre='moises'
print(list(mi_nombre))

#Datos booleanos
activo=True

print(activo)
print(type(activo))
print(not activo)

#DICT
perfil_usuario={
    'nombre':'hola',

}