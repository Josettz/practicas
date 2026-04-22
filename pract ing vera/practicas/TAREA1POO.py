class Empleado:
    _contador = 1
    def __init__(self, nombre, sueldo):
        self.id = Empleado._contador
        Empleado._contador += 1
        self.nombre = nombre
        self.sueldo = sueldo
        self.valor_hora = self.sueldo / 240

    def __str__(self):
        return f"[{self.id}] {self.nombre} | Sueldo: {self.sueldo} | Valor hora: {self.valor_hora:.2f}"
        

class tipoPermiso:
    def __init__(self):
        pass


e = Empleado("Anita Chacon", 300)
print(e)
