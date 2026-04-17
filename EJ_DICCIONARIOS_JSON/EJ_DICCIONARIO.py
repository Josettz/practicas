import json

diccionario = {
    "ESTUDIANTE1": {
            "nombre": "Isaac silva",
            "Genero": "Masculino",
            "Edad": "20"
    },
    "ESTUDIANTE2" : {
            "nombre": "Belfor Castro",
            "Genero": "Masculino",
            "Edad": "21"       
    },
    "ESTUDIANTE3" : {
            "nombre": "Elian Vladimir",
            "Genero": "Masculino",
            "Edad": "21"        
    }

    
}

print(diccionario["ESTUDIANTE1"]["nombre"])

with open("diccionario.json", "w") as archivo:
    json.dump(diccionario,archivo) 

print("ARCHIVO JSON CREADO CON EXITO")
