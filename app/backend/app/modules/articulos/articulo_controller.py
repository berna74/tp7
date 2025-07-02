from .articulo_model import ArticuloModel
from app.modules.marca.marca_model import MarcaModel
<<<<<<< HEAD
from app.modules.proveedor.proveedor_model import ProveedorModel
from app.modules.categoria.categoria_model import CategoriaModel
=======
>>>>>>> 44655ba784151407743993c5d33dcd7f4d2e6ccb

class ArticuloController:
     @staticmethod
     def get_all():
        articulos = ArticuloModel.get_all()
        return articulos
    
     @staticmethod
     def get_one(id):
<<<<<<< HEAD
        # CORRECCIÓN: Se debe llamar al método estático directamente, no desde una instancia.
        articulo = ArticuloModel.get_by_id(id)
        return articulo

     @staticmethod
     def crear(data:dict):
        """
        Espera un diccionario con: descripcion, precio, stock, marca_id, proveedor_id, categoria_ids (lista de ints)
        """
        try:
            marca_data = MarcaModel.get_by_id(data['marca_id'])
            if not marca_data: return {'mensaje': f"Marca con id {data['marca_id']} no encontrada"}, 404
            
            proveedor_data = ProveedorModel.get_by_id(data['proveedor_id'])
            if not proveedor_data: return {'mensaje': f"Proveedor con id {data['proveedor_id']} no encontrado"}, 404
            
            categorias_obj = []
            if 'categoria_ids' in data and data['categoria_ids']:
                for cat_id in data['categoria_ids']:
                    cat_data = CategoriaModel.get_by_id(cat_id)
                    if cat_data:
                        categorias_obj.append(CategoriaModel.deserializar(cat_data))
            
            articulo = ArticuloModel(
                descripcion=data['descripcion'],
                precio=data['precio'],
                stock=data['stock'],
                marca=MarcaModel.deserializar(marca_data),
                proveedor=ProveedorModel.deserializar(proveedor_data),
                categorias=categorias_obj
            )
            
            if articulo.create():
                return {'mensaje': 'Artículo creado correctamente', 'articulo': articulo.serializar()}, 201
            else:
                return {'mensaje': 'Error al crear el artículo'}, 500

        except KeyError as e:
            return {'mensaje': f'Falta el campo requerido: {e}'}, 400
        except Exception as exc:
            return {'mensaje': f'Error inesperado: {exc}'}, 500
        
     @staticmethod
     def modificar(id: int, data:dict):
        try:
            marca_data = MarcaModel.get_by_id(data['marca_id'])
            if not marca_data: return {'mensaje': f"Marca con id {data['marca_id']} no encontrada"}, 404
            
            proveedor_data = ProveedorModel.get_by_id(data['proveedor_id'])
            if not proveedor_data: return {'mensaje': f"Proveedor con id {data['proveedor_id']} no encontrado"}, 404
            
            categorias_obj = []
            if 'categoria_ids' in data and data['categoria_ids']:
                for cat_id in data['categoria_ids']:
                    cat_data = CategoriaModel.get_by_id(cat_id)
                    if cat_data:
                        categorias_obj.append(CategoriaModel.deserializar(cat_data))
            
            articulo = ArticuloModel(id=id, descripcion=data['descripcion'], precio=data['precio'], stock=data['stock'], marca=MarcaModel.deserializar(marca_data), proveedor=ProveedorModel.deserializar(proveedor_data), categorias=categorias_obj)
            
            if articulo.update():
                return {'mensaje': 'Artículo modificado correctamente', 'articulo': articulo.serializar()}, 200
            else:
                return {'mensaje': 'Error al modificar el artículo'}, 500
        except KeyError as e:
            return {'mensaje': f'Falta el campo requerido: {e}'}, 400
        except Exception as exc:
            return {'mensaje': f'Error inesperado: {exc}'}, 500
        
     @staticmethod    
     def eliminar(id):
        # CORRECCIÓN: El método se llamaba 'delete' pero no existía en el modelo.
        # Lo crearemos en el modelo y lo llamaremos desde aquí.
        if ArticuloModel.delete(id):
            return {'mensaje':"artículo eliminado con éxito"}, 200
        return {'mensaje':"error al eliminar un artículo"}, 500
=======
        articulo = ArticuloModel(id=id).get_by_id()
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
>>>>>>> 44655ba784151407743993c5d33dcd7f4d2e6ccb
