from . basic import check, addflag, delflag, BIT


class BitFlag(object):
    def __init__(self, flags, value=0):
        if not isinstance(flags, list) and not isinstance(flags, tuple):
            raise TypeError('flags must be a list/tuple')
        if len(flags) == 0:
            raise ValueError('flags must have at least one string')
        self._val = {}
        if int(value) < 0:
            raise ValueError('value must be > 0')
        self._int = int(value)
        tmp = dir(self)
        if len(flags) > 64:
            raise OverflowError('max 64 flags, got {}'.format(len(flags)))
        for i in range(len(flags)):
            if flags[i] in tmp:
                raise ValueError('Flag \'{}\' has the same name as BitFlag method'.format(flags[i]))
            if '_' in (flags[i][0], flags[i][-1]):
                raise ValueError('Flag \'{}\' cannot start/end with underscore'.format(flags[i]))
        self._flags = flags

    def __getattribute__(self, attr):
        if attr[0] == '_' or attr not in self._flags:
            return super().__getattribute__(attr)
        return check(self._int, self._get_bit(attr))

    def __setattr__(self, attr, value):
        if attr[0] == '_':
            return super().__setattr__(attr, value)
        if value not in (True, False):
            raise ValueError('Flag \'{}\' can only be True or False, got \'{}\''.format(attr, value))
        if value == False:
            self._int = delflag(self._int, self._get_bit(attr))
        else:
            self._int = addflag(self._int, self._get_bit(attr))

    def __setitem__(self, key, value):
        if value not in (True, False):
            raise ValueError('Flag \'{}\' can only be True or False, got \'{}\''.format(key, value))
        if value == False:
            self._int = delflag(self._int, self._get_bit(key))
        else:
            self._int = addflag(self._int, self._get_bit(key))

    def __getitem__(self, key):
        return check(self._int, self._get_bit(key))

    def _get_bit(self, key):
        if key not in self._flags:
            raise KeyError('`{}` not in flag list'.format(key))
        return BIT[self._flags.index(key)]

    def as_int(self):
        return self._int

    def as_dict(self):
        return {k:check(self._int, self._get_bit(k)) for k in self._flags}

    def as_list(self):
        return list(self.as_dict().items())

    def compare(self, value):
        value = int(value)
        if int(value) < 0:
            raise ValueError('value must be > 0')
        return {k:check(value, self._get_bit(k)) for k in self._flags
                if check(self._int, self._get_bit(k)) != check(value, self._get_bit(k))}

    def update(self, value):
        r = self.compare(value)
        self._int = value
        return r