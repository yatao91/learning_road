# -*- coding: utf-8 -*-
import simplejson as json

print(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]))

print(json.dumps("\"foo\bar"))

print(json.dumps(u'\u1234'))

print(json.dumps('\\'))

print(json.dumps({"c": 0, "b": 0, "hardware": 0}, sort_keys=True))

from simplejson.compat import StringIO

io = StringIO()

json.dump(['streaming API'], io)

print(io.getvalue())

obj = [1, 2, 3, {'4': '5', '6': '7'}]

print(json.dumps(obj, separators=(',', ':'), sort_keys=True))

print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4 * ' '))

obj = [u'foo', {u'bar': [u'baz', None, 1.0, 2]}]
print(json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]') == obj)

print(json.loads('"\\"foo\\bar"') == u'"foo\x08ar')

io = StringIO('["streaming API"]')
print(json.load(io)[0] == 'streaming API')

from decimal import Decimal

print(json.loads('1.1', use_decimal=True) == Decimal('1.1'))


def as_complex(dct):
    if '__complex__' in dct:
        return complex(dct['real'], dct['imag'])
    return dct


print(json.loads('{"__complex__": true, "real": 1, "imag": 2}', object_hook=as_complex))

import decimal

print(json.loads('1.1', parse_float=decimal.Decimal) == decimal.Decimal('1.1'))
