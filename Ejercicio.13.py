'''
Ejercicio 13: Verificación de Número Primo
Escribe un programa que determine si un número ingresado por el usuario es primo o no.
'''
print ('VERIFICADOR DE NÚMERO PRIMO')

Número = int(input('Introduce un número: ')) #Se solicita que introduzca un número enterero y se guarda en la variable "Número"
#Un número primo es aquel que sólo es divisible por 1 y por si mismo. Por tanto, en este caso se va a dividir por todos los números y si hay sólo dos resultado.

Counter = 0 #Se declara una variable a 0, dónde se irá contando las veces que el resto de la división es 0
i = 1 #Se declara una variable a 1 para generar un bucle desde 1 hasta el número introducido y que sirva a su vez de divisor

while i <= Número: #bucle desde 1 hasta el número introducido.
  if Número % i == 0: #si el resto de la división entre Número introcido y el valor del contador es = 0 se añade 1 al contador
    Counter += 1
  i += 1 #Se suma 1 al contador del bucle
if Counter == 2: #Si el contador es 2 (condición de número primo) se indica que es primo.
  print(f'El número {Número} es un número primo') 

else: #Si el contador es superior a 2, entonces es que el hay más de dos divisiones con resto = 0 y por tanto no es primo 
   print(f'El número {Número} no es un número primo')