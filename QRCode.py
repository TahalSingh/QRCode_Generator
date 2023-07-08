import qrcode
qr=qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
Data="Name: Tahal Singh Charti Magar\nProfession: Student\nAddress: Pyuthan "
qr.add_data(Data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save("1.png")
print("Your QRcode is Generate")

