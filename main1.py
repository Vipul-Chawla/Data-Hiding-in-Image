
from gettext import install

import text_main as tm
import Stego as st
from PIL import Image
import numpy as np


def Encoder(image_path):
    # Cryptography Encryption and Compression
    Tree, message=tm.Encoder_text()
    print(message)  ## Compessed binary text
#      Steganography
    new_image=st.Encode_text(image_path,message)
    new_image=Image.fromarray(new_image)
    new_image.save("new_image.png")
    return Tree

 # Decode the image and text. In other word this function perform Retrive compress data, Decompression of Encrypted text and Decryption of text

def Decoder(Tree):
    im=Image.open("new_image.png")
    image=np.array(im)
    message=st.Decode_text(image)
    msg=tm.Decoder_text(Tree,message)
    with open("Process_text.txt",'w') as f:
        f.write(msg)

if __name__=="__main__":
    Tree=Encoder("download1.jpg")
    Decoder(Tree)
    print("Execution Successful")
