# CONDICIONALES III
# Concatenación de operadores de comparación en un condicional if

edad=-23
if 0<edad<100: # Concatenación de operadores de comparación
    print("La edad es correcta")
else:
    print("La edad no es correcta")

# Ejercicio: Pide el salario de 4 personas y muestra si los salarios designados tiene lógica (relación cargo-salario)
salario_presidente=int(input("Introduce el salario del presidente: "))
print("Salario presidente: " + str(salario_presidente))

salario_director=int(input("Introduce el salario del director: "))
print("Salario director: " + str(salario_director))

salario_jefe_area=int(input("Introduce el salario del jefe de area: "))
print("Salario jefe de area: " + str(salario_jefe_area))

salario_administrativo=int(input("Introduce el salario del administrativo: "))
print("Salario administrativo: " + str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print("Los salarios tienen lógica")
else:
    print("Los salarios no tienen lógica, hay desvío de fondos. ¡¡¡Llamen a Hacienda!!!")

