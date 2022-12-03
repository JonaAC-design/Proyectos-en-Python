import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

qr = pyqrcode.create("Hola que hace?")
qr.png("qrpy.png",scale=8)

d = decode(Image.open("qrpy.png"))
print(d[0].data.decode("ascii"))