'''
Ejercicio 18: Contador de Palabras
Ejercicios Introducción a Python: Enunciados 3
Crea un programa que cuente la cantidad de palabras en una oración ingresada por el usuario.
'''
Texto = str(input('Introduce un texto: '))


print(f'El número de palabras introducidas es {len(Texto.split())}') #se separan las palabre de "Texto" con la función split; y el resultado see cuenta con len


