import os
import qrcode
img = qrcode.make("https://youtu.be/OrnwnrIM0r0")
img.save("qr.png","PNG")
