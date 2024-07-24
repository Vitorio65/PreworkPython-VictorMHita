'''
Ejercicio 3: Verificación de Edad
Escribe un programa que solicite la edad de un usuario y determine si es mayor de edad (mayor o igual a 18 años) o no.
'''
print ('VERIFICAR MAYORÍA DE EDAD')

Age = int(input('Introduce la edad: ')) #se solicita la edad y se almacena en al variable Age

if Age >= 18: # condicional para ver si la edad introcida en Age es menor; o mayor o igual a 18
  print('Es mayor o igual de 18 años') #Si el valor de Age es mayor o igual a 18, se imprime el texto
else:
  print ('No es mayor o igual de 18 años') #Si no, se imprime el texto