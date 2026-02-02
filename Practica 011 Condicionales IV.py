# Un alumno está postulando a una beca universitaria. Requisitos:
# - Vive a una distancia > 40 Km
# - Tiene más de 2 hermanos que estudian en la universidad (es decir, > 2)
# - Su salario familiar es ≤ 8400 dólares anuales brutos.
# Si cumple las 3 condiciones, se le otorgará la beca. De lo contrario, no se le otorgará.

print("Programa de becas universitarias (año 2025)")
distancia_escuela = int(input("Ingrese la distancia a la universidad en Km: "))

numero_hermanos = int(input("Ingrese el número de hermanos en el centro: "))

salario_familiar = int(input("Ingrese el salario familiar bruto anual en dólares: "))

# Mostrar los valores ingresados (opcional)
print(f"Distancia: {distancia_escuela} Km") 
print(f"Número de hermanos: {numero_hermanos}")
print(f"Salario familiar: {salario_familiar} (anual, bruto)")


if distancia_escuela > 40 and numero_hermanos > 2 and salario_familiar <= 8400:  # se usa and porque debe cumplir todas las condiciones
    print("Usted cumple con los requisitos para obtener una beca universitaria")
else:
    print("Usted no cumple con los requisitos para obtener una beca universitaria")


if distancia_escuela > 40 and numero_hermanos > 2 or salario_familiar <= 8400:  # se usa or porque con que cumpla una de las condiciones alcanza
    print("Usted cumple con los requisitos para obtener una beca universitaria")
else:
    print("Usted no cumple con los requisitos para obtener una beca universitaria")