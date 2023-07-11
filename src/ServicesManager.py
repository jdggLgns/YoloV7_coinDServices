#!/home/ubuntu/envyolo/bin/python3
import json
from flask import Flask, request
from RegisterUser import GestionUsuarios
from ProductServices import GestionProductos

app = Flask(__name__)


@app.route('/register', methods=['POST'])
def register():
        data = request.get_json()
        name = data.get('name')
        mail = data.get('mail')
        userid = data.get('userid')
        password = data.get('password')

        all_success = GestionUsuarios.register(name, mail, userid, password)
        response = {'success': all_success}
        return json.dumps(response)


@app.route('/login', methods=['POST'])
def login():
        data = request.get_json()
        userid = data.get('userid')
        password = data.get('password')

        response = GestionUsuarios.login(userid, password)
        return json.dumps(response)


#Create
@app.route('/product', methods=['POST'])
def register():
        data = request.get_json()
        userid = data.get('userid')
        descripcion = data.get('descripcion')
        precio = data.get('precio')

        all_success = False
        id = GestionProductos.crear(_userid=userid, _descripcion=descripcion, _precio=precio)
        if id:
                all_success = True
        response = {'success': all_success, 'id': id}
        return json.dumps(response)


@app.route('/product', methods=['POST'])
def crear_producto():
        data = request.get_json()
        userid = data.get('userid')
        descripcion = data.get('descripcion')
        precio = data.get('precio')

        all_success = False
        id = GestionProductos.crear(_userid=userid, _descripcion=descripcion, _precio=precio)
        if id:
                all_success = True
        response = {'success': all_success, 'id': id}
        return jsonify(response)


@app.route('/producto/<int:id>', methods=['DELETE'])
def baja_producto(id):
        all_success = GestionProductos.eliminar(id)
        response = {'success': all_success}
        return jsonify(response)


@app.route('/producto/<int:id>', methods=['PUT'])
def modificar_producto(id):
        data = request.get_json()
        descripcion = data.get('descripcion')
        precio = data.get('precio')
        all_success = GestionProductos.actualizar(_id=id, _descripcion=descripcion, _precio=precio)
        response = {'success': all_success}
        return jsonify(response)


@app.route('/productos/usuario/<int:userid>', methods=['GET'])
def modificar_producto(userid):
        productos = GestionProductos.listar_by_user(_userid=userid)
        response = {'success': True, 'productos': productos}
        return jsonify(response)


@app.route('/productos/<int:id>', methods=['GET'])
def modificar_producto(id):
        producto = GestionProductos.obtener_por_id(_id=id)
        response = {'success': True, 'producto': producto}
        return jsonify(response)


if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5003)
