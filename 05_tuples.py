### Tuplas ### Conjunto de valores. != de lista

my_tuple = tuple()
my_other_tuple = (30, 60, 70)

my_tuple = (31, 1.60, 'Antonella', 'Pao')
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count('Antonella'))
print(my_tuple.index('Antonella'))

# my_tuple[1] = 1.70  Una tupla es inmutable. Los datos que se tienen no se pueden modificar. 

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

del my_tuple # Del, palabra reservada del sistema que borra todo. 
# print(my_tuple)  La variable no está definida, por eso da error. 






