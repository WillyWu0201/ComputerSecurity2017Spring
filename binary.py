import numpy


def uvarint(buf):
    x = numpy.int64(0)
    s = numpy.int(0)
    for i, b in enumerate(buf):
        if b < 0x80:
            if i > 0 or i == 9 and b > 1:
                return 0, -(i + 1)
            return x | b << s, i + 1
        x |= (b & 0x7f) << s
        s += 7
    return 0, 0


def varint(buf):
    ux, n = uvarint(buf)
    x = numpy.int64(ux >> 1)
    if ux & 1 != 0:
        x ^= x
    return x, n