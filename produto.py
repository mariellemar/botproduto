class Produto():
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    
    def exibir(self):
        return f"{self.__quantidade}X {self.__nome} - R${self.__preco}"


    def atualizar(self, nome=None, preco=None, quantidade=None):
        if nome is not None:
            self.__nome = nome
        if preco is not None:
            self.__preco = preco
        if quantidade is not None:
            self.__quantidade = quantidade
        return f"Produto atualizado: {self.__quantidade}X {self.__nome} - R${self.__preco}"

