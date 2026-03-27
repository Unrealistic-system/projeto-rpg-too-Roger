class missao:
    def __init__(self, nome, descricao, recompensa):
        self.nome = nome
        self.descricao = descricao
        self.recompensa = recompensa
        self.status = "PENDENTE"

        self.nome = nome
        self.descricao = descricao
        self.recompensa = recompensa

    #PROPERTY's -> esse é o getter, pra poder receber de volta os dados
    #SETTER's -> é como gravar os dados do objeto
    # NOME:
    @property 
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, novo_nome):
        if not isinstance(novo_nome, str):
            raise TypeError ("Nome precisa ser texto!!!")
        novo_nome = novo_nome.split()# separa
        novo_nome = ' '.join(novo_nome)# junta sem espaço a mais
        if not novo_nome: # pega qualquer coisa, " " ou none tmb
            raise ValueError ("Nome é obrigatório!!!")
        self._nome = novo_nome
        
    @property
    def descricao(self):
        return self._descricao
    @property
    def recompensa(self):
        return self._recompensa
    @property
    def status(self):
        return self._status
    
    @descricao.setter
    def descricao(self, n_desc):
        if not isinstance(n_desc, str):
            raise TypeError ("descrição precisa ser texto!!!")
        n_desc = n_desc.split()
        n_desc = ' '.join(n_desc)
        if  not n_desc:
            raise ValueError ("Descrição é obrigatória!!!")
        self._descricao = n_desc

    @recompensa.setter
    def recompensa(self, n_rec):
        if not isinstance(n_rec, int):
            raise TypeError("Recompensa precisa ser número inteiro.")
        if 0 <= n_rec > 50:
            raise Exception ("Recompensa precisa ser positiva e menor que 50!!!")
        self._recompensa = n_rec

    @status.setter
    def status(self, n_st):
        if not isinstance(n_st, str):
            raise TypeError("O status precisa ser texto!!!")
        n_st = n_st.upper().strip()# maiusculo e sem espaço extra
        st_posssivel = ("PENDENTE", "EM ANDAMENTO", "CONCLUIDA")
        if n_st in st_posssivel:
            self._status = n_st
        else:
            raise ValueError(f"Status inválido! Use uma destas opções: {st_posssivel}")


    def exibir_dados(self):
        return f"{'='*30}\n--- MISSÃO ---\nNome da Missão: {self.nome}\nDescrição: {self.descricao}\nRecompensa: {self.recompensa} XP\nStatus: {self.status}\n{'='*30}"# posso usar contas pra exibir varios caracteres iguais :D


    def __str__(self):
        return f"{self.nome} ({self.descricao}) [{self.recompensa}] [{self.status}]"
   
    def __eq__(self, outro:object) -> bool:
        if not isinstance(outro, missao):
            return False
        return self.nome == outro.nome and self.descricao == outro.descricao and self.recompensa == outro.recompensa and self.status == outro.status
    
def entrada_missao() -> missao:
    while True:
        try:
            nome = input(f"{'-'*10}\nDigite o nome da Misão: ")
            desc = input(f"{'-'*10}\nDigite a descrição: ")
            rec = int(input(f"{'-'*10}\nDigite a recompensa: "))
            st = input(f"{'-'*10}\nDigite o status:\ntipos: PENDENTE, EM ANDAMENTO OU CONCLUIDA\nou pule com enter: ")
            if not st:
                missao_criada = missao(nome, desc, rec) # Usa default "PENDENTE"
            else:
                missao_criada = missao(nome, desc, rec, st)
            return missao_criada
        except TypeError as e:
            print(f"{'+'*10}\nErro de Digitação: {e}\n{'+'*10}")
        except ValueError as e:
            print(f"{'+'*10}\nValor Inválido: {e}\n{'+'*10}")
        except Exception as e:
            print(f"{'+'*10}\nERRO: {e}\n{'+'*10}")