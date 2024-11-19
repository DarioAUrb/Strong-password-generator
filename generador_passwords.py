import random
import string
import secrets

#Este programa tiene como objetivo crear paswords seguras.
#Este programa permite al usuario crear un passwords segura o verificar la seguridad de un password ingresada.


# Lista para almacenar los caracteres generados
matriz_caracteres = []

#Función para generar un número seguro para la password y añadirlo a la matriz de carácteres
def segmento_num():
    num = secrets.randbelow(10)
    matriz_caracteres.append(['Número', num])
    return str(num)

#Función para generar un símbolo seguro para la password y añadirlo a la matriz de carácteres
def segmento_simbolos():
    simbolo = secrets.choice(string.punctuation)
    matriz_caracteres.append(['Símbolo', simbolo])
    return simbolo

#Función para generar una letra minúscula para la password y añadirlo a la matriz de carácteres
def segmento_letra_mn():
    letra_minuscula = random.choice(string.ascii_lowercase)
    matriz_caracteres.append(['Letra minúscula', letra_minuscula])
    return letra_minuscula

#Función para generar un letra mayúscula para la password y añadirlo a la matriz de carácteres
def segmento_letra_my():
    letra_mayuscula = random.choice(string.ascii_uppercase)
    matriz_caracteres.append(['Letra mayúscula', letra_mayuscula])
    return letra_mayuscula

# Función para generar caracteres aleatorios adicionales si la longitud no es suficiente
def generar_caracter_aleatorio():
    opciones = []
    if num_pswd == "S":
        opciones.append(segmento_num())
    if simbolos_pswd == "S":
        opciones.append(segmento_simbolos())
    if letra_pswd == "S":
        opciones.append(segmento_letra_mn())
        opciones.append(segmento_letra_my())
    return random.choice(opciones)


# Función para verificar la seguridad de la password ingresada
def verificar_seguridad(password):
    es_segura = True
    if len(password) < 8:
        print("La password debe tener al menos 8 caracteres.")
        es_segura = False
    if not any(char.isupper() for char in password):
        print("La password debe tener al menos una letra mayúscula.")
        es_segura = False
    if not any(char.islower() for char in password):
        print("La password debe tener al menos una letra minúscula.")
        es_segura = False
    if not any(char.isdigit() for char in password):
        print("La password debe tener al menos un número.")
        es_segura = False
    if not any(char in string.punctuation for char in password):
        print("La password debe tener al menos un símbolo.")
        es_segura = False
    
    if es_segura:
        print("La password ingresada es segura.")
    else:
        print("La password ingresada no es segura.")



opcion_menu = int(input("Que deseas hacer? \n 1.Crear password \n 2.Verificar password \n:"))

if opcion_menu == 1:
# Ciclo para permitir al usuario generar varias contraseñas
    otro = "S"
    while otro == "S":
    # Solicitar la longitud de la contraseña entre 8 y 16 caracteres
        while True:
            try:
                longitud = int(input("Elige la longitud de tu password (entre 8 y 16 caracteres): "))
                if 8 <= longitud <= 16:
                    break
                else:
                    print("La longitud debe ser entre 8 y 16 caracteres.")
            except ValueError:
                print("Debes ingresar un número válido.")

        num_pswd = input("¿Deseas que tu password contenga números? S / N ").upper()
        simbolos_pswd = input("¿Deseas que tu password contenga símbolos? S / N ").upper()
        letra_pswd = input("¿Deseas que tu password contenga letras? S / N ").upper()
        password_generada = []

        if num_pswd != "S" and simbolos_pswd != "S" and letra_pswd != "S":
            print("Debes de seleccionar al menos dos campos para generar una password segura")
            break
        elif (num_pswd == "S" and simbolos_pswd != "S" and letra_pswd != "S") or (simbolos_pswd == "S" and num_pswd != "S" and letra_pswd != "S") or (letra_pswd == "S" and num_pswd != "S" and simbolos_pswd != "S"):
            print("Debes de seleccionar al menos dos campos para generar una password segura")
            break
        else:
            if num_pswd == "S":
                password_generada.append(segmento_num())
            if simbolos_pswd == "S":
                password_generada.append(segmento_simbolos())
            if letra_pswd == "S":
                password_generada.append(segmento_letra_mn())
                password_generada.append(segmento_letra_my())
            
            # Si no se alcanzó la longitud deseada, generar más caracteres aleatorios
            while len(password_generada) < longitud:
                password_generada.append(generar_caracter_aleatorio())

            # Mostrar la contraseña generada
        print("Password generada: ", ''.join(password_generada))

        otro = input("¿Deseas generar otra password? S / N ").upper()

if opcion_menu == 2:
    otro = "S"
    while otro == "S":
        # Solicitar una password al usuario y verificar su seguridad
        password_usuario = input("Ingresa tu propia password para verificar su seguridad: ")
        verificar_seguridad(password_usuario)
        otro = input("¿Deseas verificar otra password? S / N ").upper()

if opcion_menu != 1 and opcion_menu !=2:
    print("Opcion no disponible")
