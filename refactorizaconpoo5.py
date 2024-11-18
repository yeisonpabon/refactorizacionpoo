class MetodoDePago:
    def procesar_pago(self, monto):
        raise NotImplementedError("Las subclases deben implementar este método")


class PagoConTarjetaDeCredito(MetodoDePago):
    def procesar_pago(self, monto):
        print(f"Procesando pago con tarjeta de crédito de ${monto}")

class PagoConPayPal(MetodoDePago):
    def procesar_pago(self, monto):
        print(f"Procesando pago con PayPal de ${monto}")

class PagoConBitcoin(MetodoDePago):
    def procesar_pago(self, monto):
        print(f"Procesando pago con Bitcoin de ${monto}")

pagos = [
    PagoConTarjetaDeCredito(),
    PagoConPayPal(),
    PagoConBitcoin()
]

for pago in pagos:
    pago.procesar_pago(100)
