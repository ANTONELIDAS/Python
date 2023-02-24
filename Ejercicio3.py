# 1-De dos numeros, saber cuál es el mayor.
# 2-Crear una variable numérica, y si está entre 0 y 10, mostrar un mensaje indicandolo. 
# 3-Añadir al anterior ejercicio, que si está entre 11 y 20, muestre un mensaje diferente, y
# si está entre 21 y 30, otro mensaje.

a, b = 9, 3
c = 33

if (a < b):
    print('A es menor que B')
if c >= 0 and c <= 10:
    print('C está entre 0 y 10')
elif c > 11 and c < 20:
    print('C está entre 11 y 20')
elif c > 21 and c < 30:
    print('Otro mensaje')
else:
    print('Im JesusChrist')


