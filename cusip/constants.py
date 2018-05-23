# -*- coding: utf-8 -*-
FUTURES_MONTHS = 'FGHJKMNQUVXZ'

TICKER = 'ticker'

EXPIRATION_MONTH = 'expiration_month'

EXPIRATION_YEAR = 'expiration_year'

SECTOR = 'sector'

BLOOMBERG_REGEX = r"^(?P<%s>[A-Z]{1,3}|[A-Z]\s)(?P<%s>[%s])(?P<%s>\d{1,2}) (?P<%s>Index|Comdty)$" % \
                  (TICKER, EXPIRATION_MONTH, FUTURES_MONTHS, EXPIRATION_YEAR, SECTOR)

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
