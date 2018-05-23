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

    def test_round_down(self):
        assert round_down(7) == 0
        assert round_down(17) == 10
        assert round_down(2018) == 2010

    def test_round_up(self):
        assert round_up(7) == 10
        assert round_up(17) == 20
        assert round_up(2018) == 2020

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
        assert str(e.value) == "Invalid Bloomberg ticker code - AAPL Equity"

    def test_get_alphabet_ordinal(self):
        assert get_alphabet_ordinal('a') == 1
        assert get_alphabet_ordinal('z') == 26

        with pytest.raises(TypeError) as e:
            get_alphabet_ordinal(1)
        assert str(e.value) == "Only string allowed"

    def test_check_cusip_digit(self):
        assert check_cusip_digit('03783310') == 0
        assert check_cusip_digit('17275R10') == 2
        assert check_cusip_digit('38259P50') == 8
        assert check_cusip_digit('AIH82018') == 5
        assert check_cusip_digit('CZ720177') == 5
        assert check_cusip_digit('LAZ82018') == 0
        assert check_cusip_digit('ESZ82018') == 9

        with pytest.raises(TypeError) as e:
            check_cusip_digit(1234567)
        assert str(e.value) == "Only string allowed"

        with pytest.raises(ValueError) as e:
            check_cusip_digit('1234567')
        assert str(e.value) == "Expected cusip to contain 8 characters"

        with pytest.raises(ValueError) as e:
            check_cusip_digit('^^^^^^^^')
        assert str(e.value) == "cusip contains illegal character - ^ at position 0"

    def test_generate_cusip(self):
        assert generate_cusip(**{TICKER: 'AI', EXPIRATION_MONTH: 'H', EXPIRATION_YEAR: 2018}) == 'AIH820185'
        assert generate_cusip(**{TICKER: 'C', EXPIRATION_MONTH: 'Z', EXPIRATION_YEAR: 2017}) == 'CZ7201775'
        assert generate_cusip(**{TICKER: 'LA', EXPIRATION_MONTH: 'Z', EXPIRATION_YEAR: 2018}) == 'LAZ820180'
        assert generate_cusip(**{TICKER: 'OAT', EXPIRATION_MONTH: 'Z', EXPIRATION_YEAR: 2017}) == 'OATZ72011'
        assert generate_cusip(**split_bloomberg_ticker('ESZ18 Index')) == 'ESZ820189'
        assert generate_cusip(**split_bloomberg_ticker('C Z8 Comdty')) == 'CZ8201881'

    def test_generate_cusip_from_tickers(self):
        assert generate_cusip_from_tickers(['ESZ18 Index', 'C Z8 Comdty']) == ['ESZ820189', 'CZ8201881']
        assert generate_cusip_from_tickers(['ESZ18 Index', 'C Z8 Comdty']) == ['ESZ820189', 'CZ8201881']
