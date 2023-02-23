
my_condition = input('Ingresar la nota: ')
my_condition = int(my_condition)
if my_condition == 10: 
    print('Excelente')

elif my_condition > 7 and my_condition < 10:
    print('Muy bien')
elif my_condition > 5 and my_condition < 8:
    print('Bien')
elif my_condition > 3 and my_condition < 6:
    print('La nota es : Satisfactorio')
else:
    print('No satisfactorio')


