from flask import Flask, render_template, request, redirect, url_for
from produto import Produto

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    produto = None
    if request.method == 'POST':
        nome = request.form.get('nome')
        preco = float(request.form.get('preco'))
        quantidade = int(request.form.get('quantidade'))

        produto = Produto(nome, preco, quantidade)
    
    return render_template('index.html', produto=produto)

if __name__ == '__main__':
    app.run()