'''
Ejercicio 5: Suma de Números Pares
Escribe un programa que calcule la suma de todos los números pares del 1 al 100.
'''
#Alternativa 1 -> se recorren todos los números del 1 al 100 y si al dividir no tiene cociente (=par) y se suma

Suma = 0 #se declara una variable para almacenar la suma

i = 1 #se declara una varible para el bucle

while i <= 100: #bucle hasta que llegue a 100
  if i % 2 > 0 : #si al divir hay cociente (>0) es par 
    Suma += i #se incrementa el valor de la variable sumar con el número del bucle
  
  i += 1 
  
print(f'La suma de todos los números pares del 1 al 100 es : {Suma}')
    
#Alternativa 2 se recorren todos los números del 2 al 100 de dos en dos (=pares) y se suma
Suma = 0 #se declara una variable para almacenar la suma

i = 2 #Se declara una variable el contador para el bucle con el valor del primer número par: 2)

while i <= 100: #bucle hasta que llegue a 100
  Suma += i #se suma el valor de la variable sumar con el número del bucle
  i += 2 #se incremeta el contador en dos unidades (pares) 
  
print(f'La suma de todos los números pares del 1 al 100 es : {Suma}')

#Alternativa 3 Suma de una serie aritmética

primer_par = 2 #Se declara el primer número par (2)
ultimo_par = 100 #Se declara el último número par (100)
diferencia = 2 #Se declara el salto entre los números para el cálculo

Número_de_términos = (ultimo_par - primer_par) // diferencia + 1 #Cálculo del número de terminos de la serie
# print(f'La cantidad de números pares del 1 al 100 es : {Número_de_términos}')

Suma = (Número_de_términos / 2) * (primer_par + ultimo_par) #Cálculo de la suma de una progresión aritmética

print(f'La suma de todos los números pares del 1 al 100 es : {Suma}') 

