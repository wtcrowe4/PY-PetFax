from flask import ( Blueprint, render_template, request, redirect ) 


bp = Blueprint('fact', __name__, url_prefix="/facts")

# View
@bp.route('/new')
def new(): 
    return render_template('newFact.html')

# Data
@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form)
        return redirect('/facts')
    return render_template('facts.html')
