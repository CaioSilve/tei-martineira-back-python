from flask import Flask
from flask_cors import CORS

from database import db
# Não remover os imports de Models
from Models.AnimalModel import AnimalModel
from Models.ClienteModel import ClienteModel
from Models.ExameModel import ExameModel
from Models.PedidoModel import PedidoModel
from Models.ProdutoModel import ProdutoModel
from Models.UsuarioModel import UsuarioModel
from Resources.AnimalResource import bp_animal
from Resources.ClienteResource import bp_cliente
from Resources.EIResource import bp_export
from Resources.ExameResource import bp_exame
from Resources.PedidoResource import bp_pedido
from Resources.ProdutoResource import bp_produto
from Resources.UsuarioResource import bp_usuario

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost:5432/tei-martineira-base'
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False

@app.before_first_request
def create_database():
    db.create_all()

app.register_blueprint(bp_usuario, url_prefix="/usuario")
app.register_blueprint(bp_cliente, url_prefix="/cliente")
app.register_blueprint(bp_animal, url_prefix="/animal")
app.register_blueprint(bp_exame, url_prefix="/exame")
app.register_blueprint(bp_produto, url_prefix="/produto")
app.register_blueprint(bp_pedido, url_prefix="/pedido")
app.register_blueprint(bp_export, url_prefix="/utils")


if __name__ == '__main__':
    from database import db
    db.init_app(app)
    
    app.run(port=5002, debug=True)