from flask import Flask, jsonify
from flask_cors import CORS
from models import db, init_db
from routes.treino_routes import treino_bp
from routes.refeicao_routes import refeicao_bp

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///fittrack.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
CORS(app)

with app.app_context():
    init_db()

app.register_blueprint(treino_bp, url_prefix="/api/treinos")
app.register_blueprint(refeicao_bp, url_prefix="/api/refeicoes")

@app.route("/api/health")
def health():
    return jsonify(status="ok")

if __name__ == "__main__":
    app.run(debug=True)
