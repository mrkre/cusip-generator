# -*- coding: utf-8 -*-
import re
import math
import datetime as dt

from .constants import *


def get_expiration_month(month_code):
    """
    Returns expiry month given an expiry month code, throws KeyError if not found
    :param month_code:
    :type month_code: str
    :return: expiration month
    """
    return FUTURES_EXPIRY_MONTH_MAP[month_code]


def get_expiration_month_code(month):
    """
    Get futures expiration month code given a month
    :param month:
    :type month: int
    :return: expiration month
    """
    if not isinstance(month, int):
        raise TypeError("month needs to be a string")

    if month not in range(1, 13):
        raise IndexError("Only 12 months in a year")
    return list(FUTURES_EXPIRY_MONTH_MAP)[month - 1]


def round_down(x):
    """
    Simple function to round integer down to nearest 10
    :param x:
    :return:
    """
    return int(math.floor(x / 10.0)) * 10


def round_up(x):
    """
    Simple function to round integer up to nearest 10
    :param x:
    :return:
    """
    return int(math.ceil(x / 10.0)) * 10


def calc_year(digits, year=dt.datetime.now().year):
    """
    Given digits (7, 17, 27) and returns
    :param digits:
    :type digits: int
    :param year: year to use in calculation, defaults to current year
    :type year: int
    :return: derived year
    """
    year_mod = divmod(year, 100)

    century = year_mod[0] * 100
    remainder = year_mod[1]

    if digits == remainder or digits == remainder % 10:
        return century + remainder
    elif digits < remainder and digits < round_down(remainder):
        return century + round_up(remainder) + digits
    else:
        return century + digits


def split_bloomberg_ticker(bloomberg_ticker):
    """
    Split a Bloomberg ticker into respective components

    :param bloomberg_ticker:
    :type bloomberg_ticker: str
    :return: Returns regex match object, access results in a tuple by match.groups()
             or named groups by match.group('name')
    """
    match = re.search(BLOOMBERG_REGEX, bloomberg_ticker)

    if match:
        return dict({
            TICKER: match.group(TICKER).strip(),
            EXPIRATION_MONTH: match.group(EXPIRATION_MONTH),
            EXPIRATION_YEAR: calc_year(int(match.group(EXPIRATION_YEAR))),
            SECTOR: match.group(SECTOR),
        })
    raise ValueError("Invalid Bloomberg ticker code")


def get_alphabet_ordinal(c):
    if type(c) != str:
        raise TypeError("Only string allowed")
    return ord(c) - 96


def check_cusip_digit(cusip):
    sum = 0

    if type(cusip) != str:
        raise TypeError("Only string allowed")

    if len(cusip) != 8:
        raise ValueError("Expected cusip to contain 8 characters")

    for i, c in enumerate(list(cusip)):
        if c.isdigit():
            v = int(c)
        elif c.isalpha():
            p = get_alphabet_ordinal(c.lower())
            v = p + 9
        elif c == '*':
            v = 36
        elif c == '@':
            v = 37
        elif c == '#':
            v = 38
        else:
            raise ValueError("cusip contains illegal character - %s at position %s" % (c, i))

        if (i + 1) % 2 == 0:
            v *= 2

        sum += int(v / 10) + int(v % 10)

    return (10 - (sum % 10)) % 10


def generate_cusip(**kwargs):
    """
    Generate CUSIP based on kwargs passed
    :param kwargs:
    :return:
    """
    ticker = kwargs[TICKER]
    expiration_month = kwargs[EXPIRATION_MONTH]
    expiration_year = kwargs[EXPIRATION_YEAR]

    final_digit_year = str(expiration_year)[-1]
    year = str(expiration_year)

    ticker_length = len(ticker)
    if ticker_length == 1:
        year += str(expiration_year)[-1]
    elif ticker_length == 3:
        year = str(expiration_year)[:-1]

    s = "%s%s%s%s" % (ticker, expiration_month, final_digit_year, year)
    print(s)
    return "%s%s" % (s, check_cusip_digit(s))
