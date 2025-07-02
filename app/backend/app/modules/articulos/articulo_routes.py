from flask import Blueprint, request, jsonify
from .articulo_controller import ArticuloController

articulos_bp=Blueprint("articulos", __name__)

@articulos_bp.route("/articulos/")
def get_all():
    try:
        articulos = ArticuloController.get_all()
        if articulos:
            return jsonify(articulos), 200
        else:
            return jsonify({'mensaje': 'no se encontraron artículos'}),404
        
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
            return  jsonify({'mensaje': "no se recibieron datos"})
        result = ArticuloController.crear(data)
        if result:
            return jsonify({'mensaje':'artículo creado correctamente'}), 201
        else:
            return jsonify({'mensaje': 'error al crear un artículo'}),500
        
    except Exception as exc:
         return jsonify({'mensaje': f" error : {str(exc)}"}), 500
    
@articulos_bp.route("/articulos/<int:id>", methods=["PUT"])
def modificar(id):
    try:
        data = request.get_json()
        data['id'] = id
        result = ArticuloController.modificar(data)
        if result:
            return jsonify({'mensaje':'artículo modificado correctamente'}), 200
        else:
            return jsonify({'mensaje': 'error al modificar un artículo'}),500
        
    except Exception as exc:
         return jsonify({'mensaje': f" error : {str(exc)}"}), 500

@articulos_bp.route("/articulos/id/<int:id>", methods=["DELETE"])
def eliminar(id):
    try:
        result = ArticuloController.eliminar(id)
        if result:
            return jsonify({'mensaje':"artículo eliminado con éxito"})
        return jsonify({'mensaje':"error al eliminar un artículo"})
    except Exception as exc:
        return jsonify({'mensaje':f"error str{exc}"})
