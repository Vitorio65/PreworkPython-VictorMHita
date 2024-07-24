'''
Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.
'''
print ('CÁLCULO DE MASA CORPORAL "MC"')

weight = int(input('Introduce el peso (en kgs): ')) # Se solicita el peso en kgs
height = int(input('Introduce la estatura (en cms): ')) # Se solicita la altura en cms

MC = weight / ((height / 100) ** 2)

print (f'La masa corporal (MC) = {MC:.2f}') #Se calcula MC = weight (in kg) / height (in meters)² y se formatea con dos decimales

# print (f'La masa corporal (MC) = {weight / ((height / 100) ** 2):.2f}') #Se calcula MC = weight (in kg) / height (in meters)² y se formatea con dos decimales

'''
For adult men and women, a BMI of 18.5-24.9 is considered normal, 25-29.9 is considered overweight, and 30 or higher is considered obese.
'''

# Depende de la MC se saca un comentario

if  MC < 18.5: 
  print ('es considerado delgado')

elif MC >= 18.5 and MC<=24.9 :
  print ('es considerado normal')
  
elif  MC >= 25.0 and MC<=29.9:
   print ('es considerado con sobrepeso')
   
elif MC >30:
   print ('es considerado como obeso')   
   
   


