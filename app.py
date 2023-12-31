from flask import *
from esquema import *

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False


#pegar dados da url
@app.route('/add/user', methods=['POST'])
def addUser():
    nome = request.form['name']
    email = request.form['email']
    cpf = request.form['cpf']
    senha = request.form['senha']

    user = Usuarios(
        nome = nome,
        email = email,
        cpf = cpf,
        senha = senha
    )   
    user.save()

    return 'feito'

@app.route('/add/address', methods=['POST'])
def addAddress():
    rua = request.form['rua']
    cidade = request.form['cidade']
    bairro = request.form['bairro']
    numero = request.form['numero']
    cep = request.form['cep']
    complemento = request.form['complemento']
    usuario = request.form['usuario_id']

    endereco = Enderecos(
        rua = rua,
        cidade = cidade,
        bairro = bairro,
        numero = numero,
        cep = cep,
        complemento = complemento,
        usuario = Usuarios.select().where(Usuarios.nome == usuario).get()
    )   
    endereco.save()

    return 'feito'

@app.route('/add/products', methods=['POST'])
def addProducts():
    nome_produto = request.form['nome_produto']
    valor = request.form['valor']
    categoria_id = request.form['categoria']
    quantidade = request.form['quantidade']

    produto = Produtos(
        nome_produto = nome_produto,
        valor = valor,
        categoria = Categoria.select().where(Categoria.nome == categoria_id).get(),
        quantidade = quantidade
    )   
    produto.save()

    return 'feito'


@app.route('/add/category', methods=['POST'])
def addCategory():
    descricao= request.form['descricao']

    categoria = Categoria(
        decricao = descricao
    )   
    categoria.save()

#################################################

@app.route('/')
def index():

    return 'ok'


if __name__ == '__main__':
    app.run(debug=True)
