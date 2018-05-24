# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS

from config import Config
from api.handlers import JSONExceptionHandler
from api.routes import api_blueprint
from api.v1.routes import api_blueprint as api_v1_blueprint


app = Flask(__name__)
app.config.from_object(Config)

CORS(app)

app.register_blueprint(api_blueprint, url_prefix='/api')
app.register_blueprint(api_v1_blueprint, url_prefix='/api/v1')

handler = JSONExceptionHandler(app)


if __name__ == '__main__':
    app.run()
