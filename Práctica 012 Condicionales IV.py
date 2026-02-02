# Un estudiante debe escoger una asignatura optativa entre las siguientes:

print("Asignaturas optativas disponibles (2025): ")
print("Asignaturas optativas: Informática gráfica - Ingeniería en IA - Usabilidad y accesibilidad")
opcion=input("Escriba la asignatura que desea cursar: ")
asignatura=opcion.lower()  # convierte todo a minúsculas

if asignatura in ("informática gráfica", "ingeniería en ia", "¿usabilidad y accesibilidad"): # todo en minúsculas 
    print(f"Usted ha seleccionado la asignatura: {asignatura}")

else:
    print("La asignatura escogida no está disponible. Debe escoger una de las optativas.")