'''
Ejercicio 4: Contador de Vocales
Crea un programa que cuente el número de vocales en una palabra ingresada por el usuario.
'''
print ('CONTADOR DE VOCALES')

TextToCount = str(input('Introduce un texto: ')) #Se solicita introducir un texto

Counter = 0 #Se defina la variable Contador a 0 que irá incrementado cuando encuentre una vocal
Vocals = 'AEIOUaeiou' #Se crea una variable tipo cadana que tien el conjunto de todas las vocales

for Letter in TextToCount: #Bucle para ir recorriendo cada letra del texto introducido en TextToCount
  if Letter in Vocals: #Se pregunta si la letra de la variable introdida está dentro de la variable introducida
     Counter += 1 #Se suma 1 al contador de variables definido
      
print(f'El texto {TextToCount} tiene {Counter} vocales') #Se imprime el texto introducido y el valor del contador.add()
