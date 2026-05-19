from src.app.entities.pedido import Pedido
from Desconto_App.src.app.framework.database.connection import DatabaseConnection

class PedidoRepository:
    """Classe de repositório para armazenar e gerenciar pedidos."""

    def __init__(self, database: DatabaseConnection):
        self.database = database

    def adicionar_pedido(self, pedido: Pedido):
        self.database.pedidos.append(pedido)

    def listar_pedidos(self):
        return self.database.pedidos
