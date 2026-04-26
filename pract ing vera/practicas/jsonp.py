import json

estudiantes = [
    {"nombre": "Ana", "nota": 9},
    {"nombre": "Luis", "nota": 4}
]

# guardar
with open("estudiantes.json", "w") as f:
    json.dump(estudiantes, f, indent=4)  # indent=4 lo hace legible

# cargar
with open("estudiantes.json", "r") as f:
    estudiantes = json.load(f)