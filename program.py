import json

# Carga el archivo de configuración en un diccionario de Python
with open("config.json", "r") as f:
    config = json.load(f)

# Muestra una interfaz gráfica de usuario con los campos del archivo de configuración
# y los botones para guardar y cancelar

print("Por favor introduce el " + config["campo"]["nombre"]["label"])
nombre = input()
while nombre == config["campo"]["nombre"]["value"]:
    print(config["campo"]["nombre"]["messages"])
    nombre = input(config["if_error"]["messages"])
config["campo"]["nombre"]["value"] = nombre



print("Por favor introduce el " + config["campo"]["apellido"]["label"])
apellido = input()
while apellido == config["campo"]["apellido"]["value"]:
    print(config["campo"]["apellido"]["messages"])
    apellido = input(config["if_error"]["messages"])
config["campo"]["apellido"]["value"] = apellido



print("Por favor introduce el " + config["campo"]["edad"]["label"])
edad = input()
while edad == config["campo"]["edad"]["value"]:
    print(config["campo"]["edad"]["messages"])
    apellido = input(config["if_error"]["messages"])
config["campo"]["edad"]["value"] = edad



# Muestra los botones para guardar y cancelar
print("Boton: " + config["acciones"]["guardar"]["label"])
print("Boton: " + config["acciones"]["cancelar"]["label"])

# Ejecuta la función correspondiente cuando se hace clic en un botón
accion = input("Escribe si guardar o cancelar: ")

if accion == config["acciones"]["guardar"]["label"]:
    # Ejecuta la función "guardar_datos"
    print("Usaste la funcion: " + config["acciones"]["guardar"]["function"])

elif accion == config["acciones"]["cancelar"]["label"]:
    #Ejecuta la funcion "cancelar_accion"
    print("Usaste la funcion: " + config["acciones"]["cancelar"]["function"])
