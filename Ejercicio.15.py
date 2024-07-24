'''
Ejercicio 15: Conversor de Tiempo
Escribe un programa que convierta un número de minutos en horas y minutos. Por ejemplo, 145 minutos serían 2 horas y 25 minutos.
'''
print ('CONVERSOR DE MINUTOS A HORAS Y MINUTOS')

Time = int(input('Introduce los minutos: ')) # Se solita que el usuario entre los minutos y se guarda en la variable Time de tipo integer


print(f'{Time} minutos son {Time // 60} horas y {(Time % 60) % 60} minutos') #se imprime, primero el numero entero de dividir por 60, que serían las horas y luego del resto se vuelve a divir por 60 para obtener los minutos




