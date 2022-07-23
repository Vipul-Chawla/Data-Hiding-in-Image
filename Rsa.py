from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii


keyPair = RSA.generate(3072)
pubKey = keyPair.publickey()
pubKeyPEM = pubKey.exportKey()
privKeyPEM = keyPair.exportKey()

# Encryption file data using RSA Algo

def rsaEncryption(filePath):
  with open(filePath) as f:
    message=f.read()
    msg=bytes(message,'utf-8')
    encryptor = PKCS1_OAEP.new(pubKey)
    encrypted = encryptor.encrypt(msg)
    msg=binascii.hexlify(encrypted).decode('utf-8')
    return msg

# Decryption file data using RSA Algo
def rsaDecryption(msg):
    msg_bin=binascii.a2b_hex(msg)
    decryptor = PKCS1_OAEP.new(keyPair)
    decrypted = decryptor.decrypt(msg_bin)
    return decrypted.decode('utf-8')








