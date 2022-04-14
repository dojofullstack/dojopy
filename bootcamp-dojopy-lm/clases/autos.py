

"""" definiendo Clase en Python """

""" manejando getters y setteres """

# class Credenciales():
#     def __init__(self):
#         self.__apikey = 'abcv'
    
#     @property
#     def apikey(self):
#         print('returnando apikey privado')
#         return self.__apikey

#     @apikey.setter
#     def apikey(self, new_apikey):
#         if len(new_apikey) > 3:
#             print('actualizando apikey')
#             self.__apikey = new_apikey

#     @apikey.deleter
#     def apikey(self):
#         del self.__apikey


# miapi =  Credenciales()
# print(miapi.apikey)
# miapi.apikey = 'xyzabc'
# print(miapi.apikey)
# del miapi.apikey
# print(miapi.apikey)



class Auto():
    # color = 'rojo'
    # velocidad = '30km/h'
    # modelo = '22'

    def __init__(self, color, velocidad, modelo):
        self.color = color
        self.velocidad = velocidad
        self.modelo = modelo

    def frenar(self, maximo):
        self.metros = '10m'
        """ ejecutando metodo acelerar """
        self.acelerar()

        if maximo > 100:
            print('frenando')
            print(self.velocidad)
            print(self.metros)
            # print(self.__acelerando)

    def acelerar(self):
        self.__acelerando = 'go!'
        print(self.__acelerando)
        # if acelera:
        # print('acelerando!!')
        # print(self.metros)
        return 'nice'
    
    @property
    def precio_auto(self):
        if self.color == 'rojo' and self.modelo == 'tesla':
            # print('$50,000')
            return '$50,000'






# # auto_tesla = Auto('rojo', '45km/h', 'tesla')
# auto_tesla = Auto('verde', '95km/h', 'toyota')

# print(auto_tesla.color)
# print(auto_tesla.velocidad)
# print(auto_tesla.modelo)
# auto_tesla.modelo = 'tesla'
 
# print(auto_tesla.modelo)

# auto_tesla.frenar(200)
# print('atrib metros: ',auto_tesla.metros)

# print(auto_tesla.precio_auto)

# print('mi atrib metros; ',auto_tesla.metros)
# auto_tesla.metros = '50m'
# print('mi atrib metros; ',auto_tesla.metros)



# """ creando otra instance de mi clas Auto """

# auto_tesla = Auto()

# print(auto_tesla.color)
# print(auto_tesla.velocidad)
# print(auto_tesla.modelo)
# auto_tesla.modelo = 'toyota'
 
# print(auto_tesla.modelo)

# auto_tesla.frenar(200)
# print('atrib metros: ',auto_tesla.metros)

# print(auto_tesla.precio_auto)

# print('mi atrib metros; ',auto_tesla.metros)
# auto_tesla.metros = '50m'
# print('mi atrib metros; ',auto_tesla.metros)



class Planetas():
    def __init__(self, lunas, vida):
        self.lunas = lunas
        self.vida = vida

    def alienigena(self):
        if self.vida:
            print('genial hya vida', self.lunas)


class Galaxia(Planetas):
    def buscando_vida(self):
        print('buscando..')
        self.alienigena()
    
    def alienigena(self):
        print('hola aliens', self.lunas)


galaxia_oregon = Galaxia(15, True)
galaxia_oregon.buscando_vida()
galaxia_oregon.alienigena()


# planeta_desconocido = Planetas(10, True)
# planeta_desconocido.alienigena()


