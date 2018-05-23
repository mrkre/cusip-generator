# -*- coding: utf-8 -*-
import unittest
import pytest

from ..utils import *
from ..constants import *


class UtilsTest(unittest.TestCase):
    def test_get_expiry_month(self):
        assert get_expiration_month('H') == 3
        assert get_expiration_month('M') == 6
        assert get_expiration_month('U') == 9
        assert get_expiration_month('Z') == 12

        with pytest.raises(KeyError):
            get_expiration_month('E')

    def test_get_expiry_month_code(self):
        assert get_expiration_month_code(1) == 'F'
        assert get_expiration_month_code(12) == 'Z'

        with pytest.raises(IndexError) as e:
            get_expiration_month_code(13)
        assert str(e.value) == "Only 12 months in a year"

    def test_calc_year(self):
        assert calc_year(3, 2015) == 2023
        assert calc_year(7, 2017) == 2017
        assert calc_year(18, 2018) == 2018
        assert calc_year(28, 2018) == 2028
        assert calc_year(0, 2018) == 2020
        # update tests below every year since it uses datetime
        assert calc_year(17) == 2017
        assert calc_year(8) == 2018
        assert calc_year(7) == 2027
        assert calc_year(1) == 2021

    def test_split_bloomberg_ticker(self):
        assert split_bloomberg_ticker('AIH8 Index') == dict(
            {TICKER: 'AI', EXPIRATION_MONTH: 'H', EXPIRATION_YEAR: 2018, SECTOR: 'Index'})
        assert split_bloomberg_ticker('CZ8 Comdty') == dict(
            {TICKER: 'C', EXPIRATION_MONTH: 'Z', EXPIRATION_YEAR: 2018, SECTOR: 'Comdty'})
        assert split_bloomberg_ticker('C Z17 Comdty') == dict(
            {TICKER: 'C', EXPIRATION_MONTH: 'Z', EXPIRATION_YEAR: 2017, SECTOR: 'Comdty'})
        assert split_bloomberg_ticker('LAZ18 Comdty') == dict(
            {TICKER: 'LA', EXPIRATION_MONTH: 'Z', EXPIRATION_YEAR: 2018, SECTOR: 'Comdty'})
        assert split_bloomberg_ticker('OATZ7 Comdty') == dict(
            {TICKER: 'OAT', EXPIRATION_MONTH: 'Z', EXPIRATION_YEAR: 2027, SECTOR: 'Comdty'})

        with pytest.raises(ValueError) as e:
            split_bloomberg_ticker('AAPL Equity')
        assert str(e.value) == "Invalid Bloomberg ticker code"

    def test_generate_cusip(self):
        components = split_bloomberg_ticker('ESZ18 Index')
        assert generate_cusip(ticker=components[TICKER], expiration_month=components[EXPIRATION_MONTH],
                              expiration_year=components[EXPIRATION_YEAR]) == 'ESZ82018'
