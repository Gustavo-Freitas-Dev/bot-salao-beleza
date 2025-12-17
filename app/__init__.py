from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.routes import whatsapp_bp
    app.register_blueprint(whatsapp_bp)

    return app
