### Loops ### (bucles/ciclo) Iterar: pasar por el mismo código una y otra vez. 

# While - Esta atado a cumplir una condicion

from turtle import goto


my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:
    print('Mi condición es mayor o igual que 10')

print('La ejecución continúa')

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print('Se detiene la ejecución')
        break # frena el bucle
    
    print(my_condition)

print('La ejecución continúa')

## For ## Para iterar un listado de elementos. Atado a cuantos elementos posee. 

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (31, 1.60, 'Antonella', 'Pao')
for element in my_tuple:
    print(element)

my_set = {'Kotlin', 'Swift', 'Python'}
for element in my_set:
    print(element)

my_dict = {'Nombre':'Anto', 'Apellido':'Pao', 'Edad':31, 1:'Python'}
for element in my_dict: 
    print(element)
    if element == 'Edad':
        continue
else:
    print('El bucle for para diccionario ha finalziado')






