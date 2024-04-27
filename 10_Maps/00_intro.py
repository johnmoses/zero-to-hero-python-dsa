"""
Maps
"""
from collections.abc import MutableMapping

class MapBase(MutableMapping):
    class _item:
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other._key # compare items by key
        
        def __ne__(self, other):
            return not (self == other) # not equal

        def __lt__(self, other):
            return self._key < other._key # less than