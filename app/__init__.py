from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    print("Main blueprint registered")

    from app.auth import bp as auth_bp
    from app.auth import routes  # noqa: F401 импортируем маршруты до регистрации blueprint
    app.register_blueprint(auth_bp, url_prefix="/auth")

    # Импортируем модели после создания приложения
    from app import models  # noqa: F401

    return app



