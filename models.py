from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	firstname = db.Column(db.String(100))
	lastname = db.Column(db.String(100))
	email = db.Column('email', db.String(120), unique=True, index=True, nullable=False)
	pwdhash = db.Column('pwdhash',db.String)
	authenticated = db.Column(db.Boolean, default=False)

	def __init__(self, firstname, lastname, email, password):
		self.firstname = firstname.title()
		self.lastname = lastname.title()
		self.email = email.lower()
		self.set_password(password)
		self.authenticated = False

	def set_password(self, password):
		self.pwdhash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.pwdhash, password)

	@property	
	def is_active(self):
		return True

	@property
	def is_anonymous(self):
		return False

	@property
	def is_authenticated(self):
		return self.authenticated

	def get_id(self):
		return str(self.id)

	def __repr__(self):
		return 'User {0}'.format(self.firstname)