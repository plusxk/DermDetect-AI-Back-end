from flask import Blueprint, request, jsonify
from app.models.inference import predict_disease

bp = Blueprint("predict", __name__, url_prefix="/predict")

@bp.route("/", methods=["POST"])
def predict():
    data = request.json
    if "image_path" not in data:
        return jsonify({"error": "Missing image_path in request"}), 400
    
    image_path = data["image_path"]
    try:
        result = predict_disease(image_path)
        return jsonify({"prediction": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500