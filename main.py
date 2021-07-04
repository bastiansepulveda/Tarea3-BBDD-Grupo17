from flask import Flask
from flask import jsonify
from config import config
from models import db
from models import Pais, Usuario, CuentaBancaria, Moneda
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

###### PAIS ######

# Endpoint para obtener todos los países
@app.route('/api/v1/pais', methods=['GET'])
def get_paises():
	paises = [ nombre.json() for nombre in Pais.query.all() ] 
	return jsonify({'paises': paises })

# Endpoint para obtener al país con cod_pais igual a <cod_pais>
@app.route('/api/v1/pais/<cod_pais>', methods=['GET'])
def get_pais(cod_pais):
	pais = Pais.query.filter_by(cod_pais=cod_pais).first()
	if pais is None:
		return jsonify({'message': 'Pais does not exists'}), 404

	return jsonify({'pais': pais.json() })

# Endpoint para insertar un país en la bd
@app.route('/api/v1/pais', methods=['POST'])
def create_pais():
	json = request.get_json(force=True)

	if json.get('nombre') is None:
		return jsonify({'message': 'El formato está mal'}), 400

	pais = Pais.create(json['nombre'])

	return jsonify({'pais': pais.json() })

# Endpoint para actualizar los datos de un país en la bd
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

# Endpoint para eliminar al país con cod_pais igual a <cod_pais>
@app.route('/api/v1/pais/<cod_pais>', methods=['DELETE'])
def delete_pais(cod_pais):
	pais = Pais.query.filter_by(cod_pais=cod_pais).first()
	if pais is None:
		return jsonify({'message': 'El pais no existe'}), 404

	pais.delete()

	return jsonify({'pais': pais.json() })


###### USUARIO ######

# Endpoint para obtener todos los usuarios
@app.route('/api/v1/usuario', methods=['GET'])
def get_usuarios():
	usuarios = [ nombre.json() for nombre in Usuario.query.all() ] 
	return jsonify({'usuarios': usuarios })

# Endpoint para obtener el usuario con id igual a <id>
@app.route('/api/v1/usuario/<id>', methods=['GET'])
def get_usuario(id):
	usuario = Usuario.query.filter_by(id=id).first()
	if usuario is None:
		return jsonify({'message': 'Usuario does not exists'}), 404

	return jsonify({'usuario': usuario.json() })

# Endpoint para insertar un usuario en la bd
@app.route('/api/v1/usuario', methods=['POST'])
def create_usuario():
	json = request.get_json(force=True)

	if (json.get('nombre') or json.get('apellido') or json.get('correo') or json.get('contraseña') or json.get('pais')) is None:
		return jsonify({'message': 'El formato está mal'}), 400

	usuario = Usuario.create(json['nombre'], json['apellido'], json['correo'], json['contraseña'], json['pais'])

	return jsonify({'usuario': usuario.json() })

# Endpoint para actualizar los datos de un usuario en la bd
@app.route('/api/v1/usuario/<id>', methods=['PUT'])
def update_usuario(id):
	usuario = Usuario.query.filter_by(id=id).first()
	if usuario is None:
		return jsonify({'message': 'Usuario does not exists'}), 404

	json = request.get_json(force=True)
	if (json.get('nombre') or json.get('apellido') or json.get('correo') or json.get('contraseña') or json.get('pais')) is None:
		return jsonify({'message': 'Bad request'}), 400

	if json.get('nombre') is not None:
		usuario.nombre = json['nombre']
	if json.get('apellido') is not None:
		usuario.apellido = json['apellido']
	if json.get('correo') is not None:
		usuario.correo = json['correo']
	if json.get('contraseña') is not None:
		usuario.contraseña = json['contraseña']
	if json.get('pais') is not None:
		usuario.pais = json['pais']

	usuario.update()

	return jsonify({'usuario': usuario.json() })

# Endpoint para eliminar el usuario con id igual a <id>
@app.route('/api/v1/usuario/<id>', methods=['DELETE'])
def delete_usuario(id):
	usuario = Usuario.query.filter_by(id=id).first()
	if usuario is None:
		return jsonify({'message': 'El usuario no existe'}), 404

	usuario.delete()

	return jsonify({'usuario': usuario.json() })


###### CUENTA BANCARIA ######

# Endpoint para obtener todas las cuentas bancarias
@app.route('/api/v1/cuenta_bancaria', methods=['GET'])
def get_cuentas():
	cuentas = [ cuenta.json() for cuenta in CuentaBancaria.query.all() ] 
	return jsonify({'cuentas': cuentas })

