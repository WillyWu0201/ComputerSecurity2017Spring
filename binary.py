import numpy


def uvarint(buf):
    x = numpy.uint64
    s = numpy.uint
    for i, b in enumerate(buf):
        if b < 0x80:
            if i > 0 or i == 9 and b > 1:
                return 0, -(i + 1)
            return x | b << s, i + 1
        print(x)
        x |= (b & 0x7f) << s   # s要有初始值，但不知道要為多少
        s += 7
    return 0, 0


def varint(buf):
    ux, n = uvarint(buf)
    x = numpy.int64(ux >> 1)
    if ux & 1 != 0:
        x ^= x
    return x, n
