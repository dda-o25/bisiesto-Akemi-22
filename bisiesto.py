"""
Akemi Clarissa Olvera Arao
19/09/25
Determinar si un año es bisiesto o no
"""

# Declaraciones


# Entradas
año = int(input("Ingrese un año: "))

# Proceso
if año % 100 == 0:
    if año % 400 == 0:
        print(año, "es un año bisiesto")
    else:
       print(año, "no es un año bisiesto")
elif año % 4 == 0:
    print(año, "es un año bisiesto")
else:
    print(año, "no es un año bisiesto")



# Salidas

