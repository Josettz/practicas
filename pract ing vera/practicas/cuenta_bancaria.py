class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        
    def depositar(self, cantidad):
        self.saldo = self.saldo + cantidad
        print(f"Depósito: ${cantidad} | Saldo actual: ${self.saldo}")
        
    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo = self.saldo - cantidad
            print(f"Retiro: ${cantidad} | Saldo actual: ${self.saldo}")
        else:
            print("Fondos insuficientes.")

    def ver_saldo(self):
        print(f"Titular: {self.titular} | Saldo: ${self.saldo}")

cuenta = CuentaBancaria("Ana", 100)
cuenta.depositar(50)
cuenta.retirar(200)
cuenta.retirar(30)
cuenta.ver_saldo()
cuenta.retirar(40)
cuenta.ver_saldo()