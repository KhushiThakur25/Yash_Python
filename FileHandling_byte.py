file = open('dora_img.jpg','rb')
data = file.read()
print(data)
file.close()


file = open('dora_img1.jpg','wb')
file.write(data)
file.close()
