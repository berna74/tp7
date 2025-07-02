from .articulo_model import ArticuloModel
from app.modules.marca.marca_model import MarcaModel

class ArticuloController:
     @staticmethod
     def get_all():
        articulos = ArticuloModel.get_all()
        return articulos
    
     @staticmethod
     def get_one(id):
        articulo = ArticuloModel.get_by_id(id)
        return articulo
     @staticmethod
     def crear(data:dict):
        marca_row = MarcaModel.get_by_id(data['marca_id'])
        marca = MarcaModel.deserializar(marca_row)
        articulo = ArticuloModel( descripcion=data['descripcion'], precio=data['precio'], stock=data['stock'], marca=marca)
        result= articulo.create()
        return result
        
     @staticmethod
     def modificar(data:dict):
         marca_row = MarcaModel.get_by_id(data['marca_id'])
         marca = MarcaModel.deserializar(marca_row)
         data['marca'] = marca         
         articulo = ArticuloModel.deserializar(data)
         result = articulo.update()
         return result
        
     @staticmethod    
     def eliminar(id):
        result = ArticuloModel.delete(id)
        return result