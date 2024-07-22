'''
Ejercicio 10: Determinar el Día de la Semana
Escribe un programa que determine el día de la semana correspondiente a un
número ingresado por el usuario (1 para lunes, 2 para martes, etc.).
'''
Day = str (input('Introduce el un dia de la semana (1-7): ')) # Se pide introducir un número de semana y se le asigna a la variable Day

Days = {'1' : 'Lunes', # Se crea un diccionario en el que la clave es el número de semana y el valor es el día de la semana
      '2' : 'Martes',
      '3' : 'Miércoles',
      '4' : 'Jueves',
      '5' : 'Viernes',
      '6' : 'Sábado',
      '7' : 'Domingo'}

if Day in Days : # Se preguna si el valor introducido está dentro de los valores del diccionario y se muesetra el valor del número introducido.
  print (f'El día se la semana correspondiente es {Days[Day]}')
  
else: #Si el valor no está en el diccionarioi, se muestra un texto indicando que el valoro es erróneo
  print ('Número ingresado de semana no es correcto, debe ser del 1 al 7')