#List of Papers for this project:

##Automatic facial expression analysis: a survey

* B. Fasel, Juergen Luettin
* Cited by 664
* Pattern Recognition, 2003
* Elsevier
* [http://www.sciencedirect.com/science/article/pii/S0031320302000523](link)

####Abstract
Over the last decade, automatic facial expression analysis has become an active research area that finds potential applications in areas such as more engaging human–computer interfaces, talking heads, image retrieval and human emotion analysis. Facial expressions reflect not only emotions, but other mental activities, social interaction and physiological signals. In this survey, we introduce the most prominent automatic facial expression analysis methods and systems presented in the literature. Facial motion and deformation extraction approaches as well as classification methods are discussed with respect to issues such as face normalization, facial expression dynamics and facial expression intensity, but also with regard to their robustness towards environmental changes.

##Coding, analysis, interpretation, and recognition of facial expressions

* Essa I.A., Pentland A.P.
* Cited by 630
* Analysis and Machine Intelligence, 1997
* ieee
* [http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=598232&tag=1](link)

####Abstract
We describe a computer vision system for observing facial motion by using an optimal estimation optical flow method coupled with geometric, physical and motion-based dynamic models describing the facial structure. Our method produces a reliable parametric representation of the face's independent muscle action groups, as well as an accurate estimate of facial motion. Previous efforts at analysis of facial expression have been based on the facial action coding system (FACS), a representation developed in order to allow human psychologists to code expression from static pictures. To avoid use of this heuristic coding scheme, we have used our computer vision system to probabilistically characterize facial motion and muscle activation in an experimental population, thus deriving a new, more accurate, representation of human facial expressions that we call FACS+. Finally, we show how this method can be used for coding, analysis, interpretation, and recognition of facial expressions

##Comprehensive database for facial expression analysis

* Kanade, T.;   Cohn, J.F.;   Yingli Tian;   
* Cited by 876
* Automatic Face and Gesture Recognition, 2000
* ieee
* [http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=840611](link)

####Abstract
Within the past decade, significant effort has occurred in developing methods of facial expression analysis. Because most investigators have used relatively limited data sets, the generalizability of these various methods remains unknown. We describe the problem space for facial expression analysis, which includes level of description, transitions among expressions, eliciting conditions, reliability and validity of training and test data, individual differences in subjects, head orientation and scene complexity image characteristics, and relation to non-verbal behavior. We then present the CMU-Pittsburgh AU-Coded Face Expression Image Database, which currently includes 2105 digitized image sequences from 182 adult subjects of varying ethnicity, performing multiple tokens of most primary FACS action units. This database is the most comprehensive testbed to date for comparative studies of facial expression analysis

##Facial expression recognition using a dynamic model and motion energy

* I.A. Essa, A.P. Pentland
* Cited by 233
* Computer Vision, 1995. Proceedings., Fifth International Conference on
* ieee
* [http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=466916](link)

####Abstract
Previous efforts at facial expression recognition have been based on the Facial Action Coding System (FACS), a representation developed in order to allow human psychologists to code expression from static facial "mugshots." We develop new more accurate representations for facial expression by building a video database of facial expressions and then probabilistically characterizing the facial muscle activation associated with each expression using a detailed physical model of the skin and muscles. This produces a muscle based representation of facial motion, which is then used to recognize facial expressions in two different ways. The first method uses the physics based model directly, by recognizing expressions through comparison of estimated muscle activations. The second method uses the physics based model to generate spatio temporal motion energy templates of the whole face for each different expression. These simple, biologically plausible motion energy "templates" are then used for recognition. Both methods show substantially greater accuracy at expression recognition than has been previously achieved.

##Real Time Face Detection and Facial Expression Recognition: Development and Applications to Human Computer Interaction

* Marian Stewart Bartlett, Gwen Littlewort, Ian Fasel, Javier R. Movellan
* Cited by 114
* Computer Vision and Pattern Recognition Workshop, 2003. CVPRW '03. Conference on
* ieee
* [http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=4624313](link)

####Abstract
Computer animated agents and robots bring a social dimension to human computer interaction and force us to think in new ways about how computers could be used in daily life. Face to face communication is a real-time process operating at a a time scale in the order of 40 milliseconds. The level of uncertainty at this time scale is considerable, making it necessary for humans and machines to rely on sensory rich perceptual primitives rather than slow symbolic inference processes. In this paper we present progress on one such perceptual primitive. The system automatically detects frontal faces in the video stream and codes them with respect to 7 dimensions in real time: neutral, anger, disgust, fear, joy, sadness, surprise. The face finder employs a cascade of feature detectors trained with boosting techniques [15, 2]. The expression recognizer receives image patches located by the face detector. A Gabor representation of the patch is formed and then processed by a bank of SVM classifiers. A novel combination of Adaboost and SVM's enhances performance. The system was tested on the Cohn-Kanade dataset of posed facial expressions [6]. The generalization performance to new subjects for a 7- way forced choice correct. Most interestingly the outputs of the classifier change smoothly as a function of time, providing a potentially valuable representation to code facial expression dynamics in a fully automatic and unobtrusive manner. The system has been deployed on a wide variety of platforms including Sony's Aibo pet robot, ATR's RoboVie, and CU animator, and is currently being evaluated for applications including automatic reading tutors, assessment of human-robot interaction.

##Recognising facial expressions in video sequences

* José M. Buenaposada, Enrique Muñoz and Luis Baumela
* Cited by 23
* Pattern Analysis & Applications, 2008
* springer
* [http://www.springerlink.com/content/q075h33723m475k1/](link)

####Abstract
We introduce a system that processes a sequence of images of a front-facing human face and recognises a set of facial expressions. We use an efficient appearance-based face tracker to locate the face in the image sequence and estimate the deformation of its non-rigid components. The tracker works in real time. It is robust to strong illumination changes and factors out changes in appearance caused by illumination from changes due to face deformation. We adopt a model-based approach for facial expression recognition. In our model, an image of a face is represented by a point in a deformation space. The variability of the classes of images associated with facial expressions is represented by a set of samples which model a low-dimensional manifold in the space of deformations. We introduce a probabilistic procedure based on a nearest-neighbour approach to combine the information provided by the incoming image sequence with the prior information stored in the expression manifold to compute a posterior probability associated with a facial expression. In the experiments conducted we show that this system is able to work in an unconstrained environment with strong changes in illumination and face location. It achieves an 89% recognition rate in a set of 333 sequences from the Cohn–Kanade database.

##Recognizing action units for facial expression analysis

* Tian, Y.-I.;   Kanade, T.;   Cohn, J.F.;
* Cited by 665
* Pattern Analysis and Machine Intelligence, IEEE Transactions on , 2001
* ieee
* [http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=908962](link)

####Abstract
Most automatic expression analysis systems attempt to recognize a small set of prototypic expressions, such as happiness, anger, surprise, and fear. Such prototypic expressions, however, occur rather infrequently. Human emotions and intentions are more often communicated by changes in one or a few discrete facial features. In this paper, we develop an automatic face analysis (AFA) system to analyze facial expressions based on both permanent facial features (brows, eyes, mouth) and transient facial features (deepening of facial furrows) in a nearly frontal-view face image sequence. The AFA system recognizes fine-grained changes in facial expression into action units (AU) of the Facial Action Coding System (FACS), instead of a few prototypic expressions. Multistate face and facial component models are proposed for tracking and modeling the various facial features, including lips, eyes, brows, cheeks, and furrows. During tracking, detailed parametric descriptions of the facial features are extracted. With these parameters as the inputs, a group of action units (neutral expression, six upper face AU and 10 lower face AU) are recognized whether they occur alone or in combinations. The system has achieved average recognition rates of 96.4 percent (95.4 percent if neutral expressions are excluded) for upper face AU and 96.7 percent (95.6 percent with neutral expressions excluded) for lower face AU. The generalizability of the system has been tested by using independent image databases collected and FACS-coded for ground-truth by different research teams

##Recognizing facial expression: machine learning and application to spontaneous behavior

* Bartlett, M.S.;   Littlewort, G.;   Frank, M.;   Lainscsek, C.;   Fasel, I.;   Movellan, J.;   
* Cited by 141
* Computer Vision and Pattern Recognition, 2005. CVPR 2005. IEEE Computer Society Conference on 
* ieee
* [http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=1467492](link)

####Abstract
We present a systematic comparison of machine learning methods applied to the problem of fully automatic recognition of facial expressions. We report results on a series of experiments comparing recognition engines, including AdaBoost, support vector machines, linear discriminant analysis. We also explored feature selection techniques, including the use of AdaBoost for feature selection prior to classification by SVM or LDA. Best results were obtained by selecting a subset of Gabor filters using AdaBoost followed by classification with support vector machines. The system operates in real-time, and obtained 93% correct generalization to novel subjects for a 7-way forced choice on the Cohn-Kanade expression dataset. The outputs of the classifiers change smoothly as a function of time and thus can be used to measure facial expression dynamics. We applied the system to to fully automated recognition of facial actions (FACS). The present system classifies 17 action units, whether they occur singly or in combination with other actions, with a mean accuracy of 94.8%. We present preliminary results for applying this system to spontaneous facial expressions.

##Recognizing facial expressions in image sequences using local parameterized models of image motion

* Michael J. Black and Yaser Yacoob
* Cited by 373
* International Journal of Computer Vision, Volume 25, 1997
* springer
* [http://www.springerlink.com/content/u001314h33161447/](link)

####Abstract
This paper explores the use of local parametrized models of image motion for recovering and recognizing the non-rigid and articulated motion of human faces. Parametric flow models (for example affine) are popular for estimating motion in rigid scenes. We observe that within local regions in space and time, such models not only accurately model non-rigid facial motions but also provide a concise description of the motion in terms of a small number of parameters. These parameters are intuitively related to the motion of facial features during facial expressions and we show how expressions such as anger, happiness, surprise, fear, disgust, and sadness can be recognized from the local parametric motions in the presence of significant head motion. The motion tracking and expression recognition approach performed with high accuracy in extensive laboratory experiments involving 40 subjects as well as in television and movie sequences.

##Recognizing human facial expressions from long image sequences using optical flow

* Yacoob, Y.;   Davis, L.S.;   
* Cited by 301
* Pattern Analysis and Machine Intelligence, IEEE Transactions on, Volume 18, 1996
* ieee
* [http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=506414](link)

####Abstract
An approach to the analysis and representation of facial dynamics for recognition of facial expressions from image sequences is presented. The algorithms utilize optical flow computation to identify the direction of rigid and nonrigid motions that are caused by human facial expressions. A mid-level symbolic representation motivated by psychological considerations is developed. Recognition of six facial expressions, as well as eye blinking, is demonstrated on a large set of image sequences

##Dynamics of facial expression extracted automatically from video

* Gwen Littlewort, Marian Stewart Bartlett, Ian Fasel, Joshua Susskind, Javier Movellan
* Cited by 165
* Image and Vision Computing, Volume 24, Issue 6, 1 June 2006, Pages 615-625, Face Processing in Video Sequences
* Elsevier
* [http://www.sciencedirect.com/science/article/pii/S0262885605001654](link)

####Abstract
We present a systematic comparison of machine learning methods applied to the problem of fully automatic recognition of facial expressions, including AdaBoost, support vector machines, and linear discriminant analysis. Each video-frame is first scanned in real-time to detect approximately upright-frontal faces. The faces found are scaled into image patches of equal size, convolved with a bank of Gabor energy filters, and then passed to a recognition engine that codes facial expressions into 7 dimensions in real time: neutral, anger, disgust, fear, joy, sadness, surprise. We report results on a series of experiments comparing spatial frequency ranges, feature selection techniques, and recognition engines. Best results were obtained by selecting a subset of Gabor filters using AdaBoost and then training Support Vector Machines on the outputs of the filters selected by AdaBoost. The generalization performance to new subjects for a 7-way forced choice was 93% or more correct on two publicly available datasets, the best performance reported so far on these datasets. The outputs of the classifier change smoothly as a function of time and thus can be used for unobtrusive expression dynamics capture. We developed an end-to-end system that provides facial expression codes at 24 frames per second and animates a computer-generated character. In real-time this expression mirror operates down to resolutions of 16 pixels from eye to eye. We also applied the system to fully automated facial action coding.

##Face Detection in Color Images

* Rein-Lien Hsu;   Abdel-Mottaleb, M.;   Jain, A.K
* Cited by 1119
* Pattern Analysis and Machine Intelligence, IEEE Transactions on, May 2002
* ieee
* [http://ieeexplore.ieee.org/xpl/freeabs_all.jsp?arnumber=1000242](link)

####Abstract
Human face detection plays an important role in applications such as video surveillance, human computer interface, face recognition, and face image database management. We propose a face detection algorithm for color images in the presence of varying lighting conditions as well as complex backgrounds. Based on a novel lighting compensation technique and a nonlinear color transformation, our method detects skin regions over the entire image and then generates face candidates based on the spatial arrangement of these skin patches. The algorithm constructs eye, mouth, and boundary maps for verifying each face candidate. Experimental results demonstrate successful face detection over a wide range of facial variations in color, position, scale, orientation, 3D pose, and expression in images from several photo collections (both indoors and outdoors)

##Facial Expression Recognition A Brief Tutorial Overview

* Claude C. Chibelushi, Fabrice Bourel 
* Cited by 32
* CVonline: On-Line Compendium of Computer …, 2003
* Citeseer
* [http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.104.957&rep=rep1&type=pdf](link)

####Abstract
Facial  expressions  convey  non-verbal  cues,  which play  an  important  role  in  interpersonal  relations.  Automatic recognition of facial expressions can be an important component of  natural  human-machine  interfaces;  it  may  also  be  used  in behavioural  science  and  in  clinical  practice. Although  humans recognise  facial  expressions  virtually  without  effort  or  delay, reliable  expression  recognition  by machine  is  still  a  challenge. This  paper  presents  a  high-level  overview  of  automatic expression  recognition;  it  highlights  the  main  system components and some research challenges. 

##Haar features for facs au recognition

* Whitehill, J.;   Omlin, C.W.;   
* Cited by 32
* Automatic Face and Gesture Recognition, 2006. FGR 2006. 7th International Conference on 
* ieee
* [http://ieeexplore.ieee.org/xpl/freeabs_all.jsp?arnumber=1613004](link)

####Abstract
We examined the effectiveness of using Haar features and the Adaboost boosting algorithm for FACS action unit (AU) recognition. We evaluated both recognition accuracy and processing time of this new approach compared to the state-of-the-art method of classifying Gabor responses with support vector machines. Empirical results on the Cohn-Kanade facial expression database showed that the Haar+Adaboost method yields AU recognition rates comparable to those of the Gabor+SVM method but operates at least two orders of magnitude more quickly
Index Terms

##Machine learning methods for fully automatic recognition of facial expressions and facial actions

* Bartlett, M.S.;   Littlewort, G.;   Lainscsek, C.;   Fasel, I.;   Movellan, J.;   
* Cited by 80
* Systems, Man and Cybernetics, 2004 IEEE International Conference on 
* ieee
* [http://ieeexplore.ieee.org/xpl/freeabs_all.jsp?arnumber=1398364](link)

####Abstract
We present a systematic comparison of machine learning methods applied to the problem of fully automatic recognition of facial expressions. We explored recognition of facial actions from the facial action coding system (FACS), as well as recognition of fall facial expressions. Each video-frame is first scanned in real-time to detect approximately upright frontal faces. The faces found are scaled into image patches of equal size, convolved with a bank of Gabor energy filters, and then passed to a recognition engine that codes facial expressions into 7 dimensions in real time: neutral, anger, disgust, fear, joy, sadness, surprise. We report results on a series of experiments comparing recognition engines, including AdaBoost, support vector machines, linear discriminant analysis, as well as feature selection techniques. Best results were obtained by selecting a subset of Gabor filters using AdaBoost and then training support vector machines on the outputs of the filters selected by AdaBoost. The generalization performance to new subjects for recognition of full facial expressions in a 7-way forced choice was 93% correct, the best performance reported so far on the Cohn-Kanade FACS-coded expression dataset. We also applied the system to fully automated facial action coding. The present system classifies 18 action units, whether they occur singly or in combination with other actions, with a mean agreement rate of 94.5% with human FACS codes in the Cohn-Kanade dataset. The outputs of the classifiers change smoothly as a function of time and thus can be used to measure facial expression dynamics.
Index Terms

##Measuring facial expressions by computer image analysis

* Marian Stewart Bartlett, Joseph C. Hager, Paul Ekman, Terrence J. Sejnowski
* Cited by 223
* Physiological Psychology, Vol 36 Issue 2, Pages 253-263, March 1999
* Wiley Online Library
* [http://onlinelibrary.wiley.com/doi/10.1017/S0048577299971664/abstract](link)

####Abstract
Facial expressions provide an important behavioral measure for the study of emotion, cognitive processes, and social interaction. The Facial Action Coding System (Ekman & Friesen, 1978) is an objective method for quantifying facial movement in terms of component actions. We applied computer image analysis to the problem of automatically detecting facial actions in sequences of images. Three approaches were compared: holistic spatial analysis, explicit measurement of features such as wrinkles, and estimation of motion flow fields. The three methods were combined in a hybrid system that classified six upper facial actions with 91% accuracy. The hybrid system outperformed human nonexperts on this task and performed as well as highly trained experts. An automated system would make facial expression measurement more widely accessible as a research tool in behavioral science and investigations of the neural substrates of emotion.

##Robust Real-Time Face Detection

* Paul Viola and Michael J. Jones
* Cited by 2608
* International Journal of Computer Vision Volume 57, Number 2, 137-154, 2004
* Springer
* [http://www.springerlink.com/content/q70v4h6715v5p152/](link)

####Abstract
This paper describes a face detection framework that is capable of processing images extremely rapidly while achieving high detection rates. There are three key contributions. The first is the introduction of a new image representation called the ldquoIntegral Imagerdquo which allows the features used by our detector to be computed very quickly. The second is a simple and efficient classifier which is built using the AdaBoost learning algorithm (Freund and Schapire, 1995) to select a small number of critical visual features from a very large set of potential features. The third contribution is a method for combining classifiers in a ldquocascaderdquo which allows background regions of the image to be quickly discarded while spending more computation on promising face-like regions. A set of experiments in the domain of face detection is presented. The system yields face detection performance comparable to the best previous systems (Sung and Poggio, 1998; Rowley et al., 1998; Schneiderman and Kanade, 2000; Roth et al., 2000). Implemented on a conventional desktop, face detection proceeds at 15 frames per second.

##Texture features for browsing and retrieval of image data

* Manjunath, B.S.;   Ma, W.Y.;   
* Cited by 2310
* Pattern Analysis and Machine Intelligence, IEEE Transactions on, 1996
* ieee
* [http://ieeexplore.ieee.org/xpl/freeabs_all.jsp?arnumber=531803](link)

####Abstract
Image content based retrieval is emerging as an important research area with application to digital libraries and multimedia databases. The focus of this paper is on the image processing aspects and in particular using texture information for browsing and retrieval of large image data. We propose the use of Gabor wavelet features for texture analysis and provide a comprehensive experimental evaluation. Comparisons with other multiresolution texture features using the Brodatz texture database indicate that the Gabor features provide the best pattern retrieval accuracy. An application to browsing large air photos is illustrated

##Facial Expression Recognition

* Cemre Zor
* Submitted for the Degree of Master of Science in Signal Processing and Machine Intelligence from the University of Surrey, 2008
* University of Surrey
* [http://personal.ee.surrey.ac.uk/Personal/T.Windeatt/msc_projects/MSc_DISSERTATION.pdf](link)

####Abstract
Face expression analysis and recognition has been one of the fast developing areas due to its wide range of application areas such as emotion analysis, biometrics, image retrieval and is one of the subjects on which lots of research has been done through solving the problems occurring in recognition of the face expressions under different illuminations, orientations and numerous other variations. 

Different methods, all aiming to meet different requirements, have been used in solving facial expression analysis problems. These methods consist of pre-processing and processing parts. The detection and extraction of face images from the input data together with the normalization process, which aims to align these extracted images independent of varying environmental conditions such as illumination and orientation, form up the pre-processing part. The processing part on the other hand; aims to extract specific features from the already pre-processed images, and recognize the facial action units/facial expressions depending on these features. Several methods try to find different optimised algorithms mainly for the processing part.

Thus, the project primarily concentrates on the recognition of expressions that are generated on 44 action units on face. The steps of the resulting systems, which aim to recognize the facial expression action units; mainly consist of normalization, feature extraction, feature selection and binary & multi-class classifications of the frontal face images. Experiments are carried out on various system combinations; and comparisons have been made. In the binary classification case, in which the facial expressions are recognized in “1 vs. all” manner, the results are found to be quite satisfactory in terms of accuracy. In multi-class classification case, the combinations of different expressions occurring at the same time are treated as separate classes and different methods such as Error Correcting Output Codes have been applied. Although for a large number of classes, the results are not as accurate as the ones of the binary case; the recognition speed obtained is quite pleasing. When certain conditions such as having large numbers of training samples and small number of classes are fulfilled, the results also turn out to be a lot better in terms of accuracy as well as speed. 