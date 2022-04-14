

class Universo():
    black_holes = 'BlackX'

    def __init__(self, planetas, constelaciones):
        print('init Universo')
        self.planetas = planetas
        self.constelaciones = constelaciones
        self.__black_hole_destructor = 'BlakZ'
        # self.galaxias = galaxias
    
    def rotar_planetas(self, velocity, direction):
        # self.__crear_estrellas()

        if len(self.planetas) >= 2:
            print(f'rotar planetas')
            return f'rotar planetas'

    def numero_universos(self):
        self.number = 100
        print('hay infinitos universos')


    # def __crear_estrellas(self):
    #     self.start = 10000
    #     print('creando estrellas', self.start)
    

    @property
    def crear_estrellas(self):
        self.start = 10000
        # print('creando estrellas', self.start)
        return f'creando estrellas {self.start} {self.__black_hole_destructor}'
        # return self.__black_hole_destructor



    def __str__(self):
        if len(self.planetas) > 1:
            return 'agrega mas planetas'
        else:
            return 'planetas :D'




# planetas = ['marte', 'tierra']
# constelaciones = ['Capricornus', 'Aries']
# galaxias = ['via lactea', 'Andrómeda', 'Triángulo']

# universo1 = Universo(planetas, constelaciones)

# # print(universo1.planetas)
# universo1.planetas = ['saturno', 'mercurio']

# # print(universo1.planetas)


# print(universo1.planetas)
# # print(universo1.black_hole_destructor)
# universo1.rotar_planetas('29km/h', 'derecha')

# # universo1.crear_estrellas()
# print(universo1.crear_estrellas)



class Planeta(Universo):
    
    def __init__(self):
        self.vida = True
        self.oxigeno = True
        self.nitrogeno = True
        self.velocity = '29km/s'
        # Universo.__init__(self, ['marte', 'tierra'], ['Capricornus', 'Aries'])

    def main(self):
        print('ejecutando metodo main')
        # self.rotar_planetas('10km/m', 'inzquierda')
        self.numero_universos()
        print(self.black_holes)


planeta_tierra =  Planeta()
print(planeta_tierra.velocity)
planeta_tierra.main()