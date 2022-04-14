""" entradad y salida de datos """
import sys
import argparse as args

# name =  input('¿cual es tu nombre?')
# print(name)

# print(sys.argv)
# if len(sys.argv) == 3:
#     name = sys.argv[1]
#     lastname = sys.argv[2]
#     print('nombre:', name.upper())
#     print('apellido:', lastname.upper())
# else:
#     print('ingresa el nombre y apellido')


parser = args.ArgumentParser(description='Calculadora, suma/resta/multiplica a y b')
parser.add_argument('-x', '--numero_a', type=int, help='Parámetro a')
parser.add_argument('-y', '--numero_b', type=int, help='Parámetro b')
parser.add_argument('-z', '--operacion',
                    type=str,
                    choices=['suma', 'resta', 'multiplicar'],
                    default='suma', required=False,
                    help='Operación a realizar con a y b')

args = parser.parse_args()
print(args)

if args.operacion == 'suma':
    print(args.numero_a + args.numero_b)
elif args.operacion == 'resta':
    print(args.numero_a - args.numero_b)
elif args.operacion == 'multiplicar':
    print(args.numero_a * args.numero_b)