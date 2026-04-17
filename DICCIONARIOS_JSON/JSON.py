import json

# Un diccionario básico, sin cosas anidadas
mi_perfil = {
    "nombre": "Jose Antonio",
    "edad": 20,
    "rango": "Diamante"
}


# Abrimos un archivo en modo escritura ("w")
with open("perfil.json", "w") as archivo:
    
    # Metemos el diccionario dentro del archivo
    json.dump(mi_perfil, archivo)

print("¡Archivo guardado!")


