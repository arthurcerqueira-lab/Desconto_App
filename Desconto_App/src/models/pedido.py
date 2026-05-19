from src.models.desconto import IDesconto

class Pedido:
    def __init__(self, cliente, desconto: IDesconto):
        self.cliente = cliente
        self.desconto = desconto
        self.val_valor_original = 0.0

    def valor_final(self, valor) -> float:
        self.val_valor_original = valor
        return self.val_valor_original - self.desconto.calcular(self.val_valor_original)
