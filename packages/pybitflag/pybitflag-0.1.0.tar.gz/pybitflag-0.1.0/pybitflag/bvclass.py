from . basic import bitcount, explode_num, implode_num


class BitValue(object):
    def __init__(self, vals, num=0):
        if not isinstance(vals, dict):
            raise TypeError('`vals` must be a dict')
        if len(vals) == 0:
            raise ValueError('vals must have at lease one key:value')
        self._val = {k:dict(length=bitcount(v), max=v, value=0) for k,v in vals.items()}
        if sum([x['length'] for x in self._val.values()]) > 64:
            raise OverflowError('max length is 64 bits, got {}'.format(sum([x['length'] for x in self._val.values()])))
        if num > 0:
            t = explode_num(num, [x['length'] for x in self._val.values()])
            for k,v in zip(self._val.keys(), t):
                self._val[k]['value'] = v

    def __setitem__(self, key, value):
        if value > self._val[key]['max']:
            raise ValueError('Max value for {} is {} got {}'.format(key,
                             self._val[key]['max'], value))
        elif value < 0:
            raise ValueError('Min value is 0')
        self._val[key]['value'] = value

    def __getitem__(self, key):
        return self._val[key]['value']

    def __setattr__(self, key, value):
        if key[0] == '_':
            return super().__setattr__(key, value)
        if value > self._val[key]['max']:
            raise ValueError('max value for {} is {}, got {}'.format(key,
                             self._val[key]['max'], value))
        self._val[key]['value'] = value

    def __getattribute__(self, key):
        if key[0] == '_' or key not in self._val:
            return super().__getattribute__(key)
        return self._val[key]['value']

    def as_int(self):
        return implode_num([(v['length'],v['value']) for v in self._val.values()])

    def as_dict(self):
        return {k:v['value'] for k,v in self._val.items()}

    def as_list(self):
        return [(k,v['value']) for k,v in self._val.items()]

    def compare(self, value):
        value = int(value)
        if value < 0:
            raise ValueError('value must be > 0')
        t = explode_num(value, [x['length'] for x in self._val.values()])
        return {k:v for k,v in zip(self._val.keys(), t) if v != self._val[k]['value']}

    def update(self, value):
        value = int(value)
        r = self.compare(value)
        for k,v in r.items():
            self._val[k]['value'] = v
        return r