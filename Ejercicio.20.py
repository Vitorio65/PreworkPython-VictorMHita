'''
Ejercicio 20: Suma de Números en una Lista
Crea un programa que sume todos los números en una lista ingresada por el usuario.
'''
print ('SUMA DE UNA LISTA DE NUMEROS INTRODUCIDOS POR EL USUARIO')

Numeros = list(map(int,input('Introduce los números a sumar, separados por ",": ').split(','))) #se solita una entradas de números, separdos por comas, se divide con split y se guarda en una lista 
               
Suma = 0 #se pone la variable Suma a 0

for Numero in Numeros: #se recorre la tabla y se suman los números
    Suma += Numero

print(f'La suma de todos los números es {Suma}') #se imprime el resultado.

            
            