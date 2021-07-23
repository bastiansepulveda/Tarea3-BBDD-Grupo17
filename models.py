from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from pytz import timezone

db = SQLAlchemy()

#### Se crea la entidad Pais ####

class Pais(db.Model):
	cod_pais = db.Column(db.Integer, primary_key=True)
	nombre_pais = db.Column(db.String(45), nullable=False)
	#Añadimos la relación
	ciudadanos = db.relationship('Usuario', cascade="all,delete", backref="parent", lazy='dynamic')

	@classmethod
	def create(cls, new_pais):
		#Buscamos la última ID desde la función Last_id
		last_id = Pais.Last_id().fetchall()[0][0]
		# Instanciamos un nuevo usuario y lo guardamos en la bd
		pais = Pais(cod_pais = last_id +1, nombre_pais=new_pais)
		return pais.save()

	def save(self):
		try:
			db.session.add(self)
			db.session.commit()
			return self
		except:
			return False
	def json(self):
		return {
			'cod_pais': self.cod_pais,
			'nombre_pais': self.nombre_pais
		}
	def update(self):
		self.save()
	def delete(self):
		try:
			db.session.delete(self)
			db.session.commit()

			return True
		except:
			return False

	#Buscamos la última id
	def Last_id():
		try:
			result = db.session.execute('SELECT cod_pais FROM Pais ORDER BY cod_pais DESC LIMIT 1')
			return result
		except:
			return False


#### Se crea la entidad Usuario ###

class Usuario(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String(50), nullable=False)
	apellido = db.Column(db.String(50), nullable=True)
	correo = db.Column(db.String(50), nullable=False)
	contraseña = db.Column(db.String(50), nullable=False)
	pais = db.Column(db.Integer, db.ForeignKey('pais.cod_pais'))
	fecha_registro = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone('America/Santiago')))
	#Agregamos el atributo admin, creado para la tarea 2.
	admin = db.Column(db.Boolean, nullable = False)
	#Añadimos la relación
	utm = db.relationship('UsuarioTieneMoneda', cascade="all,delete", backref="utm_parent", lazy='dynamic')
	banco = db.relationship('CuentaBancaria', cascade="all,delete", backref="banco_parent", lazy='dynamic')


	@classmethod
	def create(cls, name, lastname, email, password, id_country, adm):
		last_id = Usuario.Last_id().fetchall()[0][0]
		# Instanciamos un nuevo usuario y lo guardamos en la bd
		usuario = Usuario(id=last_id +1,nombre=name, apellido=lastname, correo=email, contraseña=password, pais=id_country, admin=adm)
		return usuario.save()

	def save(self):
		try:
			db.session.add(self)
			db.session.commit()

			return self
		except:
			return False
	def json(self):
		return {
			'id': self.id,
			'nombre': self.nombre,
			'apellido': self.apellido,
			'correo': self.correo,
			'contraseña': self.contraseña,
			'pais': self.pais,
			'fecha_registro': self.fecha_registro,
			'admin': self.admin,
		}
	def update(self):
		self.save()
	def delete(self):
		try:
			db.session.delete(self)
			db.session.commit()

			return True
		except:
			return False

	#Consulta 1
	def consulta1(year_registration):
		try:
			result = db.session.execute('SELECT nombre AS "Nombre", apellido AS "Apellido", fecha_registro AS "Fecha Registro" FROM usuario WHERE EXTRACT(YEAR FROM usuario.fecha_registro)=:año ORDER BY fecha_registro', {'año': year_registration})
			return result
		except:
			return False
	#Buscamos la última id
	def Last_id():
		try:
			result = db.session.execute('SELECT id FROM Usuario ORDER BY id DESC LIMIT 1')
			return result
		except:
			return False


###  Se crea la entidad Cuenta Bancaria  ###
			
class CuentaBancaria(db.Model):
	numero_cuenta = db.Column(db.Integer, primary_key=True)
	id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
	balance = db.Column(db.Float)

	@classmethod
	def create(cls, id_usuario, balance):
		#Buscamos la última ID desde la función Last_id
		last_id = CuentaBancaria.Last_id().fetchall()[0][0]
		# Instanciamos un nuevo usuario y lo guardamos en la bd
		cuenta = CuentaBancaria(numero_cuenta = last_id+1, id_usuario=id_usuario, balance=balance)
		return cuenta.save()

	def save(self):
		try:
			db.session.add(self)
			db.session.commit()

			return self
		except:
			return False
	def json(self):
		return {
			'numero_cuenta': self.numero_cuenta,
			'id_usuario': self.id_usuario,
			'balance': self.balance
		}
	def update(self):
		self.save()
	def delete(self):
		try:
			db.session.delete(self)
			db.session.commit()

			return True
		except:
			return False
	
	def Last_id():
		try:
			result = db.session.execute('SELECT numero_cuenta FROM cuenta_bancaria ORDER BY numero_cuenta DESC LIMIT 1')
			return result
		except:
			return False
	
	#Consulta 2
	def consulta2(max_balance):
		try:
			result = db.session.execute('SELECT numero_cuenta AS "Id Cuenta", balance AS "Balance" FROM cuenta_bancaria WHERE balance>:max_balance', {'max_balance': max_balance})
			return result
		except:
			return False

