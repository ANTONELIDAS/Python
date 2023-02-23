# 1-Imprimir Hola Mundo por pantalla.
# 2-Crear dos variables numéricas, sumarlas y mostrar el resultado.
# 3-Mostrar el precio del IVA de un producto de valor 100, y su precio final.

#1
print('Hola Mundo')

#2
primer_numero = 3
segundo_numero = 5
print('resultado', 3+5)

# O también 

suma = primer_numero + segundo_numero
print('resultado', suma)

#3
valor_producto = 100
valor_iva = 0.21

print('el precio del IVA es de', 100 * 0.21)
print('el precio total es de', (100 * 0.21) + 100)

# Para no hacer tantas variables? Sino sería:

precio_iva = valor_producto * valor_iva
print('el precio total es de', precio_iva + valor_producto)

