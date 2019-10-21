from flask import Flask, jsonify
from config import DevelopmentConfig

from hello import HelloApi

# create app
app = Flask(__name__)

# load configuration
app.config.from_object(DevelopmentConfig)

# apis
app.register_blueprint(HelloApi, url_prefix='/hello')

# homepage
@app.route('/')
def hello():
    return "Hello World!"

# main method
if __name__ == '__main__':
    app.run()
