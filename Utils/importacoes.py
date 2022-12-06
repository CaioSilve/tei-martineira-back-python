from Models.AnimalModel import AnimalModel
from Models.ClienteModel import ClienteModel
from Models.ExameModel import ExameModel
from Models.PedidoModel import PedidoModel
from Models.ProdutoModel import ProdutoModel
from Models.UsuarioModel import UsuarioModel


def importar_animal(animais):
    for animal in animais:
        if ClienteModel.find_cliente(animal["dono_id"]):
            animal.pop("id")
            animal = AnimalModel(**animal)
            animal.save_animal()

def importar_cliente(clientes):
    for cliente in clientes:
        cliente.pop("id")
        cliente.pop("animais")
        cliente.pop("pedidos")
        cliente = ClienteModel(**cliente)
        cliente.save_cliente()

def importar_exame(exames):
    for exame in exames:
        if AnimalModel.find_animal(exame["paciente"]):
            exame.pop("id")
            exame = ExameModel(**exame)
            exame.save_exame()

def importar_pedido(pedidos):
    for pedido in pedidos:
        produtos = list()
        pedido_id = 0
        if ClienteModel.find_cliente(pedido["cliente_id"]):
            for produto in pedido["produtos"]:
                produtos.append(produto)

            pedido.pop("produtos")
            pedido_id = pedido["id"]
            pedido.pop("id")
            pedido.pop("precoTotal")

            pedido = PedidoModel(**pedido)
            pedido.save_pedido()

            for produto in produtos:
                produto = ProdutoModel.find_produto(produto["id"])
                if produto:
                    pedido = PedidoModel.find_pedido(pedido_id)
                    if pedido:
                        pedido.add_produto(produto)
                        pedido.save_pedido()

def importar_produto(produtos):
    for produto in produtos:
        produto.pop("id")
        produto = ProdutoModel(**produto)
        produto.save_produto()
def importar_usuario(usuarios):
    for usuario in usuarios:
        if UsuarioModel.find_usuario(usuario["usuario"]) == None:
            usuario.pop("id")
            usuario = UsuarioModel(**usuario)
            usuario.save_usuario()