class Figura:
    def __init__(self, color):
        self.color = color
        
    def area(self):
        pass

    def descripcion(self):
        print(f"Soy un {self.__class__.__name__} de color {self.color} y mi área es {self.area()}")

class Rectangulo(Figura):
    def __init__(self, color, ancho, alto):
        super().__init__(color)
        self.ancho = ancho
        self.alto = alto
    def area(self):
        return self.ancho * self.alto
    

class Circulo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio
    def area(self):
        return 3.1416 * self.radio ** 2

class Triangulo(Figura):
    def __init__(self, color, base, altura):
        super().__init__(color)
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura / 2


figuras = [
    Rectangulo("rojo", 5, 3),
    Circulo("azul", 4),
    Triangulo("verde", 6, 8)
]

for f in figuras:
    f.descripcion()