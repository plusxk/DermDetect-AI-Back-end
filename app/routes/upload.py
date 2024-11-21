import os
from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
from app.utils.file_handler import allowed_file, save_file
from app.utils.image_analyzer import analyze_image
bp = Blueprint("upload", __name__, url_prefix="/upload")

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in current_app.config["ALLOWED_EXTENSIONS"]

@bp.route("/", methods=["POST"])
def upload_and_process_image():
    if "image" not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    image = request.files["image"]
    if image.filename == "":
        return jsonify({"error": "No selected file"}), 400
    
    if image and allowed_file(image.filename):
        # 使用 secure_filename 確保文件名安全
        filename = secure_filename(image.filename)
        filepath = save_file(image, filename, current_app.config["UPLOAD_FOLDER"])
        
        # 分析圖片並返回結果
        result_text = analyze_image(filepath)
        return jsonify({"message": "Success", "result": result_text}), 200
    
    return jsonify({"error": "File type not allowed"}), 400