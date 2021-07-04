from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#### Se crea la entidad Pais ####

class Pais(db.Model):
	cod_pais = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String(45), nullable=False)
	
	@classmethod
	def create(cls, new_pais):
		# Instanciamos un nuevo usuario y lo guardamos en la bd
		pais = Pais(nombre=new_pais)
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


#### Se crea la entidad Usuario ###

class Usuario(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String(50), nullable=False)
	apellido = db.Column(db.String(50), nullable=True)
	correo = db.Column(db.String(50), nullable=False)
	contraseña = db.Column(db.String(50), nullable=False)
	pais = db.Column(db.Integer, db.ForeignKey('pais.cod_pais'))
	fecha_registro = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

	@classmethod
	def create(cls, name, lastname, email, password, id_country):
		# Instanciamos un nuevo usuario y lo guardamos en la bd
		usuario = Usuario(nombre=name, apellido=lastname, correo=email, contraseña=password, pais=id_country)
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

###  Se crea la entidad Cuenta Bancaria  ###
			
class CuentaBancaria(db.Model):
	numero_cuenta = db.Column(db.Integer, primary_key=True)
	id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
	balance = db.Column(db.Float, nullable=False)

	@classmethod
	def create(cls, id_usuario, balance):
		# Instanciamos un nuevo usuario y lo guardamos en la bd
		cuenta = CuentaBancaria(id_usuario=id_usuario, balance=balance)
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


### Se crea la entidad Moneda ####

class Moneda(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	sigla = db.Column(db.String(10), nullable=False)
	nombre = db.Column(db.String(80), nullable=False)

	@classmethod
	def create(cls, sigla, nombre):
		# Instanciamos un nuevo usuario y lo guardamos en la bd
		#print(Moneda.custom().fetchall()[0][0])
		moneda = Moneda(sigla=sigla, nombre=nombre)
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