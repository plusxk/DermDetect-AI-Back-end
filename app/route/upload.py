import os
from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename

bp = Blueprint("upload", __name__, url_prefix="/upload")

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in current_app.config["ALLOWED_EXTENSIONS"]

@bp.route("/", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)
        return jsonify({"message": "File uploaded", "filepath": filepath}), 200
    return jsonify({"error": "File type not allowed"}), 400
