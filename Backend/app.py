# backend/app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import regula_falsi_modificada

app = Flask(__name__)
CORS(app)

@app.route("/api/regula", methods=["POST"])
def calcula_raiz():
    """
    Espera JSON { N: float, exp: int }
    Responde { raiz: float|null, tabla: [...] } o {"error": "..."} en caso de fallo.
    """
    data = request.get_json() or {}
    # 1. Leer parámetros
    try:
        N   = float(data.get("N", 0))
        exp = int(data.get("exp", 6))
    except (ValueError, TypeError):
        return jsonify({"error": "Parámetros inválidos"}), 400

    # 2. Definir intervalo inicial [a, b]
    a, b = 0.0, max(1.0, N)

    # 3. Ejecutar Regula Falsi con exponente de tolerancia
    resultado = regula_falsi_modificada(N, a, b, exp)
    if resultado is None:
        return jsonify({"error": "Intervalo [a,b] inválido"}), 400

    raiz, tabla = resultado

    # 4. Devolver JSON con resultado
    return jsonify({"raiz": raiz, "tabla": tabla})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
