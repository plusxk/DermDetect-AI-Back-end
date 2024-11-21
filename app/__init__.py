from flask import Flask
from app.routes import upload
from flask_cors import CORS
def create_app():
    app = Flask(__name__)
    CORS(app)
    # 加載配置
    app.config.from_object("app.config.Config")
    
    # 註冊路由
    app.register_blueprint(upload.bp)

    return app