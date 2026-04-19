estudiantes = [
    {"nombre": "Ana", "nota": 9, "carrera": "Sistemas"},
    {"nombre": "Luis", "nota": 4, "carrera": "Marketing"},
    {"nombre": "María", "nota": 7, "carrera": "Sistemas"},
    {"nombre": "Carlos", "nota": 5, "carrera": "Marketing"},
    {"nombre": "Sofía", "nota": 8, "carrera": "Sistemas"}
]

nombres = list(map(lambda e: e["nombre"], estudiantes))
aprobados = list(filter(lambda e:e["nota"] >= 6, estudiantes))
notas = list(map(lambda e: e["nota"] + 1, estudiantes))
sistema = list(map(lambda e: e["nombre"], filter(lambda e: e["carrera"] == "Sistemas", estudiantes)))

print(nombres)
print(aprobados)
print(notas)
print(sistema)