# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_restful import Api
from ..resources import Health
from cusip.resources import Cusip, FileUpload

api_blueprint = Blueprint('api_v1', __name__)
api = Api(api_blueprint)

api.add_resource(Health, '/health')

api.add_resource(Cusip, '/cusip')
api.add_resource(FileUpload, '/cusip/upload')
