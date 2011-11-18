import cv
import svm
import svmutil
import gabor
import glob
import face
import operator
import os.path

def main():
	
	img_kind = "happy"

	happy_cv_svm_params = "-t 2 -c 2.0 -g 3.0517578125e-05"
	surprise_cv_svm_params = "-t 2 -c 0.03125 -g 0.0078125"
	anger_cv_svm_params = "-t 2 -c 0.03125 -g 0.0078125"
	# example_make_model(img_kind, happy_cv_svm_params)

	# img_kind = "surprise"
	# example_make_model(img_kind, surprise_cv_svm_params)

	# img_kind = "anger"
	# example_make_model(img_kind, anger_cv_svm_params)

	# test_model(img_kind)

	live_test()

	# data_gen(img_kind)
	img_kind = "anger"
	# test_model(img_kind)

def data_gen(img_kind):
	subdir = "data/"
	extension = '.data'
	file_path = subdir + img_kind + extension
	output_file = open(file_path, 'w+')

	the_ones = glob.glob(subdir + "f_" + img_kind + "*.jpg")
	all_of_them = glob.glob(subdir + "f_*_*.jpg")
	the_others = []

	for x in all_of_them:
		if the_ones.count(x) < 1:
			the_others.append(x)
	
	for x in the_ones:
		img_features = get_image_features(cv.LoadImageM(x))
		class_label = 1
		#write label in a new line
		output_file.write(str(class_label))
		#write features one by one and increment the index
		for i in xrange(1,len(img_features)):
			output_file.write(' ' + str(i) + ':' + str(img_features[i-1]))
		#write newline
		output_file.write("\n")
		print x
	
	for x in the_others:
		img_features = get_image_features(cv.LoadImageM(x))
		class_label = -1
		#write label in a new line
		output_file.write(str(class_label))
		#write features one by one and increment the index
		for i in xrange(1,len(img_features)):
			output_file.write(' ' + str(i) + ':' + str(img_features[i-1]))
		#write newline
		output_file.write("\n")
		print x
	
	output_file.close()

def live_test():
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

				results = {'happy': happy_label[0][0], 'surprise': surprise_label[0][0], 'anger': anger_label[0][0]}
				sorted_results = sorted(results.iteritems(), key=operator.itemgetter(1))
				print sorted_results[len(sorted_results)-1][0]

				print "---------------------"

def test_model(img_kind):
	model = svmutil.svm_load_model(img_kind + '.model')
	print "Finished Loading Model"

	total_count = 0
	correct_count = 0
	wrong_count = 0

	subdir = "data/"
	the_ones = glob.glob(subdir + "f_" + img_kind + "*.jpg")
	all_of_them = glob.glob(subdir + "f_*_*.jpg")
	the_others = []

	for x in all_of_them:
		total_count += 1
		if the_ones.count(x) < 1:
			the_others.append(x)
	
	for x in the_ones:
		img = cv.LoadImageM(x)
		cv.ShowImage("img", img)
		cv.WaitKey(10)
		img_features = get_image_features(img)
		predict_input_data = []
		predict_input_data.append(img_features)
		(val, val_2, val_3) = svmutil.svm_predict([1], predict_input_data, model)
		if int(val[0]) == 1:
			print 'correct'
			correct_count += 1
		else:
			wrong_count += 1

	for x in the_others:
		img = cv.LoadImageM(x)
		cv.ShowImage("img", img)
		cv.WaitKey(10)
		img_features = get_image_features(img)
		predict_input_data = []
		predict_input_data.append(img_features)
		(val, val_2, val_3) = svmutil.svm_predict([1], predict_input_data, model)
		if int(val[0]) == -1:
			correct_count += 1
		else:
			wrong_count += 1
	
	print "Total Pictures: " + str(total_count)
	print "Correct: " + str(correct_count)
	print "Wrong: " + str(wrong_count)
	print "Accuracy: " + str(correct_count/float(total_count) * 100) + '%'

# img_kind = "happy"
# svm_params = "-t 0 -c 10"
def example_make_model(img_kind, svm_params):
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

# gets an opencv image
# computes all of its gabor filters and returns them in a list
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