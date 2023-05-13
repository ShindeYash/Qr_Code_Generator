import qrcode
import image
qr = qrcode.QRCode(
    version = 15, # 15 means the version of the qr code high the number bigger the code image and complicated picture
    box_size = 10, # Size of the box where qr code will be displayed.
    border = 5 # It is the white part of image -- border is all 4 sides with white color
)

data = "https://github.com/ShindeYash"
# I have given the path of my Github Profile.

qr.add_data(data)
qr.make(fit = True)

img = qr.make_image()
img.save("test.png")