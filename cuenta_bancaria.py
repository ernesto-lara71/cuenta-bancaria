class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, cantidad):
        if cantidad <= 0:
            print(f'{self.titular} deposita una cantidad invalida')
        else:
            self._saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= 0:
            print(f'{self.titular} retira una cantidad invalida')
            return False
        elif cantidad > self._saldo:
            print(f'{self.titular} tiene saldo insuficiente')
            return False
        else:
            self._saldo -= cantidad
            return True

    def transferir(self, cantidad, otra_cuenta):
        if self.retirar(cantidad):
            otra_cuenta.depositar(cantidad)

    def mostrar_saldo(self):
        print(f'{self.titular} tiene ${self._saldo}')

class CuentaCheques(CuentaBancaria):
    def __init__(self, titular, saldo=0, limite_sobregiro = 500):
        super().__init__(titular, saldo)
        self.limite_sobregiro = limite_sobregiro

    def retirar(self, cantidad):
        if cantidad <= 0:
            print(f'{self.titular} retira una cantidad invalida')
            return False
        if cantidad > self._saldo + self.limite_sobregiro:
            print(f'{self.titular} excede su limite de sobregiro')
            return False
        else:
            self._saldo -= cantidad
            return True

    def mostrar_saldo(self):
            print(f'{self.titular} tiene ${self._saldo} (disponible: ${self._saldo + self.limite_sobregiro})')

pedro = CuentaBancaria("Pedro", 350)
pablo = CuentaBancaria("Pablo", 100)

pedro.depositar(120)
pablo.retirar(-70)
pedro.transferir(1000, pablo)
pedro.mostrar_saldo()
pablo.mostrar_saldo()

maria = CuentaCheques("María", 100)
maria.retirar(500)
maria.mostrar_saldo()
maria.transferir(100, pablo)
maria.transferir(1, pablo)
maria.mostrar_saldo()
pablo.mostrar_saldo()
print(f'${pedro.saldo}')

print("\n--- Prueba de polimorfismo ---")
cuentas = [pedro, pablo, maria]

for cuenta in cuentas:
    cuenta.retirar(300)
    cuenta.mostrar_saldo()