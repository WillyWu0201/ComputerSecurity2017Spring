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

# https: // golang.org / src / crypto / aes / cipher.go?s = 688:736  # L21
# // NewCipher creates and returns a new cipher.Block.
#   // The key argument should be the AES key,
#   // either 16, 24, or 32 bytes to select
#   // AES-128, AES-192, or AES-256.
#   func NewCipher(key []byte) (cipher.Block, error) {
#   	k := len(key)
#   	switch k {
#   	default:
#   		return nil, KeySizeError(k)
#   	case 16, 24, 32:
#   		break
#   	}
#   	return newCipher(key)
#   }