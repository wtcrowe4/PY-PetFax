from flask import Flask
from flask_bootstrap import Bootstrap

def create_app():
    app = Flask(__name__)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    Bootstrap(app)
    
    @app.route('/')
    def index():
        return 'PetFax Index Route'
    
    from . import pet
    app.register_blueprint(pet.bp)
    
    from . import fact
    app.register_blueprint(fact.bp)
    
    return app