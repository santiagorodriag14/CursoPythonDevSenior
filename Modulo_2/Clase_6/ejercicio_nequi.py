class Usuario:
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

    def mostrar_info(self):
        print(f"Nombre: {self.nombre} Documento: {self.documento}")

class ClientePremium(Usuario):
    def __init__(self, nombre, documento, beneficios):
        super().__init__(nombre, documento)
        self.beneficios = beneficios
    
    def mostrar_beneficios(self):
        return f"{self.nombre} tiene los siguientes beneficios premium: {self.beneficios}"
    
class Transaccion:
    def __init__(self, tipo, monto):
        self.tipo = tipo
        self.monto = monto
    
    def mostrar_transaccion(self):
        return f"Tipo: {self.tipo} Monto: {self.monto}"


class Cuenta:
    def __init__(self,numero_cuenta, saldo=0):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        self.transacciones = [] #Composición: cuenta tiene una lista de Transacciones

    def depositar(self,monto):
        self.saldo += monto
        self.transacciones.append(Transaccion("Consignacion", monto))
    
    def retirar(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            self.transacciones.append(Transaccion("Retiro", monto))
        else:
            print("Saldo insuficiente para retirar.")

    def mostrar_historial(self):
        print(f"Historial de transacciones de la cuenta: {self.numero_cuenta}")
        for transaccion in self.transacciones:
            print(transaccion.mostrar_transaccion())
    
    def mostrar_saldo(self):
        print(f"El saldo actual de la cuenta {self.numero_cuenta}: {self.saldo}")


usuario = Usuario("Carlos", "12345")
clientePremium = ClientePremium("Javier", "2343214", "descuentos exclusivos")

cuenta1 = Cuenta("001", 1000)
cuenta1.depositar(5000)
cuenta1.retirar(3000)
cuenta1.mostrar_saldo()
cuenta1.mostrar_historial()


usuario.mostrar_info()
clientePremium.mostrar_info()
print(clientePremium.mostrar_beneficios())