from database import db

class Cliente(db.Model):
    __tablename__ = 'clientes'
    id_clientes = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(50))
   
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    
    def __repr__(self):
        return f"<Cliente {self.nome}>"
    

class Feedbacks(db.Model):
    __tablename__ = 'feedbacks'
    id_feedbacks = db.Column(db.Integer, primary_key = True)
    comentario = db.Column(db.String(100))
    data = db.Column(db.Date)
    id_clientes = db.Column(db.Integer, db.ForeignKey('clientes.id_clientes'))

    cliente = db.relationship('Cliente', foreign_keys=id_clientes)

    def __init__(self, comentario, data, id_feedbacks):
        self.comentario = comentario
        self.data = data
        self.id_feedbacks = id_feedbacks
    
    def __repr__(self):
        return f"<Feedbacks: {self.comentario} - {self.data} - {self.id_feedbacks}> "