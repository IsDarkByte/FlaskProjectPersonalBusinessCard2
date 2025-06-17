import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_app_creation():
    from app import create_app

    app = create_app()
    assert app is not None


def test_config():
    from app import create_app

    app = create_app()
    assert app.config["SECRET_KEY"] is not None
    assert app.config["SQLALCHEMY_DATABASE_URI"] is not None
