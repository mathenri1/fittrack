from flask import Blueprint, request, jsonify
from models import db, Refeicao

refeicao_bp = Blueprint("refeicao_bp", __name__)

@refeicao_bp.get("/")
def listar():
    items = Refeicao.query.order_by(Refeicao.data_hora.desc()).all()
    return jsonify([
        {
            "id": r.id,
            "usuario_id": r.usuario_id,
            "data_hora": r.data_hora.isoformat(),
            "descricao": r.descricao,
            "proteina_g": r.proteina_g,
            "carbo_g": r.carbo_g,
            "gordura_g": r.gordura_g,
        }
        for r in items
    ])

@refeicao_bp.post("/")
def criar():
    body = request.json or {}
    r = Refeicao(
        usuario_id=body.get("usuario_id", 1),
        descricao=body.get("descricao"),
        proteina_g=body.get("proteina_g", 0),
        carbo_g=body.get("carbo_g", 0),
        gordura_g=body.get("gordura_g", 0),
    )
    db.session.add(r)
    db.session.commit()
    return jsonify(id=r.id), 201

@refeicao_bp.put("/<int:refeicao_id>")
def atualizar(refeicao_id):
    r = Refeicao.query.get_or_404(refeicao_id)
    body = request.json or {}
    r.descricao = body.get("descricao", r.descricao)
    r.proteina_g = body.get("proteina_g", r.proteina_g)
    r.carbo_g = body.get("carbo_g", r.carbo_g)
    r.gordura_g = body.get("gordura_g", r.gordura_g)
    db.session.commit()
    return jsonify(ok=True)

@refeicao_bp.delete("/<int:refeicao_id>")
def deletar(refeicao_id):
    r = Refeicao.query.get_or_404(refeicao_id)
    db.session.delete(r)
    db.session.commit()
    return jsonify(ok=True)
