import SqlUtils


class GestionProductos:

    #Devuelve el id del producto creado o None si ocurrio un error
    @staticmethod
    def crear(_userid, _descripcion, _precio, _tipo):
        id = None
        if _userid and _descripcion and _precio and _tipo:
            sql = "INSERT INTO producto (userid, descripcion, precio, tipo) VALUES (%s, %s, %s, %s)"
            parametros = (_userid, _descripcion, _precio, _tipo)
            id = SqlUtils.execInsert(sql,parametros)
        return id


    # devuelve True si se ha podido eliminar correctamente y False en caso contrario
    @staticmethod
    def eliminar(_id):
        all_success = False
        if _id:
            sql = "DELETE FROM producto WHERE id = %s"
            parametros = (_id,)
            all_success = SqlUtils.execDelete(sql, parametros)
        return all_success


    # devuelve True si se ha podido actualizar correctamente y False en caso contrario
    # _id: id del producto a actualizar
    @staticmethod
    def actualizar(_id, _descripcion, _precio):
        all_success = False
        if _id and _descripcion and _precio:
            sql = "UPDATE producto SET descripcion = %s, precio = %s WHERE id = %s"
            parametros = (_descripcion, _precio, _id)
            all_success = SqlUtils.execUpdate(sql, parametros)
        return all_success

    # devuelve todos los productos de un usuario
    @staticmethod
    def listar_by_user(_userid):
        sql = "SELECT id, descripcion, precio, tipo FROM producto WHERE userid = %s"
        parametros = (_userid,)
        rows = SqlUtils.execSelect(sql, parametros)
        productos = []
        try:
            for row in rows:
                producto = {
                    'id': row[0],
                    'descripcion': row[1],
                    'precio': row[2],
                    'tipo': row[3]
                }
                productos.append(producto)
        except BaseException as e:
            productos = []
        return productos


    # devuelve un producto dado su id
    @staticmethod
    def obtener_por_id(_id):
        sql = "SELECT id, descripcion, precio, tipo FROM producto WHERE id = %s"
        parametros = (_id,)
        rows = SqlUtils.execSelect(sql, parametros)
        producto = {}
        try:
            for row in rows:
                producto = {
                    'id': row[0],
                    'descripcion': row[1],
                    'precio': row[2]
                }
        except BaseException as e:
            producto = {}
        return producto
