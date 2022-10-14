### Sets ### 

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un 'diccionario'.

my_other_set = {'Anto', 'Paoloni', 31} # Le agrego datos y cambia a 'Set'.
print(type(my_other_set)) 

print(len(my_other_set))

my_other_set.add('apaoloni')
print(my_other_set) # Un set no es una estructura ordenada. 

my_other_set.add('apaoloni')
print(my_other_set) # Un set no admite repetidos. 

print('Anto' in my_other_set) # Busqueda. 
print('Anti' in my_other_set)

my_other_set.remove('Anto')
print(my_other_set)

my_other_set.clear() # Vacía los elementos del set, pero sigue existiendo. 
print(len(my_other_set))

del my_other_set # Este elimina por completo un objeto, y el print da error. 
# print(my_other_set)

my_set = {'Anto', 'Paoloni', 31}
my_list = list(my_set) # Cambiarlo a list no garantiza sabre el orden, porque originariamente fue un set.
print(my_list)
print(my_list[0])

my_other_set = {'Kotlin', 'Swift', 'Python'}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({'JavaScript', 'C#'})) # Los 2 primeros union los ignora porque se repiten los datos.

print(my_new_set.difference(my_set))


