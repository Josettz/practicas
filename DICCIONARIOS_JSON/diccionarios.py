# Sintaxis: { "clave": valor }

usuario = {
    "nombre": "Jose Antonio",
    "edad": 20,
    "carrera": "Ingeniería de Software",
    "universidad": "UNEMI"
}

print(usuario["nombre"])       # Salida: Jose Antonio
print(usuario.get("apellido", "No encontrado")) # Evita que el programa explote

usuario["edad"] = 21

print(usuario.get("edad", "pon bien tu webada"))

print(usuario.keys()) #Devuelve solo los nombres de las claves.
print(usuario.values()) #Devuelve solo los datos guardados.
print(usuario.items()) #Devuelve ambos (clave y valor) en parejas.
print(usuario.clear()) #Vacía el diccionario por completo.
