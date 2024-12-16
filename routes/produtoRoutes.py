from controllers.produtoController import produto_controller, atualizar_produto

def produto(app):
    # Rota para criar e listar produtos
    app.route('/metalurgica/produto', methods=['POST', 'GET'])(produto_controller)
    
    # Rota para atualizar um produto específico
    app.route('/metalurgica/produto/<int:produto_id>', methods=['PUT'])(atualizar_produto)
    
    # Rota para deletar um produto específico
    app.route('/metalurgica/produto/<int:produto_id>', methods=['DELETE'])(produto_controller)