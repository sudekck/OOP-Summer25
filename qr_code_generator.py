import qrcode
url = "https://warsaw-engineer-sude-project.lovable.app/"
qr = qrcode.make(url)
qr.save("sude_qr.png")