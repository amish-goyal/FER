import cv

face_cascade = "haarcascades/haarcascade_frontalface_alt.xml"

def main():
	hc = cv.Load(face_cascade)
	cv.NamedWindow("camera", 1)
	capture = cv.CaptureFromCAM(0)

	while True:
		img = cv.QueryFrame(capture)

		returned = handel_camera_image(img, hc)

		if returned == None:
			pass
		else:
			(img_f, img_r) = returned

			cv.ShowImage("camera", img_f)
			cv.ShowImage("normalized", img_r)

		key_pressed = cv.WaitKey(1)
		# print "key pressed: " + str(key_pressed)

		if (key_pressed == 27):
			break

	cv.DestroyWindow("camera")
	cv.DestroyWindow("normalized")
	

#return the 64 to 64 image
def resize_crop_img(img,x,y,w,h):
	dest_size = 128

	img_o = cv.GetSubRect(img, (x,y,w,h))
	img_r = cv.CreateImage((dest_size, dest_size), 8, 1)
	cv.Resize(img_o, img_r)
	return img_r

# img is the image from the camera
# hc is the haar cascade xml loaded into memory it is used to detect faces

# returns a tuple (img_f, img_face) (or None if more than or less than one face is detected in the image)
# 	img_f is the resized, grayscaled input image with a rectangle around the face
# 	img_face is the normalized image of the face which is the output of resize_crop_img function
def handel_camera_image(img, hc):
	#resize it
	img2 = cv.CreateMat(cv.GetSize(img)[1] / 2, cv.GetSize(img)[0] / 2, cv.CV_8UC3)
	cv.Resize(img, img2)

	#convert to grayscale
	img_gray = cv.CreateImage(cv.GetSize(img2), 8, 1)
	cv.CvtColor(img2, img_gray, cv.CV_RGB2GRAY)

	#set the final image
	img_f = img_gray

	#detect faces from it
	objects = cv.HaarDetectObjects(img_f, hc, cv.CreateMemStorage())
	number_of_faces = len(objects)

	if number_of_faces != 1:
		print "Error! Number of detected faces: " + str(number_of_faces)
		return None
	else:
		for (x, y, w, h), n in objects:
			#annotate the image
			cv.Rectangle(img_f, (x,y), (x+w, y+h), 255)
			print "FACE -> h: " + str(h) + ", w: " + str(w) + ", r(w/h): " + str(float(w)/float(h))
			
			#resize to 64 to 64
			img_r = resize_crop_img(img_f, x,y,w,h)
			return (img_f, img_r)


if __name__ == '__main__':
	main()