'''
Ejercicio 5: Suma de Números Pares
Escribe un programa que calcule la suma de todos los números pares del 1 al 100.
'''

Suma = 0

i = 2

while i < 101:
  if i % 2 > 0 :
    Suma += i
  
  i += 1
  
print(f'La suma de todos los números pares del 1 al 100 es : {Suma}')
    
#Alternativa
Suma = 0
i = 2

while i < 101:
  Suma += i
  i += 2
  
print(f'La suma de todos los números pares del 1 al 100 es : {Suma}')         