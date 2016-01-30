#! /usr/bin/env python
# -*- coding: utf-8 -*

Descriptions = {}

Descriptions['1987'] = {
    -6 : 'total_len',
    -5 : 'tpdu',
    -4 : 'message_explain',
    -3 : 'message_type',
    -2 : 'Bitmap',
    2 : 'Primary account number (PAN)' ,
    3 : 'Processing code' ,
    4 : 'Amount, transaction' ,
    5 : 'Amount, settlement' ,
    6 : 'Amount, cardholder billing' ,
    7 : 'Transmission date & time' ,
    8 : 'Amount, cardholder billing fee' ,
    9 : 'Conversion rate, settlement' ,
    10 : 'Conversion rate, cardholder billing' ,
    11 : 'System trace audit number' ,
    12 : 'Time, local transaction (hhmmss)' ,
    13 : 'Date, local transaction (MMDD)' ,
    14 : 'Date, expiration' ,
    15 : 'Date, settlement' ,
    16 : 'Date, conversion' ,
    17 : 'Date, capture' ,
    18 : 'Merchant type' ,
    19 : 'Acquiring institution country code' ,
    20 : 'PAN extended, country code' ,
    21 : 'Forwarding institution. country code' ,
    22 : 'Point of service entry mode' ,
    23 : 'Application PAN sequence number' ,
    24 : 'Network International identifier (NII)' ,
    25 : 'Point of service condition code' ,
    26 : 'Point of service capture code' ,
    27 : 'Authorizing identification response length' ,
    28 : 'Amount, transaction fee' ,
    29 : 'Amount, settlement fee' ,
    30 : 'Amount, transaction processing fee' ,
    31 : 'Amount, settlement processing fee' ,
    32 : 'Acquiring institution identification code' ,
    33 : 'Forwarding institution identification code' ,
    34 : 'Primary account number, extended' ,
    35 : 'Track 2 data' ,
    36 : 'Track 3 data' ,
    37 : 'Retrieval reference number' ,
    38 : 'Authorization identification response' ,
    39 : 'Response code' ,
    40 : 'Service restriction code' ,
    41 : 'Card acceptor terminal identification' ,
    42 : 'Card acceptor identification code' ,
    43 : 'Card acceptor name/location' ,
    44 : 'Additional response data' ,
    45 : 'Track 1 data' ,
    46 : 'Additional data - ISO' ,
    47 : 'Additional data - national' ,
    48 : 'Additional data - private' ,
    49 : 'Currency code, transaction' ,
    50 : 'Currency code, settlement' ,
    51 : 'Currency code, cardholder billing' ,
    52 : 'Personal identification number data' ,
    53 : 'Security related control information' ,
    54 : 'Additional amounts' ,
    55 : 'Reserved ISO' ,
    56 : 'Reserved ISO' ,
    57 : 'Reserved national' ,
    58 : 'Reserved national' ,
    59 : 'Reserved national' ,
    60 : 'Reserved national' ,
    61 : 'Reserved private' ,
    62 : 'Reserved private' ,
    63 : 'Reserved private' ,
    64 : 'Message authentication code (MAC)' ,
    65 : 'Bitmap, extended' ,
    66 : 'Settlement code' ,
    67 : 'Extended payment code' ,
    68 : 'Receiving institution country code' ,
    69 : 'Settlement institution country code' ,
    70 : 'Network management information code' ,
    71 : 'Message number' ,
    72 : 'Message number, last' ,
    73 : 'Date, action (YYMMDD)' ,
    74 : 'Credits, number' ,
    75 : 'Credits, reversal number' ,
    76 : 'Debits, number' ,
    77 : 'Debits, reversal number' ,
    78 : 'Transfer number' ,
    79 : 'Transfer, reversal number' ,
    80 : 'Inquiries number' ,
    81 : 'Authorizations, number' ,
    82 : 'Credits, processing fee amount' ,
    83 : 'Credits, transaction fee amount' ,
    84 : 'Debits, processing fee amount' ,
    85 : 'Debits, transaction fee amount' ,
    86 : 'Credits, amount' ,
    87 : 'Credits, reversal amount' ,
    88 : 'Debits, amount' ,
    89 : 'Debits, reversal amount' ,
    90 : 'Original data elements' ,
    91 : 'File update code' ,
    92 : 'File security code' ,
    93 : 'Response indicator' ,
    94 : 'Service indicator' ,
    95 : 'Replacement amounts' ,
    96 : 'Message security code' ,
    97 : 'Amount, net settlement' ,
    98 : 'Payee' ,
    99 : 'Settlement institution identification code' ,
    100 : 'Receiving institution identification code' ,
    101 : 'File name' ,
    102 : 'Account identification 1' ,
    103 : 'Account identification 2' ,
    104 : 'Transaction description' ,
    105 : 'Reserved for ISO use' ,
    106 : 'Reserved for ISO use' ,
    107 : 'Reserved for ISO use' ,
    108 : 'Reserved for ISO use' ,
    109 : 'Reserved for ISO use' ,
    110 : 'Reserved for ISO use' ,
    111 : 'Reserved for ISO use' ,
    112 : 'Reserved for national use' ,
    113 : 'Reserved for national use' ,
    114 : 'Reserved for national use' ,
    115 : 'Reserved for national use' ,
    116 : 'Reserved for national use' ,
    117 : 'Reserved for national use' ,
    118 : 'Reserved for national use' ,
    119 : 'Reserved for national use' ,
    120 : 'Reserved for private use' ,
    121 : 'Reserved for private use' ,
    122 : 'Reserved for private use' ,
    123 : 'Reserved for private use' ,
    124 : 'Reserved for private use' ,
    125 : 'Reserved for private use' ,
    126 : 'Reserved for private use' ,
    127 : 'Reserved for private use' ,
    128 : 'Message authentication code'
}


