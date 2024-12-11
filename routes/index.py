from routes.produtoRoutes import produto
from routes.usuarioRoutes import usuario
from routes.vendedorRoutes import vendedor
from routes.loginRoutes import login



def default_routes(app):
    produto(app)
    usuario(app)
    vendedor(app)
    login(app)