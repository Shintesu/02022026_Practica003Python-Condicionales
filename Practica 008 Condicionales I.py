# CONDICIONALES
# if, elif, else    
# Permiten ejecutar diferentes bloques de código según se cumplan o no ciertas condiciones.
 # if condición:
    # Bloque de código si la condición es verdadera
 # elif otra_condición:
    # Bloque de código si la otra condición es verdadera
 # else:
    # Bloque de código si ninguna condición es verdadera



def evaluacion(nota):
    valoracion = "Aprobado" # Valor por defecto
    if nota < 5: # Si la nota es menor que 5
        valoracion = "Suspendido"   # Cambiamos el valor de la variable
    return valoracion # Devolvemos el valor de la variable

print(evaluacion(4)) 
print(evaluacion(6))    
print(evaluacion(5))



print("Programa de evaluación de notas")
nota_alumno=input("Introduce la nota del alumno: ") # La función input siempre devuelve una cadena
def evaluacion(nota): 
    valoracion = "Aprobado" 
    if nota < 5: 
        valoracion = "Suspendido"   
    return valoracion 

print(evaluacion(float(nota_alumno)))