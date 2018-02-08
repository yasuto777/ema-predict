from flask import Blueprint

app = Blueprint("api", __name__, url_prefix="/api")

@app.route('')
def hello():
    return 'hello'
