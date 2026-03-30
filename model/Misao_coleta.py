from model.Status import Status_Missao
from model.missao import Missao

class MissaoColeta (Missao):
    def __init__(self, nome, descricao, recompensa, item, quantidade:int, status=Status_Missao.PENDENTE):
        super().__init__(nome, descricao, recompensa, status)
        self.item_necessario = item
        self.quantidade = quantidade
    
    @property 
    def item_necesario(self):
        return self.__item_necessario
    @item_necesario.setter
    def item_necessario(self, it):
        if not isinstance(it, str):
            raise TypeError("Item precisa ser texto.")
        it = it.split()
        it = ' '.join(it)
        self.__item_necessario = it

    @property 
    def quantidade(self):
        return self.__quantidade
    @quantidade.setter
    def quantidade(self, qt):
        if not isinstance(qt, int):
            raise ValueError("Quantidade precisa ser um número inteiro.")
        self.__quantidade = qt

    def exibir_dados(self):
        return (f"{'='*30}\n--- MISSÃO DE COLETA: ---"
                f"\nNome da Missão: {self.nome}\n"
                f"Descrição: {self.descricao}\n"
                f"Recompensa: {self.recompensa} XP\n"
                f"Status: {self.status.name}\n"
                f"Item necessário: {self.item_necesario}\n"
                f"Quantidade: {self.quantidade}\n{'='*30}")

    def __str__(self):
        return f"{self.nome} ({self.descricao}) XP:[{self.recompensa}] [{self.status.value}], item: {self.item_necesario} X [{self.quantidade}]"
   
    def __eq__(self, outro:object) -> bool:
        if not isinstance(outro, MissaoColeta):
            return False
        return (self.nome == outro.nome and self.descricao == outro.descricao 
                and self.recompensa == outro.recompensa and self.status == outro.status
                and self.item_necesario == outro.item_necesario 
                and self.quantidade == outro.quantidade)
    