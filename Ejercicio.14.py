'''
Ejercicio 14: Calculadora de Descuento
Crea un programa que calcule el precio final de un artículo después de aplicar un descuento del 20%.
'''
Price = float(input('Introduce el precio: ')) #Se solicita el precio y se almacena en la variable "Price"

print(f'El precio final es {(Price + (Price * 0.2)):.2f}') #Se imprime el resultado de sumar el 20% al precio inicial y se redondea a dos decimales

