### Lists ### Guarda datos 

from ipaddress import summarize_address_range
from unicodedata import name


my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [31, 1.60, 'Anto', 'Pao']
print(my_other_list)

print(type(my_other_list))

print(my_other_list[0]) # Puedo traer determinado dato dentro de la lista.
print(my_other_list[1])  
print(my_other_list[-1]) 
print(my_other_list[-4])  
# print(my_other_list[-5]) # Da error porque la lista solo tiene 4 datos dentro. 
print(my_list.count(30))  

age, height, name, surname = my_other_list
print(age)

print(my_list + my_other_list)

#my_list = 'Hola Python' # Lenguaje de Tipado dinamico.
print(my_list)

my_other_list.append('Panadería') # Agrega datos a la lista. 
print(my_other_list)

my_other_list.insert(1, 'Azul') # Agrega dato en la posición indicada. 
print(my_other_list)

my_other_list.remove('Azul')

print(my_list)
print(my_list.pop()) # Saca el último dato por defecto.
print(my_list)

del my_list[2] # Elimina el dato especificado. 
print(my_list)

print('--------------------------------')
my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort() # Ordena de menor a mayor por defecto. 
print(my_new_list)

print(my_new_list[1:2]) # Muestra el elemento entre 1 y 2.






