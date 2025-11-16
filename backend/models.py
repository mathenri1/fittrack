from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = "usuario"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha_hash = db.Column(db.String(255), nullable=False)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

    treinos = db.relationship("Treino", backref="usuario", lazy=True)
    refeicoes = db.relationship("Refeicao", backref="usuario", lazy=True)

class Treino(db.Model):
    __tablename__ = "treino"
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=False)
    data_hora = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    observacoes = db.Column(db.String(255))
    percepcao_esforco = db.Column(db.Integer)
    itens = db.relationship("TreinoExercicio", backref="treino", lazy=True)

class Exercicio(db.Model):
    __tablename__ = "exercicio"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    grupo_muscular = db.Column(db.String(40))
    itens = db.relationship("TreinoExercicio", backref="exercicio", lazy=True)

class TreinoExercicio(db.Model):
    __tablename__ = "treino_exercicio"
    id = db.Column(db.Integer, primary_key=True)
    treino_id = db.Column(db.Integer, db.ForeignKey("treino.id"), nullable=False)
    exercicio_id = db.Column(db.Integer, db.ForeignKey("exercicio.id"), nullable=False)
    series = db.relationship("Serie", backref="treino_exercicio", lazy=True)

class Serie(db.Model):
    __tablename__ = "serie"
    id = db.Column(db.Integer, primary_key=True)
    treino_exercicio_id = db.Column(db.Integer, db.ForeignKey("treino_exercicio.id"), nullable=False)
    repeticoes = db.Column(db.Integer, nullable=False)
    carga = db.Column(db.Float)
    duracao_seg = db.Column(db.Integer)

class Refeicao(db.Model):
    __tablename__ = "refeicao"
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=False)
    data_hora = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    descricao = db.Column(db.String(255))
    proteina_g = db.Column(db.Float, default=0)
    carbo_g = db.Column(db.Float, default=0)
    gordura_g = db.Column(db.Float, default=0)

def init_db():
    db.create_all()
    # sementes simples de exercícios (ajuda a testar)
    if Exercicio.query.count() == 0:
        db.session.add_all([
            Exercicio(nome="Supino Reto", grupo_muscular="Peito"),
            Exercicio(nome="Agachamento Livre", grupo_muscular="Pernas"),
            Exercicio(nome="Remada Curvada", grupo_muscular="Costas"),
        ])
        db.session.commit()
