"""
# Usando la sentencia "if-else" realizado lo siguiente:
nombre = "Rene"
if (len(nombre) > 5):
    print("El nombre tiene más de 5 caracteres")
else:
    print("El nombre no tiene más de 5 caractres")

# Usando la sentencia "if-elif-else" realizando lo siguiente:
nombre = "Rene" # puede ser Juan Carlos, Ari, Bob
if (len(nombre) >= 1 and len(nombre) <= 3):
    print(f"Tu nombre tiene entre 1 y 3 caracteres")
elif (len(nombre) >= 3 and len(nombre) <= 5):
    print(f"Tu nombre tiene entre 3 y 5 caracteres")
else:
    print(f"Tu nombre tiene más de 5 caracteres")

# Usando el operador terneario realizando lo siguiente:

lista = [1,3,5,4] # puede tener [1,3,5,4]
mensaje = "Mi lista tiene 3 o menos elementos" if len(lista) <= 3 else "Mi lista tiene más de 3 elementos"
print(mensaje)

# Usando el bucle "while" realizar lo siguiente:

lenguajes = ["c++", "java", "python", "sql", "javascript"]
contador = 0
while contador <= len(lenguajes):
    if (lenguajes[contador] == "python"):
        print(f"\tHemos encontrado el elemento python :)")
        print(f"\tEn la iteración número: {contador+1}")
        break
    contador += 1

# Usando el bucle "for" realizar lo siguiente:
mi_lista = ["google", "facebook", "microsoft", "apple", "spacex"]
print("La lista de los elementos son: ")
for elemento in mi_lista:
    print(f"\t{elemento}")

# Usando el bucle "for" realizar lo siguiente:

companias_tech = ["google", "facebook", "microsoft", "apple", "spacex", "twitter", "neuralink"]
nombres_cortos = []
nombres_largos = []
for companias in companias_tech:
    if len(companias) <= 6 :
        nombres_cortos.append(companias)
    elif len(companias) > 6 :
        nombres_largos.append(companias)
print(f"\tLas compañias de menos de 6 caracteres son: {len(nombres_cortos)}")
print(f"\ty estas son las siguientes: ", nombres_cortos)
print(f"\tLas compañias de más de 6 caracteres son: {len(nombres_largos)}")
print(f"\ty estas son las siguientes: ", nombres_largos)

# Usando el bucle "for" realizar lo siguiente:

info_usuario = {"nombre": "Maria", "email": "maria@email.com", "edad": 42}
print("\tllave\t\t valor")
for key, value in info_usuario.items():
    print(f"\t{key}\t:\t{value}")

# Usando el bucle "for" y la funcion "range()" realizar lo siguiente:

print("Los números son: ")
for numero in range(10,16):
    print("\t", numero, end='')

# Ejercicios mas complejos

usuarios = [ {"nombre" : "María", "email" : "maria@email.com", "edad" : 42}, \
    {"nombre" : "Rene", "email" : "rene@hola.com", "edad" : 42}, \
    {"nombre" : "Juan Carlos", "email" : "juancarlos@otro.com", "edad" : 39} ]
for usuario in usuarios:
    print(f"\tEl usuario {usuario['nombre']} tiene el email: {usuario['email']} y tiene {usuario['edad']} años")


"""

usuarios = [ {"nombre" : "María", "email" : "maria@email.com", "edad" : 42}, \
    {"nombre" : "Rene", "email" : "rene@hola.com", "edad" : 42}, \
    {"nombre" : "Juan Carlos", "email" : "juancarlos@otro.com", "edad" : 39} ]
for usuario in usuarios:
    usuario["longitud_nombre"] = len(usuario["nombre"])
    if usuario["longitud_nombre"] > 5:
        del usuario["email"]
print("\n\tLa lista donde se agrega longitud de nombre es:\n", usuarios, "\n")

for usu in usuarios:
    usu["tiene_email"] = True
    if not usu.get("email"):
        usu["tiene_email"] = False
print("\tEl usuario que tiene email false\n", usu, "\n")
print("\tLa lista completa es:\n",usuarios, "\n")
