from auto import Auto

# clases  en python
""" clases en python """

class Autodromo(Auto):
    def pista(self):
        self.pista_distancia = '100km'
        print(f'la pista tiene una distancia de {self.pista_distancia}')
        self.impulso('model laudy')
        print('desde la clase Autodromo', self.kilometraje)
        for value in range(self.galones):
            if value == 9:
                self.frenar()

    

class Autodromo2(Autodromo):
    def nueva_pista(self):
        print('new pista')
        # self.impulso('model laudy')



# auto_toyota = Auto()
# auto_toyota.velocidad = '200km'
# auto_toyota.kilometraje = 100
# auto_toyota.color = 'verde'
# auto_toyota.modelo = 'toyota'

# print(auto_toyota.kilometraje)
# print(auto_toyota.color)

# auto_laudy = Auto('100km', '150km', 'verde', 'laudy')
# auto_laudy.velocidad = '250km'
# auto_laudy.kilometraje = 140
# auto_laudy.color = 'rojo'
# print('atrib publico',auto_laudy.kilometraje )
# auto_laudy.impulso('laudy')
# print(auto_laudy.__precio)
# auto_laudy.frenar()
# auto_laudy.acelerar()


# obj_autodromo = Autodromo('100km', '150km', 'verde', 'laudy')
# obj_autodromo.pista()
# obj_autodromo.frenar()
# print(obj_autodromo.capacidad)


obj_hernecia_multi_nivel = Autodromo2('100km', '150km', 'verde', 'laudy')
obj_hernecia_multi_nivel.nueva_pista()
obj_hernecia_multi_nivel.pista()