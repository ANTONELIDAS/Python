### Strings ###

my_string = 'My String'
my_other_string = 'My Other String'


print(len(my_string))
print(len(my_other_string))

print(my_string + '' + my_other_string)

my_new_line_string = 'Este es un String \ncon salto de línea'
print(my_new_line_string)

my_tab_string = '\tEste es un String con tabulación'
print(my_tab_string)

my_scape_string = '\\Este es un String \n escapado'
print(my_scape_string)

# Formateo

name, surname, age = 'Antonella', 'Pao', 31

print('Mi nombre es {} {} y mi edad es {}'.format(name, surname, age))
print('Mi nombre es %s %s y mi edad es %d' %(name, surname, age))

print('My name is', name, surname, 'and I am', age)
print(f'My name is {name} {surname} and I am {age}')

# Desempaquetado de caracteres 

language = 'python'
a, b, c, d, e, f = language
print(a)
print(b)

# División

language_slice = language[1:3]
print(language_slice)

language_slice = language[0:6:2] # Pilla todo y salta de 2 en 2.
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

# Reverse

reversed_language = language[::-1]
print(reversed_language)

# Funciones de Python

print(language.capitalize()) # Pone mayúscula, siempre a la primera.
print(language.upper()) # Todo en mayúsculas.
print(language.count('t')) # Cuenta las 't'.
print(language.isnumeric()) # Pregunta si es numérico. 
print('1'.isnumeric())
print(language.lower()) # Todo en minúsculas. 
print(language.upper().isupper()) # Pone mayúscula y pregunta si es mayúscula. 
print(language.startswith('py')) # Empieza con








