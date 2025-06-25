from flask import Flask
from flask_cors import CORS
from .modules.articulos.articulo_routes import articulos_bp
from .modules.categoria.categoria_routes import categoria_bp
from .modules.marca.marca_routes import marca_bp
from .modules.proveedor.proveedor_routes import proveedor_bp

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(articulos_bp)
    app.register_blueprint(categoria_bp)
    app.register_blueprint(marca_bp)
    app.register_blueprint(proveedor_bp)
    return app