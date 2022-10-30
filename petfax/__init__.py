from flask import Flask

def create_app():
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return 'PetFax Index Route'
    
    from . import pet
    app.register_blueprint(pet.bp)
    
    return app