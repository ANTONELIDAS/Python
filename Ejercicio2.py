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
pepa = valor_producto * valor_iva
pepe = (valor_producto * valor_iva) + valor_producto

print('el precio del IVA es de', pepa)
print('el precio total es de', pepe)

# Para no hacer tantas variables? Sino sería:

precio_iva = valor_producto * valor_iva
print('el precio total es de', precio_iva + valor_producto)



valorProd = 20767656567
valorIva = 0.21
valorProdIva = valorProd * 1.21

print(f'valor con iva {valorProdIva}')
print(f'Porcentaje de Iva {valorProd * valorIva}')


def prod_venta(producto, iva):
    valor_producto = producto
    valor_iva = iva
    pepe = (valor_producto * valor_iva) + valor_producto
    return pepe

print(prod_venta(100, 0.21))
print(prod_venta(200, 0.21))
print(prod_venta(300, 0.21))
print(prod_venta(400, 0.21))

print(prod_venta(500, 0.21))

una_pepe = prod_venta(500, 0.21)
cosa = 1

ppppppp = una_pepe + cosa
print(ppppppp + 1)

