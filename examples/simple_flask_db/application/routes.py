from flask import current_app as app
from flask import render_template

from .hello import HelloApi
from .books import BookApi

#blueprint lives here because flask has been told so
app.register_blueprint(HelloApi, url_prefix='/hello')
app.register_blueprint(BookApi, url_prefix='/books')

# homepage - renders homepage hello.html which is saved in same project

@app.route('/')
def hello():
    return render_template('hello.html')

#app.route and render_template are both flask items

# creating a second web page
@app.route('/rob')
def rob():
    return jsonify({"name":"rob"})