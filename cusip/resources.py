# -*- coding: utf-8 -*-
import io
import csv
from flask import jsonify
from flask_restful import request, reqparse, Resource, abort
from werkzeug.datastructures import FileStorage

from .utils import generate_cusip_from_tickers, generate_cusip, split_bloomberg_ticker

ALLOWED_EXTENSIONS = ['csv', 'txt']


class Cusip(Resource):
    def post(self):
        json_data = request.get_json(force=True)

        if 'tickers' in json_data:
            if isinstance(json_data['tickers'], list):
                tickers = json_data['tickers']
            elif isinstance(json_data['tickers'], str):
                if json_data['tickers'].count('\n') > 0:
                    tickers = json_data['tickers'].splitlines()
                else:
                    tickers = json_data['tickers'].split(',')
            else:
                return abort(400, message="tickers must be a list or comma-delimited string")

            try:
                results = generate_cusip_from_tickers(tickers)
            except (ValueError, TypeError) as e:
                return abort(400, message=str(e))

        else:
            return abort(400, message="tickers is required")

        return jsonify({'results': results})


class FileUpload(Resource):
    post_parser = reqparse.RequestParser()
    post_parser.add_argument('file', required=True, type=FileStorage, location='files')

    def post(self):
        args = self.post_parser.parse_args()

        file = args['file']
        extension = file.filename.rsplit('.', 1)[1].lower()

        if '.' in file.filename and not extension in ALLOWED_EXTENSIONS:
            return abort(400, message="File extension is not one of our supported types.")

        # parse file
        decoded_file = file.read().decode('utf-8')
        io_string = io.StringIO(decoded_file)

        next(io_string)  # skip header

        try:
            results = [generate_cusip(**split_bloomberg_ticker(line[0])) for line in csv.reader(io_string, delimiter=',')]
        except (ValueError, TypeError) as e:
            return abort(400, message=str(e))

        return jsonify({'results': results})
