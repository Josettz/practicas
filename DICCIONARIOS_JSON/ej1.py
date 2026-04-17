diccionario = {

    "nombre":"Juan Cabezas",
    "edad":23,
    "Es_estudiante": True,
    "Notas":[7,10,9],

    "profesor":{
        "Nombre":"Juan Barquitos",
        "edad":30,
        "materia":"Programacion"

    }



}

#print(diccionario)
Es_estudiante = diccionario.pop("Es_estudiante")
print(diccionario)