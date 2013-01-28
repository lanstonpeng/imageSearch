from PIL import Image
im = Image.open("../asset/i2.jpg")

#resize number 
size = 8,8
#resize the image
im = im.resize(size,Image.ANTIALIAS)
#covert it into a grey image
im = im.convert("L")
average = reduce( lambda x , y : x + y,im.getdata()) / (size[0]*size[1])

#covert it to bitnary thumbnail image
temp = map(lambda x : 1 if x > average else  0 ,im.getdata()) 
#print list(enumerate(temp))
hash1 = reduce(lambda x ,(y,z): x | (z << y),
        enumerate(temp),
        0 
        )
hash2 = reduce(lambda x , y : x << 1 | y,temp,0)
print hash1 , hash2
