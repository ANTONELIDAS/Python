# 1-Mostrar con un 'while' los números del 1 al 100.
# 2-Mostrar con un 'for' los números del 1 al 100.
# 3-Mostrar los caracteres de la cadena 'Hola mundo'.
# 4-Mostrar los números pares entre 1 al 100.

'''
#1- Con While
my_condition = 1

while (my_condition <= 100):
    print(my_condition)
    my_condition+=1
print('Fin del bucle con while')


#2- Con for
my_condition = 1

for my_condition in range(1, 101):
    print(my_condition)
print('Fin del bucle con for')
'''

#3- 
for my_condition in 'Hola mundo':
    print(my_condition)


#4-
for my_condition in range(2, 101, 2): #Empieza en 2, termina en 100 porque es exluyente, y va de 2 en 2.
    print(my_condition)
