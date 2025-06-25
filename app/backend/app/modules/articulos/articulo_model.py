from app.database.conect_db import ConectDB
from app.modules.marca.marca_model import MarcaModel
from app.modules.categoria.categoria_model import CategoriaModel
from app.modules.proveedor.proveedor_model import ProveedorModel

class ArticuloModel:
    def __init__(self, id: int = 0, descripcion: str = "", precio: float = 0.0, stock: int = 0, 
                 marca: object = MarcaModel, proveedor: object = ProveedorModel, categorias: list = []):
        self.id = id
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.marca = marca
        self.proveedor = proveedor
        self.categorias = categorias  # Lista de CategoriaModel

    def serializar(self) -> dict:
        return {
            'id': self.id,
            'descripcion': self.descripcion,
            'precio': self.precio,
            'stock': self.stock,
            'marca': self.marca.serializar(),
            'proveedor': self.proveedor.serializar(),
            'categorias': [categoria.serializar() for categoria in self.categorias]
        }

    @staticmethod
    def deserializar(data: dict):
        return ArticuloModel(
            id=data['id'],
            descripcion=data['descripcion'],
            precio=data['precio'],
            stock=data['stock'],
            marca=MarcaModel.deserializar(data['marca']),
            proveedor=ProveedorModel.deserializar(data['proveedor']),
            categorias=[CategoriaModel.deserializar(c) for c in data['categorias']]
        )

    @staticmethod
    def get_all():
        cnx = ConectDB.get_connect()
        if cnx is None:
            return {'mensaje': 'No se pudo conectar a la base de datos'}
        try:
            with cnx.cursor(dictionary=True) as cursor:
                # Obtengo todos los artículos
                cursor.execute("SELECT * FROM ARTICULOS")
                rows = cursor.fetchall()
                articulos = []
                if rows:
                    for row in rows:
                        # Obtengo la marca asociada
                        marca_row = MarcaModel.get_by_id(row['marca_id'])
                        
                        # Obtengo el proveedor asociado
                        proveedor_row = ProveedorModel.get_by_id(row['proveedor_id'])
                        
                        # Obtengo las categorías asociadas
                        cursor.execute("SELECT categoria_id FROM ARTICULOS_CATEGORIAS WHERE articulo_id = %s", (row['id'],))
                        categoria_ids = cursor.fetchall()
                        categorias = [CategoriaModel.get_by_id(c['categoria_id']) for c in categoria_ids]
                        
                        # Construyo el artículo con los datos obtenidos
                        articulo = ArticuloModel(
                            id=row['id'],
                            descripcion=row['descripcion'],
                            precio=row['precio'],
                            stock=row['stock'],
                            marca=marca_row,
                            proveedor=proveedor_row,
                            categorias=categorias
                        )
                        articulos.append(articulo.serializar())
                    return articulos
                return []
        except Exception as exc:
            return {'mensaje': f"Error al listar artículos: {exc}"}
        finally:
            cnx.close()

    @staticmethod
    def get_by_id(id):
        cnx = ConectDB.get_connect()
        if cnx is None:
            return {'mensaje': 'No se pudo conectar a la base de datos'}
        try:
            with cnx.cursor(dictionary=True) as cursor:
                # Obtengo el artículo por ID
                cursor.execute("SELECT * FROM articulos WHERE id = %s", (self.id,))
                row = cursor.fetchone()
                if row:
                       marca_row = MarcaModel.get_by_id(row['marca_id'])
                       proveedor_row = ProveedorModel.get_by_id(row['proveedor_id'])
                       cursor.execute("SELECT categoria_id FROM articulos_categorias WHERE articulo_id = %s", (row['id'],))
                       categoria_ids = cursor.fetchall()
                       categorias = [CategoriaModel.get_by_id(c['categoria_id']) for c in categoria_ids]
                       articulo = ArticuloModel(
                           id=row['id'],
                           descripcion=row['descripcion'],
                           precio=row['precio'],
                           stock=row['stock'],
                           marca=marca_row,
                           proveedor=proveedor_row,
                           categorias=categorias
                       )
                       return articulo.serializar()
                return {}
        except Exception as exc:
            return {'mensaje': f"Error al buscar un artículo: {exc}"}
        finally:
            cnx.close()