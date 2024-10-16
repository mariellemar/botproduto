from flask import Flask, render_template, request, redirect, url_for
from produto import Produto

app = Flask(__name__)

produtos = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form.get('nome')
        preco = float(request.form.get('preco'))
        quantidade = int(request.form.get('quantidade'))

        produto = Produto(nome, preco, quantidade)

        produtos.append(produto)
    return render_template('index.html', produtos=produtos)


@app.route('/atualizar/<int:indice>', methods = ['GET', 'POST'])
def atualizar_produto(indice):
    produto = produtos[indice]
    
    if request.method == 'POST':
        nome = request.form['nome']
        preco = request.form['preco']
        quantidade = request.form['quantidade']
        
        produto.atualizar(nome=nome if nome else None,
                        preco=float(preco) if preco else None,
                        quantidade=int(quantidade) if quantidade else None
                        )
    
        return redirect(url_for('index'))

    return render_template('atualizar.html', produto=produto, indice=indice)

if __name__ == '__main__':
    app.run()