import binary
import numpy
from Crypto.Cipher import AES
initPRFLen = 4

import os
import SimpleCipher

from Crypto import Cipher
#from Crypto import Random


def randomcryptoint():

    # the value sys.maxint, which is either 231 - 1 or 263 - 1 depending on your platform.
    # 查看原始function，他的亂數都小於256
    b = numpy.random.randint(256, size=8)

    ans, _ = binary.varint(b)
    print(ans)
    return numpy.uint(ans)

def getBit(n, N, pos):
    val = (n & (1 << (N - pos)))
    if val > 0:
        return 1
    else:
        return 0


def prf(x, aesBlocks, numBlocks, temp, out ):
    #If request blocks greater than actual needed blocks, grow output array
    # initPRFLen 4

    cipher = GetCipher(AES.MODE_CTR)

    if numBlocks > initPRFLen :
        #out = make([]byte, numBlocks*aes.BlockSize)
        f = []

        for i in range(numBlocks*AES.block_size):
            f.append(0)
        print(f)

    for i in range(numBlocks):
        # get AES_k[i](x)

        #Encrypt encrypts the first block in src into dst.
        #Dst and src may point at the same memory.
        #Encrypt(dst, src []byte)
        #aesBlocks[i].Encrypt(temp, x)   #still go    ####這行不確定


        temp= SimpleCipher.encrypt(x,256)

        #print(temp)
        #print(len(x))
        #print(AES.block_size)

        #print(len(out))

        # get AES_k[i](x) ^ x
        for j in range(16):
            #XOR

            #print('i'+str(i))
            #print('j'+str(j))
            #print('====')
            #print(int(temp[j]) ^ int(x[j]))
            #print('====')
            out[i * AES.block_size + j] = int(temp[j]) ^ int(x[j])



    return x, aesBlocks, numBlocks, temp, out

def GetCipher(mode, iv='', ctr=''):
    # key (byte string)
    # The secret key to use in the symmetric cipher. It must be 16 (AES-128), 24 (AES-192), or 32 (AES-256) bytes long.
    key = b'_____________________32 byte key'

    if (mode == AES.MODE_CTR):
        ctr = os.urandom(16)
        cipher = AES.new(key, mode, counter=lambda: ctr)

    elif (mode == AES.MODE_CBC):
        cipher = AES.new(key, mode, iv)

    else:
        cipher = AES.new(key, mode)

    return cipher

def Padding(Input):
    return Input + (AES.block_size - len(Input) % AES.block_size) * chr(AES.block_size - len(Input) % AES.block_size)




#=================  test data ==================
#str = bytearray(b'12345678')
#print(str[0])

#aa = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#bb = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#cc = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#for i in range(16):
    #aa[i] = str(i+54)
    #bb[i] = str(i+54)

#print(aa)
#prf(aa,0,3,bb,cc)

#print(cc)