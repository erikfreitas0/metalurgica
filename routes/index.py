from routes.produtoRoutes import produto
from routes.usuarioRoutes import usuario
from routes.vendedorRoutes import vendedor



def default_routes(app):
    produto(app)
    usuario(app)
    vendedor(app)