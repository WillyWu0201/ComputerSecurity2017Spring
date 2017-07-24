
def encrypt(x,l):
    y = x

    for i in range(len(x)):
        y[i] = l - 1 - int(x[i])
    return y


def decrypt(x,l):
    y = x

    for i in range(len(x)):
        y[i] = l - 1 - int(x[i])
    return y


aa = [0,0,0,0,0,0,0,0]

for i in range(8):
    aa[i] = str(i+54)


# 0-255
print(encrypt(aa,256))
