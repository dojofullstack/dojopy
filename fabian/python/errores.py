try:
    print(number_users + 10)
    print(10/5)
    print(fabain)
except TypeError:
    print('no puedes operar tipo string con numeral')
    print('tienes el error del tipo TypeError')
except ZeroDivisionError:
    print('no peudes diviri entre cero')
except Exception as e:
    print('otro error')
    print(e)
