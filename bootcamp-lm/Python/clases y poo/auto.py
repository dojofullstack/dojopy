
class Auto:
    # velocidad = ''
    # kilometraje = 0
    # color = ''
    # modelo = ''
        
    def __init__(self, velocidad, kilometraje, color, modelo):
        self.velocidad = velocidad
        self.kilometraje = kilometraje
        self.color = color
        self.modelo = modelo
        self.__precio = '10$'
        print('se crea el constructor de la clase Auto!')
        self.metodo_sin_vincular()

    def impulso(self, model):
        self.capacidad = []
        self.galones = 10
        self.power = 'nitro'
        self.modelo = model
        print(self.power)
        print(self.modelo)
        print(self.kilometraje)
        print(self.velocidad)
        print('el precio es de; ',self.__precio)
        # self.frenar()

    def acelerar(self):
        self.aceleracion = '5km'
        print(self.aceleracion)
        # self.impulso()

    def frenar(self):
        self.frenado = '159km'
        print('estamos frenando ',self.frenado)