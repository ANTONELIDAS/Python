### Dictionaries ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {'Nombre':'Anto', 'Apellido':'Pao', 'Edad':31, 1:'Python'} # Relación clave-valor. Estructura similar json. No-SQL
my_dict = {
    'Nombre':'Anto', 
    'Apellido':'Pao', 
    'Edad':31, 
    'Lenguajes':{'Python', 'Swift', 'Kotlin'} # Varios valores almacenados en una misma clave. 
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))

print(my_dict['Edad'])

my_dict['Nombre'] = 'Pedro' # Reemplaza valor.
print(my_dict['Nombre'])

my_dict['Calle'] = 'Calle Anto' # Agrega un nuevo campo al diccionario. 
print(my_dict)

del my_dict['Calle'] # Eliminar un solo elemento en el diccionario. 
print(my_dict)

print('Pedro' in my_dict) # Error
print('Nombre' in my_dict) # Busca por clave, no por valor. 

print(my_dict.items()) # Un listado con cada uno de los items. 
print(my_dict.keys()) # Un listado de las claves. 
print(my_dict.values()) # Un listado de los valores. 

my_new_dict = my_other_dict.fromkeys(('Nombre', 1, 'Piso')) # Solo crea claves de un dicc existente, pero vacías. Te permite agregar claves también. 
print(my_new_dict)

my_new_dict['Nombre'] = 'Pepa' # Agregar valores al nuevo diccionario. 
my_new_dict[1] = -3333
my_new_dict['Piso'] = 3333

print(my_new_dict)






