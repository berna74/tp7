from flask import Blueprint, request, jsonify
from .articulo_controller import ArticuloController

articulos_bp=Blueprint("articulos", __name__)

@articulos_bp.route("/articulos/")
def get_all():
    try:
        articulos = ArticuloController.get_all()
        # El controlador devuelve una lista en caso de éxito (incluso vacía) o un diccionario en caso de error.
        if isinstance(articulos, list):
            return jsonify(articulos), 200
        else:
            # Si no es una lista, es un diccionario de error del modelo.
            return jsonify(articulos), 500
    except Exception as exc:
         return jsonify({'mensaje': f" error : {str(exc)}"}), 500
@articulos_bp.route("/articulos/<int:id>")
def get_one(id):
    try:
        articulo = ArticuloController.get_one(id)
        if articulo:
            return jsonify(articulo), 200
        else:
            return jsonify({'mensaje': 'no se encontro el artículo'}),404
        
    except Exception as exc:
         return jsonify({'mensaje': f" error : {str(exc)}"}), 500
@articulos_bp.route("/articulos/", methods=["POST"])
def crear():
    try:
        data = request.get_json()
        if data is None:
            return  jsonify({'mensaje': "No se recibieron datos"}), 400
        response, status_code = ArticuloController.crear(data)
        return jsonify(response), status_code
    except Exception as exc:
         return jsonify({'mensaje': f" error : {str(exc)}"}), 500
    
@articulos_bp.route("/articulos/<int:id>", methods=["PUT"])
def modificar(id):
    try:
        data = request.get_json()
        if data is None:
            return jsonify({'mensaje': "No se recibieron datos"}), 400
        response, status_code = ArticuloController.modificar(id, data)
        return jsonify(response), status_code
    except Exception as exc:
         return jsonify({'mensaje': f" error : {str(exc)}"}), 500

@articulos_bp.route("/articulos/<int:id>", methods=["DELETE"])
def eliminar(id):
    try:
        response, status_code = ArticuloController.eliminar(id)
        return jsonify(response), status_code
    except Exception as exc:
        return jsonify({'mensaje': f"error: {str(exc)}"}), 500
