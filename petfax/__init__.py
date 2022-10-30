from flask import Flask

def create_app():
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return 'PetFax Index Route'
    
    @app.route('/pets')
    def pets():
        return 'PetFax Pets Route'
    
    return app