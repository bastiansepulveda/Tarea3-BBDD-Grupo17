from flask import Flask
from flask import jsonify
from config import config
from models import db
from models import Pais, Usuario, CuentaBancaria, Moneda, UsuarioTieneMoneda, PrecioMoneda
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
	paises = [nombre.json() for nombre in Pais.query.all() ] 
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

	#Se deja la posibilidad de actualizar uno o mas tributos del usuario
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

	#Se deja la posibilidad de actualizar uno o más tributos de la cuenta bancaria
	if json.get('id_usuario') is not None:
		cuenta.id_usuario = json['id_usuario']
	if json.get('nombre') is not None:
		cuenta.balance = json['nombre']

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

	#Se deja la posibilidad de actualizar uno o mas tributos de la moneda
	if json.get('sigla') is not None:
		moneda.sigla = json['sigla']
	if json.get('nombre') is not None:
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

###### USUARIO TIENE MONEDA ######

# Endpoint para obtener todas las monedas que posee cada usuario
@app.route('/api/v1/utm', methods=['GET'])
def get_utms():
	utms = [ utm.json() for utm in UsuarioTieneMoneda.query.all() ] 
	return jsonify({'usuarios tienen moneda': utms })

# Endpoint para obtener al usuario y a la moneda con id_usuario & id_moneda igual a <id_usuario>&<id_moneda>
@app.route('/api/v1/utm/<id_usuario>&<id_moneda>', methods=['GET'])
def get_utm(id_usuario, id_moneda):
	utm = UsuarioTieneMoneda.query.filter_by(id_usuario=id_usuario, id_moneda=id_moneda).first()
	if utm is None:
		return jsonify({'message': 'Utm does not exists'}), 404

	return jsonify({'utm': utm.json() })

# Endpoint para insertar un usario y la moneda correspondiente en la bd
@app.route('/api/v1/utm', methods=['POST'])
def create_utm():
	json = request.get_json(force=True)

	if (json.get('id_usuario') or json.get('id_moneda') or json.get('balance')) is None:
		return jsonify({'message': 'El formato está mal'}), 400

	utm = UsuarioTieneMoneda.create(json['id_usuario'], json['id_moneda'], json['balance'])

	return jsonify({'usuario tiene moneda': utm.json() })

# Endpoint para actualizar los datos de un usuario y su moneda asociada en la bd
@app.route('/api/v1/utm/<id_usuario>&<id_moneda>', methods=['PUT'])
def update_utm(id_usuario, id_moneda):
	utm = UsuarioTieneMoneda.query.filter_by(id_usuario=id_usuario, id_moneda=id_moneda).first()
	if utm is None:
		return jsonify({'message': 'Utm does not exists'}), 404

	json = request.get_json(force=True)
	if (json.get('id_usuario') or json.get('id_moneda') or json.get('balance')) is None:
		return jsonify({'message': 'Bad request'}), 400

	#Se deja la posibilidad de actualizar uno o mas tributos
	if json.get('id_usuario') is not None:
		utm.id_usuario= json['id_usuario']
	if json.get('id_moneda') is not None:
		utm.id_moneda = json['id_moneda']
	if json.get('balance') is not None:
		utm.balance = json['balance']

	utm.update()

	return jsonify({'utm': utm.json() })

# Endpoint para eliminar al usuario y su moneda con id_usuario & id_moneda igual a <id_usuario>&<id_moneda>
@app.route('/api/v1/utm/<id_usuario>&<id_moneda>', methods=['DELETE'])
def delete_utm(id_usuario, id_moneda):
	utm = UsuarioTieneMoneda.query.filter_by(id_usuario=id_usuario, id_moneda=id_moneda).first()
	if utm is None:
		return jsonify({'message': 'La moneda no existe'}), 404

	utm.delete()

	return jsonify({'utm': utm.json() })


###### PRECIO MONEDA ######

# Endpoint para obtener el historial de todos los valores de todas las monedas
@app.route('/api/v1/precio', methods=['GET'])
def get_precios():
	precios = [ precio.json() for precio in PrecioMoneda.query.all() ] 
	return jsonify({'precios monedas': precios })

# Endpoint para obtener a la moneda (con cierto valor) en la  fecha igual <fecha>
@app.route('/api/v1/precio/<fecha>', methods=['GET'])
def get_precio(fecha):
	precio = PrecioMoneda.query.filter_by(fecha=fecha).first()
	if precio is None:
		return jsonify({'message': 'Precio does not exists'}), 404

	return jsonify({'precio': precio.json() })

# Endpoint para insertar el valor actual de la moneda (cualquiera) en la bd
@app.route('/api/v1/precio', methods=['POST'])
def create_precio():
	json = request.get_json(force=True)

	if (json.get('id_moneda') or json.get('valor')) is None:
		return jsonify({'message': 'El formato está mal'}), 400

	precio = PrecioMoneda.create(json['id_moneda'], json['valor'])

	return jsonify({'precio': precio.json() })

# Endpoint para actualizar los valores de una moneda en la bd
@app.route('/api/v1/precio/<fecha>', methods=['PUT'])
def update_precio(fecha):
	precio = PrecioMoneda.query.filter_by(fecha=fecha).first()
	if precio is None:
		return jsonify({'message': 'Precio does not exists'}), 404

	json = request.get_json(force=True)
	if (json.get('id_moneda') or json.get('valor')) is None:
		return jsonify({'message': 'Bad request'}), 400

	#Se deja la posibilidad de actualizar uno o mas atributos del precio moneda
	if json.get('id_moneda') is not None:
		precio.id_moneda= json['id_moneda']
	if json.get('valor') is not None:
		precio.valor = json['valor']

	precio.update()

	return jsonify({'precio': precio.json() })

# Endpoint para eliminar la caracteristica de la moneda en la fecha igual a  <fecha>
@app.route('/api/v1/precio/<fecha>', methods=['DELETE'])
def delete_precio(fecha):
	precio = PrecioMoneda.query.filter_by(fecha=fecha).first()
	if precio is None:
		return jsonify({'message': 'La moneda no existe'}), 404

	precio.delete()

	return jsonify({'precio': precio.json() })

if __name__ == '__main__':
	app.run(debug=True)