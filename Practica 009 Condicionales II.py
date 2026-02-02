# PRACTICA IF ELSE Y ELIF

print("Verificación de acceso")

edad_usuario=int(input("Por favor ingrese su edad: "))

if edad_usuario<18:              # edad menor a 18
    print("No puedes ingresar a la página")
elif edad_usuario==18:           # edad exacta
    print("Puedes ingresar a la página, bajo supervisión de un adulto")
else:                            # edad mayor a 18
    print("Puedes ingresar a la página")


# PRACTICA MÉTODOS DE CADENAS VIDEO 33 ARCHIVO 031

print("Verificación de acceso")

edad_usuario=(input("Por favor ingrese su edad: "))  # no debe incluir int()

while(edad_usuario.isdigit()==False):    # se usa isdigit
    print("Por favor, introduce un valor numérico")
    edad_usuario=(input("Por favor ingrese su edad: "))

if (int(edad_usuario)<18):               # al usar la función isdigit se requiere que se presida de una valor int
    print("No puedes ingresar a la página")
elif edad_usuario==18:           
    print("Puedes ingresar a la página, bajo supervisión de un adulto")
else:                            
    print("Puedes ingresar a la página")

