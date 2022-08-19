
# Desafio AÑO BISIESTO - Alan Ozzan #

def es_bisiesto(año):
        if año % 400 == 0:
            return "Si" #Se le puede poner True o False, pero dentro de "Comillas" se puede poner cualquier valor.
        elif año % 100 == 0:
            return "No"
        elif año % 4 == 0:
         return "Si"
        else:
            return "No"

año = 2020
print('El año', (año), 'es Bisiesto?: ', (es_bisiesto(año)))
año = 2023
print('El año', (año), 'es Bisiesto?: ', (es_bisiesto(año)))
año = 2000
print('El año', (año), 'es Bisiesto?: ', (es_bisiesto(año)))
año = 1989
print('El año', (año), 'es Bisiesto?: ', (es_bisiesto(año)))

