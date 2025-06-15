def test_app_creation():
    from app import create_app
    app = create_app()
    assert app is not None

def test_config():
    from app import create_app
    app = create_app()
    assert app.config['SECRET_KEY'] is not None
    assert app.config['SQLALCHEMY_DATABASE_URI'] is not None 