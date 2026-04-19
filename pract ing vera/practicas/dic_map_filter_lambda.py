productos = [
    {"nombre": "Laptop", "precio": 800},
    {"nombre": "Mouse", "precio": 25},
    {"nombre": "Teclado", "precio": 60},
    {"nombre": "Monitor", "precio": 300},
    {"nombre": "Audífonos", "precio": 45}
]

nombres = list(map(lambda e: e["nombre"], productos))
precios = list(filter(lambda e: e["precio"] >= 50, productos))
descuento = list(map(lambda e: e["precio"] * 0.9, productos))
economico = list(filter(lambda e: e["precio"] < 50, productos))

print(nombres)
print(precios)
print(descuento)
print(economico)

