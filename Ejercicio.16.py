'''
Ejercicio 16: Contador de Números Pares e Impares
Crea un programa que cuente y muestre la cantidad de números pares e impares en una lista ingresada por el usuario
'''
print ('CONTADOR DE PARES E IMPARES')

Lista_pares = [] #se declara una variable lista para almacenar los números pares introducidos
Lista_impares = [] #se declara una variable lista para almacenar los números impares introducidos

Pares = 0 #se declara una variable interger ir contanto los números pares introducidos
Impares = 0 #se declara una variable interger ir contanto los números pares introducidos

Número = 1 #se declara una variable interger que será el campo de entrada de los números. se incia con valor 1 para que entre en el bucle

while Número != 0: #se crea un bucle que estará ejencutandose hasta el número elegido sea un 0 y se terminar la introducción
    Número = int(input('Introduce un número (Pulsa el número "0" para finalizar): '))
    if Número % 2 == 0 and Número != 0: #si el cociente es 0, es par y por tanto se cuenta 1 en la variable Pares y se añade a la lista de pares
      Pares += 1
      Lista_pares.append(Número)
    elif Número != 0:  #si no, es impar y por tanto se cuenta 1 en la variable Impares y se añade a la lista de impares
      Impares += 1
      Lista_impares.append(Número)
#se imprimen el numero de pares/impares introducidos siempres que el contardor sea mayor de 1 y por tanto se han introducido al menos un número par/impar, en caso que nos se muestra un texto indicando que no se han introducido números pares/impares
if Pares > 1:
  print(f'Los números pares introducidos son {Pares} y la lista es {Lista_pares}')

else:
  print('No se han introducido números pares')

if Impares > 1:
  print(f'Los números impares introducidos son {Impares} y la lista es {Lista_impares}')

else:
  print('No se han introducido números impares')

