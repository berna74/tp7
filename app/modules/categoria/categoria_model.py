from app.database.conect_db import ConectDB

class CategoriaModel:
    def __init__(self, id: int = 0, descripcion: str = ""):
        self.id = id
        self.descripcion = descripcion

    def serializar(self) -> dict:
        return {
            "id": self.id,
            "descripcion": self.descripcion
        }

    @staticmethod
    def deserializar(data: dict):
        return CategoriaModel(
            id=data.get("id", 0),
            descripcion=data.get("descripcion", "")
        )

    @staticmethod
    def get_all():
        cnx = ConectDB.get_connect()
        if cnx is None:
            return {'mensaje': 'No se pudo conectar a la base de datos'}
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM categorias")
                rows = cursor.fetchall()
                categorias = []
                if rows:
                    for row in rows:
                        categorias.append(row)
                    return categorias
                return False
            except Exception as exc:
                return {'mensaje': f"error al listar categorías {exc}"}
            finally:
                cnx.close()

    def get_by_id(self):
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM categorias WHERE id = %s", (self.id,))
                row = cursor.fetchone()
                if row:
                    return row
                return False
            except Exception as exc:
                return {'mensaje': f"error al buscar una categoría {exc}"}
            finally:
                cnx.close()

    def create(self):
        cnx = ConectDB.get_connect()
        with cnx.cursor() as cursor:
            try:
                cursor.execute("INSERT INTO categorias (descripcion) VALUES (%s)", (self.descripcion,))
                result = cursor.rowcount
                cnx.commit()
                if result > 0:
                    return True
                return False
            except Exception as exc:
                cnx.rollback()
                print(f"error crear una categoría {exc}")
            finally:
                cnx.close()

    def update(self):
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("UPDATE categorias SET descripcion = %s WHERE id = %s", (self.descripcion, self.id))
                result = cursor.rowcount
                cnx.commit()
                if result > 0:
                    return True
                return False
            except Exception as exc:
                cnx.rollback()
                return {'mensaje': f"error al modificar una categoría {exc}"}
            finally:
                cnx.close()

    @staticmethod
    def delete(id: int):
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("DELETE FROM categorias WHERE id = %s", (id,))
                result = cursor.rowcount
                cnx.commit()
                if result > 0:
                    return True
                return False
            except Exception as exc:
                cnx.rollback()
                return {'mensaje': f"error al eliminar una categoría {exc}"}
            finally:
                cnx.close()