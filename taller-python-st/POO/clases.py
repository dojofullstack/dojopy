
class Autos:
    velocidad = ''
    color = ''
    year = ''
    model = ''


class AutosFull:
    def __init__(self, velocidad, color, year, model):
        self.velocidad = velocidad
        self.color = color
        self.year = year
        self.model = model
        self.__costo = '$10000'
        print('iniciando contructor de la clase')
    
    def acelerar(self, nitro=False):
        print(self.__costo)
        self.kilometraje = ''
        print('metodo acelerar')
        print(self.velocidad)
        if nitro:
            print('acelar x10')
        
        self.detener()
    
    def detener(self):
        print('se detiene el auto')



class AutoDromo(AutosFull):
    def carrera(self):
        ticket = '10$'
        print('carrera')
        print(self.color, self.model)
        self.year = '2021'
        self.acelerar(True)
        self.detener()
        print(ticket)



obj = AutoDromo('100km/h', 'rojo', '2000', 'tesla')
obj.carrera()
# print(obj.ticket)


# auto_tesla = Autos()
# print(auto_tesla.velocidad)
# print(auto_tesla.model)
# auto_tesla.velocidad = '100km/h'
# auto_tesla.model = 'tesla'
# auto_tesla.color = 'rojo'

# print(auto_tesla.velocidad)
# print(auto_tesla.model)
# print(auto_tesla.color)

# auto_tesla = AutosFull('100km/h', 'rojo', '2000', 'tesla')
# print(auto_tesla)
# auto_tesla.velocidad = '100km/h'
# auto_tesla.model = 'tesla'
# auto_tesla.color = 'rojo'
# print(auto_tesla.velocidad)
# print(auto_tesla.model)
# print(auto_tesla.color)
# # print(auto_tesla.__costo)
# auto_tesla.acelerar(True)