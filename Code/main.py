import cv
import svm
import svmutil
import gabor
import glob
import face

def main():
	
	img_kind = "surprise"
	# svm_params = "-t 0 -c 10"
	# expample_make_model(img_kind, svm_params)

	# test_model(img_kind)

	new_test()

def new_test():
	# load all the models
	print "Loading Models"
	happy_model = svmutil.svm_load_model('happy.model')
	print 1
	surprise_model = svmutil.svm_load_model('surprise.model')
	print 2
	anger_model = svmutil.svm_load_model('anger.model')
	print 3
	print "---------------------"

	print "Loading cascade"
	face_cascade = "haarcascades/haarcascade_frontalface_alt.xml"
	hc = cv.Load(face_cascade)
	print "---------------------"

	capture = cv.CaptureFromCAM(0)
	while True:
		img = cv.QueryFrame(capture)
		cv.ShowImage("camera",img)
		key_pressed = cv.WaitKey(50)
		if key_pressed == 27:
			break
		elif key_pressed == 32:
			print '~> KEY PRESSED <~'
			# do face detection
			print 'detecting face'
			returned = face.handel_camera_image(img, hc)
			if returned == None:
				print "No face || more than one face"
				pass
			else:
				(img_o, img_face) = returned
				cv.ShowImage("face",img_face)
				# get features from the face
				test_data = get_image_features(img_face)
				predict_input_data = []
				predict_input_data.append(test_data)

				# do svm query for all models
				(val, val_2, happy_label) = svmutil.svm_predict([1] ,predict_input_data, happy_model)
				(val, val_2, surprise_label) = svmutil.svm_predict([1] ,predict_input_data, surprise_model)
				(val, val_2, anger_label) = svmutil.svm_predict([1] ,predict_input_data, anger_model)

				happy_val = happy_label[0][0]
				surprise_val = surprise_label[0][0]
				anger_val = anger_label[0][0]

				if happy_val >= surprise_val and happy_val >= anger_val:
					print "happy: "
				if surprise_val >= happy_val and surprise_val >= anger_val:
					print "surprise: "
				if anger_val >= surprise_val and anger_val >= happy_val:
					print "anger: "

			print "---------------------"

def test_model(img_kind):
	model = svmutil.svm_load_model(img_kind + '.model')
	print "Finished Loading Model"

	face_cascade = "haarcascades/haarcascade_frontalface_alt.xml"
	hc = cv.Load(face_cascade)
	capture = cv.CaptureFromCAM(0)

	while True:
		img = cv.QueryFrame(capture)

		returned = face.handel_camera_image(img, hc)

		if returned == None:
			print "No face || more than one face"
			pass
		else:
			print "We have a face"
			(img_o, img_face) = returned

			# img_face = cv.LoadImageM('data/f_surprise_3.jpg');

			test_data = get_image_features(img_face)
			
			predict_input_data = []
			predict_input_data.append(test_data)

			print "Finished getting image features"

			label = svmutil.svm_predict([1] ,predict_input_data, model)

			print "Finished predicting"

			cv.ShowImage("img",img_face)
			print label
			if cv.WaitKey(50) == 27:

				break
	
	cv.DestroyAllWindows()



# img_kind = "happy"
# svm_params = "-t 0 -c 10"
def expample_make_model(img_kind, svm_params):
	problem = build_problem(img_kind)
	print "Prob built"

	param = svm.svm_parameter(svm_params)
	print "Params Set"

	problem_model = svmutil.svm_train(problem, param)
	print "Model built"

	svmutil.svm_save_model(img_kind + '.model', problem_model)
	print "Done"

# gets an opencv image
# returns all elements of that image as a list
def get_features(img):
	features = [] # The list of features

	for x in xrange(0,img.height):
		for y in xrange(0,img.width):
			features.append(img[x,y])
	
	return features

def get_image_features(img):
	features = []

	kernel_var = 50
	gabor_psi = 90

	gabor_pulsation = 2
	gabor_phase = 0
	(t_img_mag, t_img) = gabor.Process(img, kernel_var, gabor_pulsation, gabor_phase, gabor_psi)
	features.extend(get_features(t_img_mag))

	gabor_pulsation = 10
	gabor_phase = 0
	(t_img_mag, t_img) = gabor.Process(img, kernel_var, gabor_pulsation, gabor_phase, gabor_psi)
	features.extend(get_features(t_img_mag))
	
	gabor_pulsation = 2
	gabor_phase = 100
	(t_img_mag, t_img) = gabor.Process(img, kernel_var, gabor_pulsation, gabor_phase, gabor_psi)
	features.extend(get_features(t_img_mag))

	gabor_pulsation = 10
	gabor_phase = 100
	(t_img_mag, t_img) = gabor.Process(img, kernel_var, gabor_pulsation, gabor_phase, gabor_psi)
	features.extend(get_features(t_img_mag))

	return features

def build_problem(img_kind):
	subdir = "data/"
	# img_kind = "happy"

	classes = []
	data = []

	the_ones = glob.glob(subdir + "f_" + img_kind + "*.jpg")
	all_of_them = glob.glob(subdir + "f_*_*.jpg")
	the_others = []

	for x in all_of_them:
		if the_ones.count(x) < 1:
			the_others.append(x)
	
	for x in the_ones:
		classes.append(1)
		data.append(get_image_features(cv.LoadImageM(x)))
	
	for x in the_others:
		classes.append(-1)
		data.append(get_image_features(cv.LoadImageM(x)))

	prob = svm.svm_problem(classes, data)

	return prob

if __name__ == '__main__':
	main()