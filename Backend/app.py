# backend/app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import regula_falsi_modificada

app = Flask(__name__)
CORS(app)

@app.route("/api/regula", methods=["POST"])
def calcula_raiz():
    """
    Espera JSON { N: float, error: float }
    Responde { raiz: float|null, tabla: [...] }
    """
    data = request.get_json() or {}
    try:
        N = float(data.get("N", 0))
        error = float(data.get("error", 1e-6))
    except (ValueError, TypeError):
        return jsonify({"error": "Parámetros inválidos"}), 400

    a, b = 0.0, max(1.0, N)
    raiz, tabla = regula_falsi_modificada(N, a, b, error)
    return jsonify({"raiz": raiz, "tabla": tabla})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
