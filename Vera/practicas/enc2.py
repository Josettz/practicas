class producto:
    def __init__(self,nombre,precio):
        self.__nombre = nombre
        self.__precio = precio
    

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, valor):
       if valor <= 0:
          print("Precio inválido, debe ser mayor a 0")
       else:
          self.__precio = valor  
         
    def categoria(self):
        if self.precio < 50:
            print("es economico")
        elif self.precio >= 50 and self.precio < 200:
            print("es estandar")    
        else: 
            print("es premium")
    
p = producto("Laptop", 800)
print(p.nombre)
print(p.precio)
p.precio = -10
p.precio = 45
print(p.precio)
p.categoria()
 
        