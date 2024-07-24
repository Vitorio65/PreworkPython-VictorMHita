'''
Ejercicio 9: Conversor de Divisas
Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que
en este caso se solicita el tipo de cambio.
'''
print ('CONVERSOR DOLAR - EUROS')

Amount = float(input('Introduce la cantidad en dolares: ')) #Se pide la cantadad a cambiar y se define como float 

Type_change = float(input('Introduce el tipo de cambio: ')) #Se el tipo de cambio

print(f'la conversión (1 dolar {Type_change:.2f}]) es : {(Amount * Type_change):.2f}') #Se imprime el resultado y se formatea con dos decimales