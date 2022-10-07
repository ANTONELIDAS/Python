# Variables.

from ctypes import addressof
from sunau import _sunau_params
from tkinter import N


my_string_variable = 'My String Variable'
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenacion de variables en un print.
type(print(my_string_variable, my_int_variable, my_bool_variable))
print('Este es mi valor de:', my_bool_variable)

# (algunas)Funciones del sistema. 
print(len(my_string_variable))

# Variables en una sola línea. Ten cuidao.
name, surname, alias, age = 'antonella', 'poloni', 'anto', 25
print(name, age, 'mi alias es:', alias, surname)

# Inputs
'''
name = input('What is your name: ')
age = input('How old are you! ')

print('My name is:', name)
print('I am', age, 'years old')
'''

# Cambiamos su tipo
name = 23
age = 'anto'
print(name)
print(age)

# Forzamos el tipo. Not really.
address: str = 'Mi dirección'
address = 32
print(address)
