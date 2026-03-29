from Status import Status_Missao
from missao import Missao

class MissaoCombate (Missao):
    def __init__(self, nome, descricao, recompensa, inimigos_a_derrotar:int, inimigo:str, status=Status_Missao.PENDENTE):
        super().__init__(nome, descricao, recompensa, status)
        self.inimigos_a_derrotar = inimigos_a_derrotar
        self.inimigo = inimigo

    
