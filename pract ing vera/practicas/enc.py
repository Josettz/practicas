class Estudiante:
    def __init__(self,nombre, nota):
        self._nombre = nombre
        self.__nota = nota

    @property
    def nombre(self):
        return self._nombre

    @property
    def nota(self):
        return self.__nota
    
    @nota.setter
    def nota(self, valor):
       if valor < 0 or valor > 10:
         print("Nota inválida...")
       else:
         self.__nota = valor

    def estado(self):
       if self.nota >= 6:
          print("APROBADO")
       else:
          print("REPROBADO")

e = Estudiante("Luis", 8)
print(e.nombre)
print(e.nota)
e.nota = 12
e.nota = 5
print(e.nota)
e.estado()