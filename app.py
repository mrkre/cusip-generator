# -*- coding: utf-8 -*-
from flask import Flask
from config import Config
from api.routes import api_blueprint
from api.v1.routes import api_blueprint as api_v1_blueprint


app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(api_blueprint, url_prefix='/api')
app.register_blueprint(api_v1_blueprint, url_prefix='/api/v1')


if __name__ == '__main__':
    app.run()
