import Rsa
import huffman

# Text Encryption and lossless Compression

def Encoder_text():
    msg=Rsa.rsaEncryption("text");
    encoding,tree=huffman.Huffman_Encoding(msg)
    buffer=bytearray(encoding,encoding="utf-8")
    return tree, buffer

# Text Decryption and Decompression

def Decoder_text(Tree,msg):
    decoding=huffman.Huffman_Decoding(str(msg),Tree)
    msg2=  Rsa.rsaDecryption(decoding)
    return msg2
