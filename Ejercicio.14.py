'''
Ejercicio 14: Calculadora de Descuento
Crea un programa que calcule el precio final de un artículo después de aplicar un descuento del 20%.
'''
print ('CÁLCULO DE DESCUENTO DEL 20%')

Price = float(input('Introduce el precio: ')) #Se solicita el precio y se almacena en la variable "Price"

print(f'El precio final es {(Price - (Price * 0.2)):.2f}') #Se imprime el resultado de restar el 20% al precio inicial y se redondea a dos decimales

