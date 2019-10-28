from flask import Blueprint

HelloApi = Blueprint('hello_api', __name__)

@HelloApi.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)