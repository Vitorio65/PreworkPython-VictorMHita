'''
Ejercicio 11: Calculadora de Edad
Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad actual.
'''

Age = int(input('Introduce el año de nacimiento: ')) #Se pide que se introduzca un año y se almacena en la variable 'Age?

from datetime import datetime #Se importa datetime del módulo datetime.

Current_year = datetime.now().year #Se obtiene el año actual. datetime.now() devuelve la fecha y hora actuales, y .year extrae el año de esa fecha.

if Age < 1900 or Age > Current_year : #Se comprueba que el número ingtroducido esté entre el el añó 1900 y el actual. Si no se saca el mensaje siguiente
  print ('El año introducido debe estar entre el año 1900 y el actual')
  
else:
  print (f'La edad es {Current_year - Age}') #Se imprime la diferencia entre el año actual y el año introducido. No hace falta truncar el resultado al haber declarado la variable Age tipo "int"
  
  
  