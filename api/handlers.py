# -*- coding: utf-8 -*-
from flask import jsonify
from werkzeug.exceptions import default_exceptions
from werkzeug.exceptions import HTTPException


class JSONExceptionHandler(object):
    def __init__(self, app=None):
        if app:
            self.app = app
            self.register(HTTPException)
            for code, v in default_exceptions.items():
                self.register(code)

    def std_handler(self, error):
        response = jsonify(message=str(error))
        response.status_code = error.code if isinstance(error, HTTPException) else 500
        return response

    def register(self, exception_or_code, handler=None):
        self.app.errorhandler(exception_or_code)(handler or self.std_handler)
