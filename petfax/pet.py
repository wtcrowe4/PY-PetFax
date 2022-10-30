from flask import (Blueprint, render_template)
import json

bp = Blueprint('pet', __name__, url_prefix='/pets')
pets = json.load(open('pets.json'))

@bp.route('/')
def index():
    return render_template('index.html', pets=pets)

@bp.route('/<int:id>')
def show(id):
    return render_template('show.html', pet=pets[id-1])