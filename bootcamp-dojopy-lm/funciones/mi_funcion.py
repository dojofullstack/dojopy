
planeta = 'marte'

def programar():
    print(planeta)
    planeta2 = '124'
    # print(unviseral)
    while True:
        name =  input('¿Cual es tu nombre?')
        print(name)
        break
        # if name == 'Elon Musk':
        #     print('genial!')
        #     break
        # else:
        #     print('sigue intentando ;D')

def emprender(project, marketing):
    if project == 'ecommerce':
        # print('tienda online!')
        return f'tienda online! {marketing}'
    else:
        # print('super!')
        return False



emprendimiento = emprender(marketing=False, project='ecommerce')
print(emprendimiento)


def emprender_2022(*args):
    print(args)
# emprender_2022('ecommerce', 'academia')

def emprender_2022(**Kwargs):
    # primer_item =  args[0]
    # segundo_item =  args[1]
    # print(primer_item)
    # print(Kwargs)
    # for item in Kwargs:
    #     print(Kwargs[item])

    for item in Kwargs.keys():
        print(item)

    print(Kwargs.values())


# emprender_2022(project='ecommerce', project2='academia')

def emprender_2022(project_name='ecommerce', project_time='6meses'):
    print(project_name)
    print(project_time)


emprender_2022('marketing', '3 meses')


# def main():
#     programar()
#     emprender()