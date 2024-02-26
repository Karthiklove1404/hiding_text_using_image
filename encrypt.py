from stegano import lsb
secreat_msg = lsb.hide("eagle01.webp", "hello")
secreat_msg.save("encrypt.png")
