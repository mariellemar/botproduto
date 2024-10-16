from botcity.web import WebBot, Browser, By
from botcity.maestro import *
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker

from produto import Produto

BotMaestroSDK.RAISE_NOT_CONNECTED = False

fake = Faker('pt_BR')

class Funcoes():
    
    @staticmethod
    def inserir_produto(bot: WebBot, produto: Produto):
        
        input_nome = bot.find_element("nome", By.ID)
        input_nome.send_keys(produto.nome)

        input_preco = bot.find_element("preco", By.ID)
        input_preco.send_keys(str(produto.preco))

        input_quantidade = bot.find_element("quantidade", By.ID)
        input_quantidade.send_keys(str(produto.quantidade))

        submit_btn = bot.find_element("//button[@type='submit']", By.XPATH) 
        submit_btn.click()
        
        
    def listar_produto(produto, cont):
       print(f"Produto {cont+1}: {produto.exibir()}")


    def atualizar_produto(bot: WebBot, indice):
        att_bttn = bot.find_element(f'//*[@id="listaProdutos"]/ul/a[{indice}]', By.XPATH)
        att_bttn.click()
        bot.wait(1000)
        Funcoes.criar_produto
        Funcoes.inserir_produto
        atualizar = bot.find_element("/html/body/div/form/div[4]/button", By.XPATH)
        atualizar.click()

    @staticmethod
    def criar_produto(bot:WebBot):
        nome = f'{fake.word().capitalize()}'
        preco = fake.random_number(digits=2)
        quantidade = fake.random_number(digits=2)
    
        produto = Produto(nome, preco, quantidade)
        return produto





def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")
    
    bot = WebBot()
    
    bot.driver_path = ChromeDriverManager().install()
    
    bot.headless = False
    bot.browse("http://127.0.0.1:5000")

    # Implement here your logic...
    for i in range (20):
        bot.wait(1000)
        produto = Funcoes.criar_produto(bot)
        Funcoes.inserir_produto(bot, produto)
        Funcoes.listar_produto(produto, i)
        if i == 5:
            Funcoes.atualizar_produto(bot, i)
        

    # Wait 3 seconds before closing
    bot.wait(3000)
    bot.stop_browser()


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
