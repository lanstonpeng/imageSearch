import Image, cv
import os, sys
import numpy

def PIL2array(img):
	return numpy.array(img.getdata(),numpy.uint8).reshape(img.size[1],img.size[0], 1)

def array2PIL(arr, size):
	#mode = 'RGBA'
	mode = 'L'
	arr = arr.reshape(arr.shape[0]*arr.shape[1], arr.shape[2])
	if len(arr[0]) == 3:
		arr = numpy.c_[arr, 255*numpy.ones((len(arr),1), numpy.uint8)]
	return Image.frombuffer(mode, size, arr.tostring(), 'raw', mode, 0, 1)

def main():
	img = Image.open("p.jpg")
	img = img.resize((32,32))
	img = img.convert("L")
	arr = PIL2array(img)
	#print arr
	src = cv.CreateMat(32, 32, cv.CV_32FC1)
	dst = cv.CreateMat(32, 32, cv.CV_32FC1)
	cv.DCT(src, dst, cv.CV_DXT_FORWARD)
	imgarray = numpy.asarray(dst)
	#img2 = array2PIL(imgarray, img.size)
	#img2 = array2PIL(arr, img.size)
	img2 = Image.fromarray(numpy.uint8(imgarray))
	img2.save('out.jpg')

if __name__ == '__main__':
	main()
