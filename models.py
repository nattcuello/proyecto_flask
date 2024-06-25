from app import db

class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50),nullable=False)

    def __str__(self):
        return self.nombre