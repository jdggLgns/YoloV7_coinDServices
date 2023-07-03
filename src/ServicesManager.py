#!/home/ubuntu/envyolo/bin/python3
import json
from random import random
from flask import Flask, send_file, request
from RegisterUser import GestionUsuarios
from Object_detection import object_detection

app = Flask(__name__)
UPLOAD_FOLDER = "files_reception/"

def alphanumeric(number):
        """
        This function allows to generate an alphanumeric text
        :param number: int -- Number of characters in the expected text
        :return: str -- Text of *number* alphanumeric characters
        """
        return ''.join(random.choice('0123456789ABCDEF') for i in range(number))


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


@app.route('/send_image', methods=["POST"])
def send_image():
        if 'image' not in request.files:
                return "No image found in the request", 400

        file = request.files['image']
        image = file.read()  # Obtiene los bytes de la imagen enviada

        alphanumeric_filename = alphanumeric(8) + ".jpg"
        with open(UPLOAD_FOLDER + alphanumeric_filename, "wb") as f:
                f.write(image)

        result = object_detection(UPLOAD_FOLDER).calculate(alphanumeric_filename)
        return result


if __name__ == '__main__':
        app.run(host='0.0.0.0', port=80)