ContentTypes = {}

ContentTypes['pos'] = {
    -6 : {'content_type':'BCD',        'max_len': 4,   'len_type': 'fixed'},
    -5 : {'content_type':'BCD',        'max_len': 10,   'len_type': 'fixed'},
    -4 : {'content_type':'BCD',        'max_len': 12,   'len_type': 'fixed'},
    -3 : {'content_type':'BCD',        'max_len': 4,    'len_type': 'fixed'},
    -2 : {'content_type':'BINARY',     'max_len': 64,   'len_type': 'fixed_b'},
     2 : {'content_type':'BCD',        'max_len': 19,   'len_type': 'LLVAR'},
     3 : {'content_type':'BCD',        'max_len': 6,    'len_type': 'fixed'},
     4 : {'content_type':'BCD',        'max_len': 12,   'len_type': 'fixed'},
    11 : {'content_type':'BCD',        'max_len': 6,    'len_type': 'fixed'},
    12 : {'content_type':'BCD',        'max_len': 6,    'len_type': 'fixed'},
    13 : {'content_type':'BCD',        'max_len': 4,    'len_type': 'fixed'},
    14 : {'content_type':'BCD',        'max_len': 4,    'len_type': 'fixed'},
    15 : {'content_type':'BCD',        'max_len': 4,    'len_type': 'fixed'},
    22 : {'content_type':'BCD',        'max_len': 3,    'len_type': 'fixed'},
    23 : {'content_type':'BCD',        'max_len': 3,    'len_type': 'fixed'},
    25 : {'content_type':'BCD',        'max_len': 2,    'len_type': 'fixed'},
    26 : {'content_type':'BCD',        'max_len': 2,    'len_type': 'fixed'},
    32 : {'content_type':'BCD',        'max_len': 11,   'len_type': 'LLVAR'},
    35 : {'content_type':'BCD',        'max_len': 37,   'len_type': 'LLVAR'},
    36 : {'content_type':'BCD',        'max_len': 104,  'len_type': 'LLLVAR'},
    37 : {'content_type':'ASCII',      'max_len': 12,   'len_type': 'fixed'},
    38 : {'content_type':'ASCII',      'max_len': 6,    'len_type': 'fixed'},
    39 : {'content_type':'ASCII',      'max_len': 2,    'len_type': 'fixed'},
    41 : {'content_type':'ASCII',      'max_len': 8,    'len_type': 'fixed'},
    42 : {'content_type':'ASCII',      'max_len': 15,   'len_type': 'fixed'},
    44 : {'content_type':'ASCII',      'max_len': 25,   'len_type': 'LLVAR'},
    48 : {'content_type':'BCD',        'max_len': 322,  'len_type': 'LLLVAR'},
    49 : {'content_type':'ASCII',      'max_len': 3,    'len_type': 'fixed'},
    52 : {'content_type':'BINARY',     'max_len': 64,   'len_type': 'fixed_b'},
    53 : {'content_type':'BCD',        'max_len': 16,   'len_type': 'fixed'},
    54 : {'content_type':'ASCII',      'max_len': 322,  'len_type': 'LLLVAR'},
    55 : {'content_type':'BCD',        'max_len': 255,  'len_type': 'LLLVAR'},
    58 : {'content_type':'BCD',        'max_len': 100,  'len_type': 'LLLVAR'},
    60 : {'content_type':'BCD',        'max_len': 17,   'len_type': 'LLLVAR'},
    61 : {'content_type':'BCD',        'max_len': 29,   'len_type': 'LLLVAR'},
    62 : {'content_type':'ASCII',      'max_len': 512,  'len_type': 'LLLVAR'},
    63 : {'content_type':'ASCII',      'max_len': 163,  'len_type': 'LLLVAR'},
    64 : {'content_type':'BINARY',     'max_len': 64,   'len_type': 'fixed_b'}
}

