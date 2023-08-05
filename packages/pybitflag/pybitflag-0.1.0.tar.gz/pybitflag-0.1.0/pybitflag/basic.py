from functools import reduce


BIT = [1 << x for x in range(64)]
MAX = [reduce(lambda x,y: x|y, BIT[:i+1]) for i in range(len(BIT))]


def check(haystack, needle):
    if isinstance(needle, list) or isinstance(needle, tuple):
        return check_multi(haystack, needle)
    return haystack & needle == needle

def check_multi(haystack, needles):
    i = newflag(needles)
    return haystack & i == i

def newflag(flags):
    return reduce(lambda x,y: x|y, flags)

def addflag(ori, flag):
    if isinstance(flag, list) or isinstance(flag, tuple):
        return addflag_multi(ori, flag)
    return ori | flag

def addflag_multi(ori, flags):
    i = newflag(flags)
    return ori | i

def delflag(ori, flag):
    if isinstance(flag, list) or isinstance(flag, tuple):
        return delflag_multi(ori, flag)
    return ori ^ flag if addflag(ori, flag) == ori else ori

def delflag_multi(ori, flags):
    tmp = ori
    for flag in flags:
        tmp = delflag(tmp, flag)
    return tmp

def bitcount(num):
    bit = 0
    while num > 0:
        bit += 1
        num >>= 1
    return bit

def prepend_num(initial, length, value):
    return (initial << length) | value

def explode_num(num, lengths):
    result = []
    for length in lengths:
        result.append(num & MAX[length-1])
        num >>= length
    return result

def implode_num(data):
    result = 0
    for length, value in data[::-1]:
        result = prepend_num(result, length, value)
    return result