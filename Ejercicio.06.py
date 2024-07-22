'''
Ejercicio 6: Verificación de Palíndromo
Crea un programa que verifique si una palabra ingresada por el usuario es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
'''
word = input("Introduce una palabra: ") # Se pide introducir una palabra


Palindromo = word == word[::-1] # se compara la palabra con su reverso ([::-1] invierte una palabra

if Palindromo:
    print(f"La palabra '{word}' es un palíndromo.")
else:
    print(f"La palabra '{word}' no es un palíndromo.")