'''
Ejercicio 19: Verificación de Año Bisiesto
Escribe un programa que determine si un año ingresado por el usuario es bisiesto o no
'''
print ('CÁLCULO DE AÑOS BISIESTOS')

'''
Para que un año sea bisiesto se deben cumplir:
  * Es divisible por 4.
  * No es divisible por 100, a menos que también sea divisible por 400.
'''  
# se define una función en al que se pasa el parámetro Anno y devuelve el texto de si es bisiesto o no, en función de si cumple las condiciones anteriores
def Bisiesto (Anno): 
  
  if Anno % 4 == 0 and (Anno % 100 != 0 or Anno % 400 == 0):
    Respuesta = "es año bisiesto"
   
  else:
    Respuesta = "no es año bisiesto"
   
  return Respuesta

# se crea un bucle infinito con la condición true para verificar si el año introducido está entre el año 1 y el 9999
while True:
  Anno = int(input('Introduce un año (entre el 1 y el 9999): '))
  
  if Anno >= 1 and Anno <= 9999: #se verifica la condición
    #print('Año correcto')
    break # se sale del bucle
  else:  
    print('El año debe ser un número entre el 1 y el 9999')
 

print(f'El año {Anno} {Bisiesto(Anno)}') #Se imprime el resultado llamando a la función Bisiesto y se pasa el parámeto Anno 



