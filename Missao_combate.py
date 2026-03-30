from Status import Status_Missao
from missao import Missao

class MissaoCombate (Missao):
    def __init__(self, nome, descricao, recompensa, inimigos_a_derrotar:int, inimigo:str, status=Status_Missao.PENDENTE):
        super().__init__(nome, descricao, recompensa, status)
        self.inimigos_a_derrotar = inimigos_a_derrotar
        self.inimigo = inimigo

    @property 
    def inimigo(self):
        return self._inimigo
    
    @inimigo.setter
    def inimigo(self, it):
        if not isinstance(it, str):
            raise TypeError("Inimigo precisa ser string.")
        it = it.split()
        it = ' '.join(it)
        it = it.title() #maiuscula primeira
        self._inimigo = it
    @property
    def inimigos_a_derrotar(self):
        return self._inimigos_a_derrotar
    @inimigos_a_derrotar.setter
    def inimigos_a_derrotar(self, qt):
        if not isinstance(qt, int):
            raise TypeError("Inimigos a derrotar precisa ser inteiro.")
        
