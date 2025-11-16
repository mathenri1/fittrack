from flask import Blueprint, request, jsonify
from models import db, Treino

treino_bp = Blueprint("treino_bp", __name__)

@treino_bp.get("/")
def listar():
    treinos = Treino.query.order_by(Treino.data_hora.desc()).all()
    return jsonify([
        {
            "id": t.id,
            "usuario_id": t.usuario_id,
            "data_hora": t.data_hora.isoformat(),
            "observacoes": t.observacoes,
            "percepcao_esforco": t.percepcao_esforco,
        }
        for t in treinos
    ])

@treino_bp.post("/")
def criar():
    body = request.json or {}
    t = Treino(
        usuario_id=body.get("usuario_id", 1),
        observacoes=body.get("observacoes"),
        percepcao_esforco=body.get("percepcao_esforco"),
    )
    db.session.add(t)
    db.session.commit()
    return jsonify(id=t.id), 201

@treino_bp.delete("/<int:treino_id>")
def deletar(treino_id):
    t = Treino.query.get_or_404(treino_id)
    db.session.delete(t)
    db.session.commit()
    return jsonify(ok=True)

@treino_bp.put("/<int:treino_id>")
def atualizar(treino_id):
    t = Treino.query.get_or_404(treino_id)
    body = request.json or {}
    t.observacoes = body.get("observacoes", t.observacoes)
    t.percepcao_esforco = body.get("percepcao_esforco", t.percepcao_esforco)
    db.session.commit()
    return jsonify(ok=True)
