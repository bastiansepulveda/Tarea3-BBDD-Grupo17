from flask import Flask
from flask import jsonify
from config import config
from models import db
from models import Pais
from flask import request

def create_app(enviroment):
	app = Flask(__name__)
	app.config.from_object(enviroment)
	with app.app_context():
		db.init_app(app)
		db.create_all()
	return app

# Accedemos a la clase config del archivo config.py
enviroment = config['development']
app = create_app(enviroment)

# Endpoint para obtener todos los usuarios
@app.route('/api/v1/pais', methods=['GET'])
def get_paises():
	paises = [ nombre.json() for nombre in Pais.query.all() ] 
	return jsonify({'paises': paises })

# Endpoint para obtener el usuario con id <id>
@app.route('/api/v1/users/<cod_pais>', methods=['GET'])
def get_pais(cod_pais):
	pais = Pais.query.filter_by(cod_pais=cod_pais).first()
	if pais is None:
		return jsonify({'message': 'Pais does not exists'}), 404

	return jsonify({'pais': pais.json() })

# Endpoint para insertar un usuario en la bd
@app.route('/api/v1/pais/', methods=['POST'])
def create_pais():
	json = request.get_json(force=True)

	if json.get('nombre') is None:
		return jsonify({'message': 'El formato está mal'}), 400

	pais = Pais.create(json['nombre'])

	return jsonify({'pais': pais.json() })

# Endpoint para actualizar los datos de un usuario en la bd
@app.route('/api/v1/pais/<cod_pais>', methods=['PUT'])
def update_pais(cod_pais):
	pais = Pais.query.filter_by(cod_pais=cod_pais).first()
	if pais is None:
		return jsonify({'message': 'Pais does not exists'}), 404

	json = request.get_json(force=True)
	if json.get('nombre') is None:
		return jsonify({'message': 'Bad request'}), 400

	pais.nombre = json['nombre']

	pais.update()

	return jsonify({'pais': pais.json() })

# Endpoint para eliminar el usuario con id igual a <id>
@app.route('/api/v1/pais/<cod_pais>', methods=['DELETE'])
def delete_pais(cod_pais):
	pais = Pais.query.filter_by(cod_pais=cod_pais).first()
	if pais is None:
		return jsonify({'message': 'El pais no existe'}), 404

	pais.delete()

	return jsonify({'pais': pais.json() })

if __name__ == '__main__':
	app.run(debug=True)
