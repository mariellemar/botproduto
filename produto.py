class Produto():
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    
    def exibir(self):
        return f"{self.__quantidade}X {self.__nome} - R${self.__preco:.2f}"


    def atualizar(self, nome=None, preco=None, quantidade=None):
        if nome is not None:
            self.__nome = nome
        if preco is not None:
            self.__preco = preco
        if quantidade is not None:
            self.__quantidade = quantidade
        return f"Produto atualizado: {self.__quantidade}X {self.__nome} - R${self.__preco}"

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
        
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, novo_preco):
        self.__preco = novo_preco
        
    @property
    def quantidade(self):
        return self.__quantidade
    
    @quantidade.setter
    def quantidade(self, nova_quantidade):
        self.__quantidade = nova_quantidade