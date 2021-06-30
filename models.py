from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Creamos la entidad User
class Pais(db.Model):
	__tablename__ = 'pais'
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
			'nombre': self.nombre,
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
