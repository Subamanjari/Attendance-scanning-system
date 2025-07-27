import qrcode

def generate_qr(user_id):
    img = qrcode.make(user_id)
    img.save(f"{user_id}_qr.png")
    print(f"QR code saved as {user_id}_qr.png")

generate_qr("suba")
generate_qr("swey")
generate_qr("vino")

