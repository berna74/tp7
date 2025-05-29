from app.database.conect_db import ConectDB
from app.modules.marca.marca_model import MarcaModel
from app.modules.categoria.categoria_model import CategoriaModel

class ArticuloModel:
        ## constructor
    def __init__(self, id:int=0, descripcion:str="", precio:float=0.0, stock:int=0, marca: object=MarcaModel, categoria:object=CategoriaModel):
        self.id=id
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.marca = MarcaModel
        self.categoria = CategoriaModel
        
        
        
    def serializar(self) -> dict:
        return {
            'id': self.id,
            'descripcion':self.descripcion,
            'precio':self.precio,
            'stock':self.stock,
            'marca': self.marca.serializar(),
            'categoria': self.categoria.serializar()
        }
    
    @staticmethod
    def deserializar(data:dict):
        return ArticuloModel(
            id=data['id'], 
            descripcion=data['descripcion'],
            precio=data['precio'], 
            stock=data['stock'],  
            marca=data['marca']       
        )
        
    
    @staticmethod
    def get_all():
        cnx = ConectDB.get_connect()
        if cnx is None:
           return {'mensaje': 'No se pudo conectar a la base de datos'}
        with cnx.cursor(dictionary=True) as cursor:
            try:
                # ejecuto la query
                cursor.execute(f"SELECT * FROM articulos")
                # guardo en una variable el resultado
                rows = cursor.fetchall()
                # lista de diccionarios
                articulos = []
                if rows:
                    for row in rows:
                        marca_row = MarcaModel(id=row['marca_id'])
                        marca = marca_row.get_by_id(row['marca_id'])
                        row['marca'] = marca
                        articulos.append(row)
                    return articulos                
                return False
            # si ocurre una excepción, solo imprime el error y no devuelve nada
            except Exception as exc:
                return {'mensaje': f" error al listar artículos {exc}"}
            finally:
                cnx.close()
        
    def get_by_id(self):
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                # ejecuto la query
                cursor.execute("SELECT * FROM articulos where id = %s", (self.id,))
                # guardo en una variable el resultado
                row = cursor.fetchone()
                if row:
                    marca_row = MarcaModel(id=row['marca_id'])
                    marca = marca_row.get_by_id(row['marca_id'])
                    row['marca'] = marca
                    return row
                return False
            except Exception as exc:
                return {'mensaje':f" error al buscar un artículo {exc}"}
            finally:
                cnx.close()
                
    def create(self):
        cnx = ConectDB.get_connect()
        with cnx.cursor() as cursor:
            try:
                # ejecuto la query
                cursor.execute("INSERT INTO articulos (descripcion, precio, stock, marca_id) VALUES (%s,%s,%s,%s)", 
                               (self.descripcion, self.precio, self.stock, self.marca.id))
                result = cursor.rowcount
                cnx.commit()
                if result > 0:
                    return True
                return False
                
            except Exception as exc:
                cnx.rollback()
                print(f" error crear un producto {exc}")
            finally:
                cnx.close()
        
    def update(self):
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                # ejecuto la query
                cursor.execute("UPDATE articulos SET descripcion = %s, precio = %s, stock= %s , marca_id=%s where id=%s ", 
                               (self.descripcion, self.precio, self.stock, self.id, self.marca.id))
                result = cursor.rowcount
                cnx.commit()
                
                if result > 0:
                    return True
                return False
                
            except Exception as exc:
                cnx.rollback()
                return {'mensaje':f" error al buscar un artículo {exc}"}
            finally:
                cnx.close()
                
    @staticmethod
    def delete(id:int):
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                # ejecuto la query
                cursor.execute("DELETE FROM articulos where id = %s ", 
                               (id,))
                result = cursor.rowcount
                cnx.commit()
                if result > 0:
                    return True
                return False
            except Exception as exc:
                cnx.rollback()
                return {'mensaje':f" error al buscar un artículo {exc}"}
            finally:
                cnx.close()    