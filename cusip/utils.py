# -*- coding: utf-8 -*-
import re

from .constants import FUTURES_EXPIRY_MONTH_MAP, BLOOMBERG_REGEX


def get_expiry_month(month_code):
    """
    Returns expiry month given an expiry month code, throws KeyError if not found
    :param month_code:
    :type month_code: str
    :return:
    """
    return FUTURES_EXPIRY_MONTH_MAP[month_code]


def get_expiry_month_code(month):
    """
    Get futures expiry month code given a month
    :param month:
    :return:
    """
    if not isinstance(month, int):
        raise TypeError("month needs to be a string")

    if month not in range(1, 13):
        raise IndexError("Only 12 months in a year")
    return list(FUTURES_EXPIRY_MONTH_MAP)[month - 1]


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
        return match
    raise ValueError("Invalid Bloomberg ticker code")
