import json


def tratar_dados_usuario(dados):
    dados.add_argument('usuario')
    dados.add_argument('senha')
    dados.add_argument('nome')
    dados.add_argument('sobrenome')

    return dados.parse_args()

def tratar_dados_usuario_update(dados):
    dados.add_argument('senha')
    dados.add_argument('nome')
    dados.add_argument('sobrenome')

    return dados.parse_args()

def tratar_dados_cliente(dados):
    dados.add_argument('nome')
    dados.add_argument('email')
    dados.add_argument('cpf')
    dados.add_argument('cidade')
    dados.add_argument('endereco')
    dados.add_argument('celular')
    dados.add_argument('telefone')

    return dados.parse_args()

def tratar_dados_animal(dados):
    dados.add_argument('nome')
    dados.add_argument('tipo')
    dados.add_argument('raca')
    dados.add_argument('idade')
    dados.add_argument('dono_id')

    return dados.parse_args()

def tratar_dados_animal_update(dados):
    dados.add_argument('nome')
    dados.add_argument('tipo')
    dados.add_argument('raca')
    dados.add_argument('idade')

    return dados.parse_args()

def tratar_dados_exame(dados):
    dados.add_argument('paciente')
    dados.add_argument('procedimento')
    dados.add_argument('resultado')
    dados.add_argument('data')
    dados.add_argument('horaInicio')
    dados.add_argument('horaFim')

    return dados.parse_args()

def tratar_dados_exame_update(dados):
    dados.add_argument('procedimento')
    dados.add_argument('resultado')
    dados.add_argument('data')
    dados.add_argument('horaInicio')
    dados.add_argument('horaFim')

    return dados.parse_args()

def tratar_dados_produto(dados):
    dados.add_argument('desc')
    dados.add_argument('tipo')
    dados.add_argument('valorUnit')
    dados.add_argument('qtde')
    dados.add_argument('validade')

    return dados.parse_args()

def tratar_dados_pedido(dados):
    dados.add_argument('cliente_id')
    dados.add_argument('data')

    return dados.parse_args()
    
def tratar_dados_pedido_update(dados):
    dados.add_argument('data')

    return dados.parse_args()

def tratar_dados_pedido_add_produto(dados):
    dados.add_argument('produto_id')
    dados.add_argument('pedido_id')

    return dados.parse_args() 

def tratar_import(dados):
    dados.add_argument('animais', action='append')
    dados.add_argument('clientes', action='append')
    dados.add_argument('exames', action='append')
    dados.add_argument('pedidos', action='append')
    dados.add_argument('produtos', action='append')
    dados.add_argument('usuarios', action='append')
    dados = dados.parse_args()
    dados_tratados = json.dumps(dados)
    dados_tratados = json.loads(dados_tratados)
    
    for key, values in dados_tratados.items():
        tratando = json.dumps(dados_tratados[key])
        dados_tratados[key] = json.loads(tratando)

    animais = list()
    for animal in dados_tratados["animais"]:
        animal = animal.replace("\'", "\"")
        animal = json.loads(animal)
        animais.append(animal)
    dados_tratados["animais"] = animais

    exames = list()
    for exame in dados_tratados["exames"]:
        exame = exame.replace("\'", "\"")
        exame = json.loads(exame)
        exames.append(exame)
    dados_tratados["exames"] = exames

    produtos = list()
    for produto in dados_tratados["produtos"]:
        produto = produto.replace("\'", "\"")
        produto = json.loads(produto)
        produtos.append(produto)
    dados_tratados["produtos"] = produtos

    usuarios = list()
    for usuario in dados_tratados["usuarios"]:
        usuario = usuario.replace("\'", "\"")
        usuario = json.loads(usuario)
        usuarios.append(usuario)
    dados_tratados["usuarios"] = usuarios

    pedidos = list()
    for pedido in dados_tratados["pedidos"]:
        pedido = pedido.replace("\'", "\"")
        pedido = json.loads(pedido)
        pedidos.append(pedido)
    dados_tratados["pedidos"] = pedidos

    clientes = list()
    for cliente in dados_tratados["clientes"]:
        cliente = cliente.replace("\'", "\"")
        cliente = json.loads(cliente)
        clientes.append(cliente)
    dados_tratados["clientes"] = clientes

    return dados_tratados