from botcity.web import WebBot, Browser, By
from botcity.maestro import *
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker

from produto import Produto

BotMaestroSDK.RAISE_NOT_CONNECTED = False

fake = Faker

class Funcoes():
    @staticmethod
    def inserir_produto(bot, produto):
        # Simula o preenchimento do formulário no navegador
        bot.click(By.ID, "nome")
        bot.paste(produto['nome'])

        bot.click(By.ID, "preco")
        bot.paste(str(produto['preco']))

        bot.click(By.ID, "quantidade")
        bot.paste(str(produto['quantidade']))

        bot.click(By.XPATH, "//button[@type='submit']") 

    def listar_produto(produto, cont):
       print(f"Produto {cont}: {produto.exibir()}")


    def atualizar_produto():
        pass


    @staticmethod
    def criar_produto(bot):
        nome = fake.word().capitalize()
        preco = round(fake.random_number(digits=2) + fake.random.random(), 2)
        quantidade = fake.random_int(min=1, max=100)
    
        produto = Produto(nome, preco, quantidade)
        return produto





def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot.driver_path = ChromeDriverManager().install()

    bot = WebBot()
    bot.headless = False
    bot.browse("http://127.0.0.1:5000")

    # Implement here your logic...
    for i in range (20):
        produto = Funcoes.criar_produto(bot)
        Funcoes.inserir_produto(bot, produto)
        Funcoes.listar_produto(produto, i)
        

    # Wait 3 seconds before closing
    bot.wait(3000)
    bot.stop_browser()


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
