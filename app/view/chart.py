from flask import Blueprint, render_template

app = Blueprint("chart", __name__, url_prefix="/chart", template_folder='templates/chart')

@app.route('')
def index():
    return render_template('index.html', title='chart')
