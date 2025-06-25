from .categoria_model import CategoriaModel

class CategoriaController:
    @staticmethod
    def get_all():
        return CategoriaModel.get_all()

    @staticmethod
    def get_one(id):
        return CategoriaModel(id=id).get_by_id()

    @staticmethod
    def crear(data):
        categoria = CategoriaModel(descripcion=data['descripcion'])
        return categoria.create()

    @staticmethod
    def modificar(data):
        categoria = CategoriaModel(id=data['id'], descripcion=data['descripcion'])
        return categoria.update()

    @staticmethod
    def eliminar(id):
        return CategoriaModel.delete(id)