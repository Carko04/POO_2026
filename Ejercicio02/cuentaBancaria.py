class CuentaBancaria:
    def __init__(self, titular, numeroCuenta, saldo):
        self.titular = titular
        self.numeroCuenta = numeroCuenta
        self.saldo = saldo

    def mostrar(self):
        print(f"Titular: {self.titular}, Cuenta: {self.numeroCuenta}, Saldo actual: {self.saldo}")

    def ingresar(self, cantidad):
        if cantidad > 0:
            saldo_anterior = self.saldo
            self.saldo += cantidad
            print(f"Saldo anterior: {saldo_anterior}")
            print(f"Cantidad depositada: {cantidad}")
            print(f"Saldo final: {self.saldo}")
        else:
            print("La cantidad a ingresar debe ser positiva.")

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            saldo_anterior = self.saldo
            self.saldo -= cantidad
            print(f"Saldo anterior: {saldo_anterior}")
            print(f"Cantidad retirada: {cantidad}")
            print(f"Saldo final: {self.saldo}")
        else:
            print("La cantidad a retirar debe ser positiva y no exceder el saldo disponible.")


cuenta1 = CuentaBancaria("Kevin", "4444", 1000)

cuenta1.ingresar(500)
print()  # espacio visual

cuenta1.retirar(200)
print()

cuenta1.mostrar()

