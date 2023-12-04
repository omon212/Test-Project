import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=5,
)
qr.add_data('https://www.instagram.com/rmkvlly/')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
type(img)

img.save(f"test.png")