'''
Ejercicio 7: Calculadora Simple
Crea un programa que realice operaciones aritméticas simples (suma, resta, multiplicación, división) según la elección del usuario.
'''
print ('CÁLCULADORA SIMPLE')

First_number = int(input ('Introduce el primer término: ')) #Solicita el primer término de la operación

Second_number = int(input ('Introduce el segundo término: ')) #Solicita el primer término de la operación

Operation = str (input('Introduce la operación (1=Suma / 2=Resta / 3=Multimplicación / 4=División): ')) #Solicita la operación a realizar. Para facilitar la introdución y evitar errones se puede el número de la operación

if Operation == "1": #Si el número de operación es 1 se imprime la suma de ambos térnimos
  print (f'El resultado es {First_number + Second_number}')
    
elif Operation == "2": #Si el número de operación es 2 se imprime la resta de ambos térnimos
  print (f'El resultado es {First_number - Second_number}')
  
elif Operation == "3": #Si el número de operación es 3 se imprime la multiplicación de ambos térnimos
  print (f'El resultado es {First_number * Second_number}')

elif Operation == "4": #Si el número de operación es 4 se imprime la división de ambos térnimos
  print (f'El resultado es {First_number / Second_number}')

else: #En caso que no se haya introducido un 1, 2, 3 ó 4 saca un mensaje de error
  print ('Operación errónea')
 
