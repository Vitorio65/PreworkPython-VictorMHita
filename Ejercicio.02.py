'''
Ejercicio 2: Calculadora de Propina
Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo una propina del 15% sobre el total de la cuenta.
'''
print('CALCULADORA DE PROPINAS')

Ticket = int(input('Importe de la comanda en euros: ')) #Solicita el precio de la comanda

Total_due = Ticket + (Ticket * 0.15) #Suma el 15% al precio

print (f'Total a pagar = {Total_due}€') #Imprime la cantidad total a pagar

