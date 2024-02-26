from stegano import lsb
decrypt = lsb.reveal("encrypt.png")
print(decrypt)
