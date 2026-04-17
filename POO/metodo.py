class personaje:
    def __init__(self, nombre, clase, nivel, salud):
        self.nombre = nombre
        self.nivel = nivel
        self.salud = salud

    def atacar(self,objetivo):
        return f"{self.nombre} ataca a {objetivo}"
    
    
class mago(personaje):
    def __init__(self, nombre, clase, nivel, salud):
        super().__init__(nombre, clase, nivel, salud)
