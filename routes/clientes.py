from flask import Blueprint, render_template
from database.cliente import CLIENTES

cliente_route = Blueprint('clientes', __name__)

"""
Rota de Clientes

    - /clientes/ (GET) - Listar os clientes
    - /clientes/ (POST) - Inserir o cliente no servidor
    - /clientes/new (GET) - Renderizar o formulario para criar um cliente
    - /clientes/<id> (GET) - Obter os dados de um cliente
    - /clientes/<id>/edit (GET) - Renderizar um formulario para editar um cliente
    - /clientes/<id>/update (PUT) - Atualizar os dados do cliente
    - /clientes/<id>/delete (DELETE) - Delete o registro do usuario  
"""

@cliente_route.route('/')
def lista_clientes():
    """"Listar os clientes"""
    return render_template('lista_clientes.html', clientes=CLIENTES)

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    """Inserir os dados de clientes"""
    pass

@cliente_route.route('/new')
def form_cliente():
    """Formulario para cadastro de clientes"""
    return render_template('form_cliente.html')

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    """Exibir detalhes do cliente"""
    return render_template('detalhe_cliente.html')

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    """Formulario de edição de cliente"""
    return render_template('form_edit_cliente.html')

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    """Atualizar informações do cliente"""
    pass

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    """Deletar informações do cliente"""
    pass

