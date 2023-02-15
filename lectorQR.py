import qrcode
import qrcode.image.svg

QR=input("write what you want to make a qr: ")
qr=qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=20,  border=2)
qr.add_data(QR)
qr.make(fit=True)
img=qr.make_image(fill_color="black", black_color="white")
img.save("QR.png")