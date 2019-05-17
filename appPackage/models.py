from appPackage import db


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)


	def __str__(self):
		return self.username


class Data(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	temperature = db.Column(db.Float, index=True)
	moisture = db.Column(db.Float, index=True)
	humidity = db.Column(db.Float, index=True)
	status = db.Column(db.Boolean, index=True)


