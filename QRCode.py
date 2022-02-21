from unittest import result
import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

"""
# Creating a QRCode
# pip install qrcode[pil]

data = "Don't Forget to Subscribe"

qr = qrcode.QRCode(version=1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color='back', back_color='white')

img.save('C:/Users/thisd/Desktop/New folder/my_qrcode.png')"""



# Reading a QRCode
# pip install pyzbar

img = Image.open('C:/Users/thisd/Desktop/New folder/my_qrcode.png')
result = decode(img)
print(result)

