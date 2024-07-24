'''
Ejercicio 17: Conversor de Millas a Kilómetros
Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo que 1 milla equivale a 1.60934 kilómetros.
'''

print('CONVERSOR DE MILLAS A KILÓMETROS')

Milles = float(input('Introduce la distancia en millas: ')) #Se pide introducir las millas a convertir y se almacena en la variable Milles

print(f'{Milles} milla equivale a {(Milles * 1.60934):.2f} kilometros') #se imprime el resultado de multimplicar millas x 1.60934

