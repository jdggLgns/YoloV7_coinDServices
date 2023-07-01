#!/home/ubuntu/envyolo/bin/python3
import json
from flask import Flask
from flask import request
from RegisterUser import GestionUsuarios


app = Flask(__name__)


@app.route('/register', methods=['POST'])
def register():
        data = request.get_json()
        name = data.get('name')
        mail = data.get('mail')
        userid = data.get('userid')
        password = data.get('password')

        all_success = GestionUsuarios.register(name,mail,userid,password)
        response = {'success': all_success}
        return json.dumps(response)


@app.route('/login', methods=['POST'])
def login():
        data = request.get_json()
        userid = data.get('userid')
        password = data.get('password')

        response = GestionUsuarios.login(userid,password)
        return json.dumps(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)