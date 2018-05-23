# -*- coding: utf-8 -*-
BLOOMBERG_REGEX = r"^(?P<ticker>[A-Z]{1,3}|[A-Z]\s)(?P<expiry_month>[FGHJKMNQUVXZ])(?P<expiry_year>\d{1,2}) " \
                  r"(?P<sector>Index|Comdty)$"

FUTURES_EXPIRY_MONTH_MAP = {
    'F': 1,
    'G': 2,
    'H': 3,
    'J': 4,
    'K': 5,
    'M': 6,
    'N': 7,
    'Q': 8,
    'U': 9,
    'V': 10,
    'X': 11,
    'Z': 12
}
