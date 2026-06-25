class Pago:
    def procesarPago(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")

class TarjetaCredito(Pago):
    def __init__(self, numero_tarjeta, monto):
        self.numero_tarjeta = numero_tarjeta
        self.monto = monto
    
    def procesarPago(self):
        return f"Procesando pago de ${self.monto} con Tarjeta de Crédito terminada en {self.numero_tarjeta[-4:]}."

class PayPal(Pago):
    def __init__(self, correo, monto):
        self.correo = correo
        self.monto = monto
    
    def procesarPago(self):
        return f"Procesando pago de ${self.monto} a través de la cuenta PayPal ({self.correo})."


def main():
    pagos = [
        TarjetaCredito("1234567812345678", 150),
        PayPal("usuario@correo.com", 85)
    ]
    
    for pago in pagos:
        print(pago.procesarPago())

if __name__ == "__main__":
    main()
