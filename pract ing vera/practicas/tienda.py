class producto:
    def __init__(self,nombre,precio,stock = 0):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def agregar_stock(self,cantidad):
        self.stock = self.stock + cantidad
        print(f"el stock actual es de {self.stock}")
        
    def vender(self,cantidad):
        if cantidad <= self.stock:
            self.stock = self.stock - cantidad
            print(f"Se ha vendido {cantidad}, el stock actual es de {self.stock}")
        else:
            print("stock insuficiente para la venta")
    
    def aplicar_descuento(self, porcentaje):
        descuento = porcentaje / 100
        self.precio = self.precio - (self.precio * descuento)

    def ver_info(self):
        print(f"el producto es {self.nombre} y el precio es {self.precio}, nos queda {self.stock} de stock")

producto = producto("Arroz", 1.40)
producto.agregar_stock(20)
producto.vender(5)
producto.vender(30)
producto.aplicar_descuento(25)
producto.ver_info()
