import json

# --- MIXINS ---

class SerializadorMixin:
    """Añade la capacidad de convertir los datos del objeto a JSON."""
    def a_json(self):
        # vars(self) devuelve los atributos del objeto como un diccionario
        return json.dumps(vars(self), indent=4)

class LogMixin:
    """Añade la capacidad de imprimir un log con el nombre de la clase."""
    def log(self, mensaje):
        print(f"[{self.__class__.__name__} LOG]: {mensaje}")


# --- CLASES DEL SISTEMA ---

class Videojuego(SerializadorMixin, LogMixin):
    def __init__(self, titulo, genero):
        self.titulo = titulo
        self.genero = genero
        self.log(f"Instancia de {self.titulo} creada")

class Usuario(LogMixin):
    def __init__(self, nombre):
        self.nombre = nombre
        self.log(f"Usuario {self.nombre} registrado")


# --- PRUEBA ---

juego = Videojuego("Elden Ring", "Souls-like")
user = Usuario("Jose")

# El juego puede convertirse a JSON porque tiene el SerializadorMixin
print(juego.a_json())

# El usuario NO puede usar .a_json() porque no lo incluimos, 
# pero sí puede usar .log()
user.log("Entrando al servidor...")