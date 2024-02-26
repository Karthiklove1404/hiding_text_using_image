from stegano import lsb
inp_img =input("enter image path or your image :")
message = input("enter your message to hide : ")
secreat_msg = lsb.hide(inp_img, message)
print("file save in .png")
save_img = input("enter name : ")
secreat_msg.save(save_img)
