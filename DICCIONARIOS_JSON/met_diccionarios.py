usuario = {
    "persona1":{
    "nombre": "Jose Antonio",
    "edad": 20,
    "carrera": "Ingeniería de Software",
    "universidad": "UNEMI" 
    },
    "persona2":{
        "nombre": "Jonathan Castro",
        "edad": 20,
        "carrera": "Medici",
        "universidad": "UEESS" 
    }
} 

print(usuario["persona2"]["nombre"])
print(usuario["persona1"].get("apellido", "No encontrado")) 

usuario["edad"] = 21

print(usuario["persona1"].get("edad", "pon la informacion correcta"))

print(usuario["persona1"].keys()) 
print(usuario["persona1"].values()) 
print(usuario["persona2"].items())