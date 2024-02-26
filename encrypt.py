from stegano import lsb
inp_img =input("enter image path or your image :")
message = input("enter your message to hide : ")
secreat_msg = lsb.hide(inp_img, message)
secreat_msg.save("encrypt.png")
