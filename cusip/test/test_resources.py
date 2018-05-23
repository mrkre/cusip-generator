# -*- coding: utf-8 -*-
import unittest
import json

from app import app


class TestCusipResources(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_cusip_post_str(self):
        response = self.app.post('/api/v1/cusip', json={'tickers': 'ESZ18 Index'})

        self.assertEquals(json.loads(response.get_data().decode()), {'results': ['ESZ820189']})

    def test_cusip_post_list(self):
        response = self.app.post('/api/v1/cusip', json={'tickers': ['ESZ18 Index', 'C Z8 Comdty']})

        self.assertEquals(json.loads(response.get_data().decode()), {'results': ['ESZ820189', 'CZ8201881']})
