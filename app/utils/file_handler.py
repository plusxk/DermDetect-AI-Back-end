import os
from flask import current_app
def allowed_file(filename):
    """檢查文件是否為允許的類型"""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in current_app.config["ALLOWED_EXTENSIONS"]

def save_file(file, filename, upload_folder):
    """儲存文件到指定目錄"""
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)  # 如果目錄不存在，則創建
    filepath = os.path.join(upload_folder, filename)
    file.save(filepath)
    return filepath
