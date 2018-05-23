# -*- coding: utf-8 -*-
import unittest
import pytest

from ..utils import *


class UtilsTest(unittest.TestCase):
    def test_get_expiry_month(self):
        assert get_expiry_month('H') == 3
        assert get_expiry_month('M') == 6
        assert get_expiry_month('U') == 9
        assert get_expiry_month('Z') == 12

        with pytest.raises(KeyError):
            get_expiry_month('E')

    def test_get_expiry_month_code(self):
        assert get_expiry_month_code(1) == 'F'
        assert get_expiry_month_code(12) == 'Z'

        with pytest.raises(IndexError) as e:
            get_expiry_month_code(13)
        assert str(e.value) == "Only 12 months in a year"

    def test_split_bloomberg_ticker(self):
        assert split_bloomberg_ticker('AIH8 Index').groups() == ('AI', 'H', '8', 'Index')
        assert split_bloomberg_ticker('CZ7 Comdty').groups() == ('C', 'Z', '7', 'Comdty')
        assert split_bloomberg_ticker('C Z7 Comdty').groups() == ('C ', 'Z', '7', 'Comdty')
        assert split_bloomberg_ticker('LAZ18 Comdty').groups() == ('LA', 'Z', '18', 'Comdty')
        assert split_bloomberg_ticker('OATZ7 Comdty').groups() == ('OAT', 'Z', '7', 'Comdty')

        with pytest.raises(ValueError) as e:
            split_bloomberg_ticker('AAPL Equity')
        assert str(e.value) == "Invalid Bloomberg ticker code"