### Se crea la entidad Moneda ####

class Moneda(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	sigla = db.Column(db.String(10), nullable=False)
	nombre = db.Column(db.String(80), nullable=False)
	#Añadimos la relación
	utm = db.relationship('UsuarioTieneMoneda', cascade="all,delete", backref="mon_utm_parent", lazy='dynamic')
	precio = db.relationship('PrecioMoneda', cascade="all,delete", backref="precio_parent", lazy='dynamic')


	@classmethod
	def create(cls, sigla, nombre):
		#Buscamos la última ID desde la función Last_id
		last_id = Moneda.Last_id().fetchall()[0][0]
		# Instanciamos un nuevo usuario y lo guardamos en la bd
		moneda = Moneda(id=last_id+1, sigla=sigla, nombre=nombre)
		return moneda.save()

	def save(self):
		try:
			db.session.add(self)
			db.session.commit()

			return self
		except:
			return False
	def json(self):
		return {
			'id': self.id,
			'sigla': self.sigla,
			'nombre': self.nombre
		}
	def update(self):
		self.save()
	def delete(self):
		try:
			db.session.delete(self)
			db.session.commit()

			return True
		except:
			return False

	def Last_id():
		try:
			result = db.session.execute('SELECT id FROM moneda ORDER BY id DESC LIMIT 1')
			return result
		except:
			return False

	#Consulta 5.1
	def consulta5(id):
		try:
			result = db.session.execute('SELECT nombre AS "Nombre" FROM moneda WHERE moneda.id=:id' , {'id': id})
			return result
		except:
			return False
	

#### Se crea la entidad Usuario Tiene Moneda  ###

class UsuarioTieneMoneda(db.Model):
	id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)
	id_moneda = db.Column(db.Integer, db.ForeignKey('moneda.id'), primary_key=True)
	balance = db.Column(db.Float, nullable=False)

	@classmethod
	def create(cls, id_usuario, id_moneda, balance):
		# Instanciamos un nuevo usuario y lo guardamos en la bd
		utm = UsuarioTieneMoneda(id_usuario=id_usuario, id_moneda=id_moneda, balance=balance)
		return utm.save()

	def save(self):
		try:
			db.session.add(self)
			db.session.commit()

			return self
		except:
			return False
	def json(self):
		return {
			'id_usuario': self.id_usuario,
			'id_moneda': self.id_moneda,
			'balance': self.balance
		}
	def update(self):
		self.save()
	def delete(self):
		try:
			db.session.delete(self)
			db.session.commit()

			return True
		except:
			return False
	#Consulta 5.2
	def consulta6(id):
		try:
			result = db.session.execute('SELECT SUM(balance) AS "Balance" FROM usuario_tiene_moneda WHERE usuario_tiene_moneda.id_moneda=:id' , {'id': id})
			return result
		except:
			return False

####  Se crea la entidad Precio Moneda ####

class PrecioMoneda(db.Model):
	fecha = db.Column(db.DateTime, default=db.func.current_timestamp(), primary_key=True)
	id_moneda = db.Column(db.Integer, db.ForeignKey('moneda.id'), nullable=False)
	valor = db.Column(db.Float, nullable=False)

	@classmethod
	def create(cls, id_moneda, valor):
		# Instanciamos un nuevo usuario y lo guardamos en la bd
		precio = PrecioMoneda(fecha=db.func.current_timestamp(), id_moneda=id_moneda, valor=valor)
		return precio.save()

	def save(self):
		try:
			db.session.add(self)
			db.session.commit()

			return self
		except:
			return False
	def json(self):
		return {
			'fecha': self.fecha.strftime('%Y-%m-%d %H:%M:%S.%f'),
			'id_moneda': self.id_moneda,
			'valor': self.valor
		}
	def update(self):
		self.save()
	def delete(self):
		try:
			db.session.delete(self)
			db.session.commit()

			return True
		except:
			return False