ContentTypes['yb'] = {
    -6 : {'content_type':'BCD',        'max_len': 4,   'len_type': 'fixed'},
    -5 : {'content_type':'BCD',        'max_len': 10,   'len_type': 'fixed'},
    -4 : {'content_type':'BCD',        'max_len': 12,   'len_type': 'fixed'},
    -3 : {'content_type':'BCD',        'max_len': 4,    'len_type': 'fixed'},
    -2 : {'content_type':'BINARY',     'max_len': 64,   'len_type': 'fixed_b'},
     2 : {'content_type':'BCD',        'max_len': 19,   'len_type': 'LLVAR'},
     3 : {'content_type':'BCD',        'max_len': 6,    'len_type': 'fixed'},
     4 : {'content_type':'BCD',        'max_len': 12,   'len_type': 'fixed'},
    11 : {'content_type':'BCD',        'max_len': 6,    'len_type': 'fixed'},
    12 : {'content_type':'BCD',        'max_len': 6,    'len_type': 'fixed'},
    13 : {'content_type':'BCD',        'max_len': 4,    'len_type': 'fixed'},
    14 : {'content_type':'BCD',        'max_len': 4,    'len_type': 'fixed'},
    15 : {'content_type':'BCD',        'max_len': 4,    'len_type': 'fixed'},
    22 : {'content_type':'BCD',        'max_len': 3,    'len_type': 'fixed'},
    23 : {'content_type':'BCD',        'max_len': 3,    'len_type': 'fixed'},
    25 : {'content_type':'BCD',        'max_len': 2,    'len_type': 'fixed'},
    26 : {'content_type':'BCD',        'max_len': 2,    'len_type': 'fixed'},
    32 : {'content_type':'BCD',        'max_len': 11,   'len_type': 'LLVAR'},
    35 : {'content_type':'BCD',        'max_len': 37,   'len_type': 'LLVAR'},
    36 : {'content_type':'BCD',        'max_len': 104,  'len_type': 'LLLVAR'},
    37 : {'content_type':'ASCII',      'max_len': 12,   'len_type': 'fixed'},
    38 : {'content_type':'ASCII',      'max_len': 6,    'len_type': 'fixed'},
    39 : {'content_type':'ASCII',      'max_len': 2,    'len_type': 'fixed'},
    41 : {'content_type':'ASCII',      'max_len': 8,    'len_type': 'fixed'},
    42 : {'content_type':'ASCII',      'max_len': 15,   'len_type': 'fixed'},
    44 : {'content_type':'ASCII',      'max_len': 25,   'len_type': 'LLVAR'},
    46 : {'content_type':'ASCII',      'max_len': 300,  'len_type': 'LLLVAR'},
    48 : {'content_type':'BCD',        'max_len': 322,  'len_type': 'LLLVAR'},
    49 : {'content_type':'ASCII',      'max_len': 3,    'len_type': 'fixed'},
    52 : {'content_type':'BINARY',     'max_len': 64,   'len_type': 'fixed_b'},
    53 : {'content_type':'BCD',        'max_len': 16,   'len_type': 'fixed'},
    54 : {'content_type':'ASCII',      'max_len': 20,  'len_type': 'LLLVAR'},
    55 : {'content_type':'BCD',        'max_len': 255,  'len_type': 'LLLVAR'},
    56 : {'content_type':'ASCII',      'max_len': 300,  'len_type': 'LLLVAR'},
    58 : {'content_type':'ASCII',      'max_len': 100,  'len_type': 'LLLVAR'},
    60 : {'content_type':'BCD',        'max_len': 13,   'len_type': 'LLLVAR'},
    61 : {'content_type':'BCD',        'max_len': 29,   'len_type': 'LLLVAR'},
    62 : {'content_type':'ASCII',      'max_len': 512,  'len_type': 'LLLVAR'},
    63 : {'content_type':'ASCII',      'max_len': 163,  'len_type': 'LLLVAR'},
    64 : {'content_type':'BINARY',     'max_len': 64,   'len_type': 'fixed_b'}
}