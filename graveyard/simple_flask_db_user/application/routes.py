from flask import current_app as app
from flask_user import login_required

from .hello import HelloApi
from .books import BookApi


app.register_blueprint(HelloApi, url_prefix='/hello')
app.register_blueprint(BookApi, url_prefix='/books')

# homepage
@app.route('/')
@login_required
def hello():
    return "Hello World!"
