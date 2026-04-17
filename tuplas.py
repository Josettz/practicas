class Celular:
    def __init__(self, marca, specs):
        # 'specs' es una TUPLA: (memoria, ram, camara, procesador)
        self.marca = marca
        # Desempaquetamos la tupla en variables individuales
        self.memoria, self.ram, self.camara, self.procesador = specs

    def especificaciones(self):
        return f"La marca {self.marca} tiene: {self.memoria}GB, {self.ram}GB RAM y procesador {self.procesador}"

class Samsung(Celular):
    def __init__(self, marca, specs, novedad):
        super().__init__(marca, specs)
        self.novedad = novedad

    def nsamsung(self):
        return f"La novedad de Samsung es que es {self.novedad}"

# --- APLICACIÓN DE TUPLAS ---

# 1. Creamos tuplas con las características (Datos que no cambian)
specs_xiaomi = (128, 16, 108, "Helio G99")
specs_iphone = (256, 8, 48, "A15 Bionic")
specs_samsung = (512, 12, 200, "Snapdragon Gen 2")

# 2. Pasamos la tupla entera al crear el objeto
xiaomi1 = Celular("Xiaomi", specs_xiaomi)
iphone1 = Celular("iPhone", specs_iphone)
samsung1 = Samsung("Samsung", specs_samsung, "Plegable")

# 3. Guardamos los objetos en una TUPLA (Colección protegida)
mis_celulares = (xiaomi1, iphone1, samsung1)

for c in mis_celulares:
    print(c.especificaciones())



