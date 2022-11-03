from flask import Flask
import os
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

load_dotenv()
database = os.getenv('DATABASE_URI')

def create_app():
    app = Flask(__name__)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    
    app.config['SQLALCHEMY_DATABASE_URI'] = database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)
    
    Bootstrap(app)
    
    @app.route('/')
    def index():
        return 'PetFax Index Route'
    
    from . import pet
    app.register_blueprint(pet.bp)
    
    from . import fact
    app.register_blueprint(fact.bp)
    
    return app