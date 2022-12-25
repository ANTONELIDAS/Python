### CLASES ### 

class MyEmptyPerson:        #Los nombre de las clases se escriben en camel case.
    pass

print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias = 'Sin alias'):  #Esto no es una funcion, es un constructor de clase. Aca podemos establecer valores asociados a Persona.
        self.name = name #propiedad
        self.surname = surname #propiedad
        self.alias = alias

    def walk(self):
        print(f'{self.name} {self.surname} {self.alias} Está caminando')


my_person = Person('Anto', 'Pao')
print(my_person.name)
print(my_person.surname)
print(my_person.alias)
my_person.walk()

my_other_person = Person('Antonella', 'Pao', 'Sarasa')
print(my_other_person.name)
print(my_other_person.surname)
print(my_other_person.alias)
my_other_person.walk()

# Otra forma de lo mismo

class Person:
    def __init__(self, name, surname, alias = 'Sin alias'):
        self.full_name = f'{name} {surname} {alias}'

    def walk(self):
        print (f'{self.full_name} Está caminando')

my_person = Person('anto', 'paoloni')
print(my_person.full_name)
my_person.walk() 