# Endpoint para obtener la cuenta bancaria con numero_cuenta igual a  <numero_cuenta>
@app.route('/api/v1/cuenta_bancaria/<numero_cuenta>', methods=['GET'])
def get_cuenta(numero_cuenta):
	cuenta = CuentaBancaria.query.filter_by(numero_cuenta=numero_cuenta).first()
	if cuenta is None:
		return jsonify({'message': 'Cuenta does not exists'}), 404

	return jsonify({'cuenta': cuenta.json() })

# Endpoint para insertar una cuenta bancaria en la bd
@app.route('/api/v1/cuenta_bancaria', methods=['POST'])
def create_cuenta():
	json = request.get_json(force=True)

	if (json.get('id_usuario') or json.get('balance')) is None:
		return jsonify({'message': 'El formato está mal'}), 400

	cuenta = CuentaBancaria.create(json['id_usuario'], json['balance'])

	return jsonify({'cuenta': cuenta.json() })

# Endpoint para actualizar los datos de una cuenta bancaria en la bd
@app.route('/api/v1/cuenta_bancaria/<numero_cuenta>', methods=['PUT'])
def update_cuenta(numero_cuenta):
	cuenta = CuentaBancaria.query.filter_by(numero_cuenta=numero_cuenta).first()
	if cuenta is None:
		return jsonify({'message': 'Cuenta does not exists'}), 404

	json = request.get_json(force=True)
	if (json.get('id_usuario') or json.get('balance')) is None:
		return jsonify({'message': 'Bad request'}), 400

	if json.get('id_usuario') is not None:
		cuenta.id_usuario = json['id_usuario']
	if json.get('balance') is not None:
		cuenta.balance = json['balance']

	cuenta.update()

	return jsonify({'cuenta': cuenta.json() })

# Endpoint para eliminar la cuenta bancaria con numero_cuenta igual a <numero_cuenta>
@app.route('/api/v1/cuenta_bancaria/<numero_cuenta>', methods=['DELETE'])
def delete_cuenta(numero_cuenta):
	cuenta = CuentaBancaria.query.filter_by(numero_cuenta=numero_cuenta).first()
	if cuenta is None:
		return jsonify({'message': 'La cuenta no existe'}), 404

	cuenta.delete()

	return jsonify({'cuenta': cuenta.json() })


###### MONEDA ######

# Endpoint para obtener todas las monedas
@app.route('/api/v1/moneda', methods=['GET'])
def get_monedas():
	monedas = [ moneda.json() for moneda in Moneda.query.all() ] 
	return jsonify({'monedas': monedas })

# Endpoint para obtener la moenda con id  igual a <id>
@app.route('/api/v1/moneda/<id>', methods=['GET'])
def get_moneda(id):
	moneda = Moneda.query.filter_by(id=id).first()
	if moneda is None:
		return jsonify({'message': 'Moneda does not exists'}), 404

	return jsonify({'cuenta': moneda.json() })

# Endpoint para insertar una moneda en la bd
@app.route('/api/v1/moneda', methods=['POST'])
def create_moneda():
	json = request.get_json(force=True)

	if (json.get('sigla') or json.get('nombre')) is None:
		return jsonify({'message': 'El formato está mal'}), 400

	moneda = Moneda.create(json['sigla'], json['nombre'])

	return jsonify({'moneda': moneda.json() })

# Endpoint para actualizar los datos de una moneda en la bd
@app.route('/api/v1/moneda/<id>', methods=['PUT'])
def update_moneda(id):
	moneda = Moneda.query.filter_by(id=id).first()
	if moneda is None:
		return jsonify({'message': 'Moneda does not exists'}), 404

	json = request.get_json(force=True)
	if (json.get('sigla') or json.get('nombre')) is None:
		return jsonify({'message': 'Bad request'}), 400

	if json.get('sigla'):
		moneda.sigla = json['sigla']
	if json.get('nombre'):
		moneda.nombre = json['nombre']

	moneda.update()

	return jsonify({'moneda': moneda.json() })

# Endpoint para eliminar la moneda con id igual a <id>
@app.route('/api/v1/moneda/<id>', methods=['DELETE'])
def delete_moneda(id):
	moneda = Moneda.query.filter_by(id=id).first()
	if moneda is None:
		return jsonify({'message': 'La moneda no existe'}), 404

	moneda.delete()

	return jsonify({'moneda': moneda.json() })


if __name__ == '__main__':
	app.run(debug=True)