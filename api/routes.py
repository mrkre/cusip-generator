# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_restful import Api
from .resources import Health

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)

api.add_resource(Health, '/health')
