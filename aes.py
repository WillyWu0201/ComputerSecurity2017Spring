import os
from Crypto.Cipher import AES

_IV = os.urandom(16)		# 產生隨機亂數IV
_KEY = os.urandom(32)		# 設定Key
_BlockSize = AES.block_size	# Block Size

#padding
# _Pad = lambda s: s + (_BlockSize - len(s) % _BlockSize) * chr(_BlockSize - len(s) % _BlockSize)
# _Unpad = lambda s: s[0:-ord(s[-1])]

# 使用CBC加密
def aes_encrypt(data):
    cryptor = AES.new(_KEY, AES.MODE_CBC, _IV)
    return cryptor.encrypt(data)

# 使用CBC解密
def aes_decrypt(data):
    cryptor = AES.new(_KEY, AES.MODE_CBC, _IV)
    return _Unpad(cryptor.decrypt(data))