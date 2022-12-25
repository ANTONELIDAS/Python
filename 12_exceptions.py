### Excepciones ### Manejo de errores

numberOne = 5
numberTwo = 1
numberTwo = '1'

# Try except

try:
    print(numberOne + numberTwo)
    print('No se ha producido error')
except:
    print('Se ha producido un error')


# try except else finally

try:
    print(numberOne + numberTwo)
    print('No se ha producido error')

except:
    # Se ejecuta si se produce una excepción. 
    print('Se ha producido un error')
else:
    # Se ejecuta si no se produce una excepción.
    print('La ejecución continúa correctamente')
finally: # Opcional.
    # Se ejecuta siempre.
    print('La ejecución continúa')


# Excepciones por tipo.

try:
    print(numberOne + numberTwo)
    print('No se ha producido error')
except ValueError:
    print('Se ha producido un ValueError')
except TypeError:
    print('Se ha producido un TypeError')


# Captura de la información de la excepción.

try:
    print(numberOne + numberTwo)
    print('No se ha producido error')
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
