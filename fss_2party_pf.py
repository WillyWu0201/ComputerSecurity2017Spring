import binary
from Crypto.Cipher import AES
import FssKeyEq2P
import os

def GenerateTreePF(a, b):
    fssKeys = FssKeyEq2P[2]

    tempRand1 = bytes[AES.BlockSize + 1]

    os.urandom().Read(tempRand1)

    fssKeys[0].SInit = tempRand1[:AES.BlockSize]

    fssKeys[0].TInit = tempRand1[AES.BlockSize] % 2

    fssKeys[1].SInit = bytes[AES.BlockSize]

    os.urandom().Read(fssKeys[1].SInit)