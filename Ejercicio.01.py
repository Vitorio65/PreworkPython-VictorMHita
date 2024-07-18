'''
Ejercicio 1: Conversor de Temperatura
Escribe un programa que convierta una temperatura de grados Celsius a grados
Fahrenheit.
'''
Temperature_C = int(input('Introduce la temperatura en grados Celsius: ')) #Solicita que se introduzca la temperatura en Celsius

Temperature_F = (Temperature_C*(9/5)+32) #Transforma la temperaruta de Celsius a Farenheit

print (f'La temperatura en Grados Fareheit es de {Temperature_F}') #imprime el resultado