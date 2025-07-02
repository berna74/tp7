from .proveedor_model import ProveedorModel

class ProveedorController:
    @staticmethod
    def get_all():
        return ProveedorModel.get_all()

    @staticmethod
    def get_one(id):
        return ProveedorModel(id=id).get_by_id()

    @staticmethod
    def crear(data):
        proveedor = ProveedorModel(
            nombre=data.get('nombre', ''),
            telefono=data.get('telefono', ''),
            direccion=data.get('direccion', ''),
            email=data.get('email', '')
        )
        return proveedor.create()

    @staticmethod
    def modificar(data):
        proveedor = ProveedorModel(
            id=data['id'],
            nombre=data.get('nombre', ''),
            telefono=data.get('telefono', ''),
            direccion=data.get('direccion', ''),
            email=data.get('email', '')
        )
        return proveedor.update()

    @staticmethod
    def eliminar(id):
        return ProveedorModel.delete(id)