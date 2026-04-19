class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def ver_info(self):
        print(f"Empleado: {self.nombre} | Sueldo: ${self.sueldo}")

class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.departamento = departamento
    
    def dirigir(self):
        print(f"{self.nombre} digire el departamento de {self.departamento}")
    
class Vendedor(Empleado):
    def __init__(self, nombre, sueldo, comision):
        super().__init__(nombre, sueldo)
        self.comision = comision
    
    def calcular_pago(self):
        sueldo_total = self.sueldo + (self.sueldo * self.comision / 100)

        print(f"El sueldo total de {self.nombre} es de {sueldo_total}")

g = Gerente("Carlos", 2000, "Sistemas")
g.ver_info()
g.dirigir()

v = Vendedor("María", 1000, 15)
v.ver_info()
v.calcular_pago()

        

    

    

