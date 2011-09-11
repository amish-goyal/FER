#Papers I've read:

##Automatic facial expression analysis: a survey

* B. Fasel, Juergen Luettin
* Cited by 664
* Pattern Recognition, 2003
* Elsevier
* [http://www.sciencedirect.com/science/article/pii/S0031320302000523](link)

###Abstract
Over the last decade, automatic facial expression analysis has become an active research area that finds potential applications in areas such as more engaging human–computer interfaces, talking heads, image retrieval and human emotion analysis. Facial expressions reflect not only emotions, but other mental activities, social interaction and physiological signals. In this survey, we introduce the most prominent automatic facial expression analysis methods and systems presented in the literature. Facial motion and deformation extraction approaches as well as classification methods are discussed with respect to issues such as face normalization, facial expression dynamics and facial expression intensity, but also with regard to their robustness towards environmental changes.

##Coding, analysis, interpretation, and recognition of facial expressions

* Essa I.A., Pentland A.P.
* Cited by 630
* Analysis and Machine Intelligence, 1997
* ieee
* [http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=598232&tag=1](link)

###Abstract
We describe a computer vision system for observing facial motion by using an optimal estimation optical flow method coupled with geometric, physical and motion-based dynamic models describing the facial structure. Our method produces a reliable parametric representation of the face's independent muscle action groups, as well as an accurate estimate of facial motion. Previous efforts at analysis of facial expression have been based on the facial action coding system (FACS), a representation developed in order to allow human psychologists to code expression from static pictures. To avoid use of this heuristic coding scheme, we have used our computer vision system to probabilistically characterize facial motion and muscle activation in an experimental population, thus deriving a new, more accurate, representation of human facial expressions that we call FACS+. Finally, we show how this method can be used for coding, analysis, interpretation, and recognition of facial expressions

##Comprehensive database for facial expression analysis

* Kanade, T.;   Cohn, J.F.;   Yingli Tian;   
* Cited by 876
* Automatic Face and Gesture Recognition, 2000
* ieee
* [http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=840611](link)

###Abstract
Within the past decade, significant effort has occurred in developing methods of facial expression analysis. Because most investigators have used relatively limited data sets, the generalizability of these various methods remains unknown. We describe the problem space for facial expression analysis, which includes level of description, transitions among expressions, eliciting conditions, reliability and validity of training and test data, individual differences in subjects, head orientation and scene complexity image characteristics, and relation to non-verbal behavior. We then present the CMU-Pittsburgh AU-Coded Face Expression Image Database, which currently includes 2105 digitized image sequences from 182 adult subjects of varying ethnicity, performing multiple tokens of most primary FACS action units. This database is the most comprehensive testbed to date for comparative studies of facial expression analysis

##Facial expression recognition using a dynamic model and motion energy

* I.A. Essa, A.P. Pentland
* Cited by 233
* Computer Vision, 1995. Proceedings., Fifth International Conference on
* ieee
* [http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=466916](link)

###Abstract
Previous efforts at facial expression recognition have been based on the Facial Action Coding System (FACS), a representation developed in order to allow human psychologists to code expression from static facial "mugshots." We develop new more accurate representations for facial expression by building a video database of facial expressions and then probabilistically characterizing the facial muscle activation associated with each expression using a detailed physical model of the skin and muscles. This produces a muscle based representation of facial motion, which is then used to recognize facial expressions in two different ways. The first method uses the physics based model directly, by recognizing expressions through comparison of estimated muscle activations. The second method uses the physics based model to generate spatio temporal motion energy templates of the whole face for each different expression. These simple, biologically plausible motion energy "templates" are then used for recognition. Both methods show substantially greater accuracy at expression recognition than has been previously achieved.

##Real Time Face Detection and Facial Expression Recognition: Development and Applications to Human Computer Interaction

* Marian Stewart Bartlett, Gwen Littlewort, Ian Fasel, Javier R. Movellan
* Cited by 114
* Computer Vision and Pattern Recognition Workshop, 2003. CVPRW '03. Conference on
* ieee
* [http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=4624313](link)

###abstract
Computer animated agents and robots bring a social dimension to human computer interaction and force us to think in new ways about how computers could be used in daily life. Face to face communication is a real-time process operating at a a time scale in the order of 40 milliseconds. The level of uncertainty at this time scale is considerable, making it necessary for humans and machines to rely on sensory rich perceptual primitives rather than slow symbolic inference processes. In this paper we present progress on one such perceptual primitive. The system automatically detects frontal faces in the video stream and codes them with respect to 7 dimensions in real time: neutral, anger, disgust, fear, joy, sadness, surprise. The face finder employs a cascade of feature detectors trained with boosting techniques [15, 2]. The expression recognizer receives image patches located by the face detector. A Gabor representation of the patch is formed and then processed by a bank of SVM classifiers. A novel combination of Adaboost and SVM's enhances performance. The system was tested on the Cohn-Kanade dataset of posed facial expressions [6]. The generalization performance to new subjects for a 7- way forced choice correct. Most interestingly the outputs of the classifier change smoothly as a function of time, providing a potentially valuable representation to code facial expression dynamics in a fully automatic and unobtrusive manner. The system has been deployed on a wide variety of platforms including Sony's Aibo pet robot, ATR's RoboVie, and CU animator, and is currently being evaluated for applications including automatic reading tutors, assessment of human-robot interaction.

##Recognising facial expressions in video sequences

* José M. Buenaposada, Enrique Muñoz and Luis Baumela
* Cited by 23
* Pattern Analysis & Applications, 2008
* springer
* [http://www.springerlink.com/content/q075h33723m475k1/](link)

###Abstract
We introduce a system that processes a sequence of images of a front-facing human face and recognises a set of facial expressions. We use an efficient appearance-based face tracker to locate the face in the image sequence and estimate the deformation of its non-rigid components. The tracker works in real time. It is robust to strong illumination changes and factors out changes in appearance caused by illumination from changes due to face deformation. We adopt a model-based approach for facial expression recognition. In our model, an image of a face is represented by a point in a deformation space. The variability of the classes of images associated with facial expressions is represented by a set of samples which model a low-dimensional manifold in the space of deformations. We introduce a probabilistic procedure based on a nearest-neighbour approach to combine the information provided by the incoming image sequence with the prior information stored in the expression manifold to compute a posterior probability associated with a facial expression. In the experiments conducted we show that this system is able to work in an unconstrained environment with strong changes in illumination and face location. It achieves an 89% recognition rate in a set of 333 sequences from the Cohn–Kanade database.

##Recognizing action units for facial expression analysis

* Tian, Y.-I.;   Kanade, T.;   Cohn, J.F.;
* Cited by 665
* Pattern Analysis and Machine Intelligence, IEEE Transactions on , 2001
* ieee
* [http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=908962](link)

###Abstract
Most automatic expression analysis systems attempt to recognize a small set of prototypic expressions, such as happiness, anger, surprise, and fear. Such prototypic expressions, however, occur rather infrequently. Human emotions and intentions are more often communicated by changes in one or a few discrete facial features. In this paper, we develop an automatic face analysis (AFA) system to analyze facial expressions based on both permanent facial features (brows, eyes, mouth) and transient facial features (deepening of facial furrows) in a nearly frontal-view face image sequence. The AFA system recognizes fine-grained changes in facial expression into action units (AU) of the Facial Action Coding System (FACS), instead of a few prototypic expressions. Multistate face and facial component models are proposed for tracking and modeling the various facial features, including lips, eyes, brows, cheeks, and furrows. During tracking, detailed parametric descriptions of the facial features are extracted. With these parameters as the inputs, a group of action units (neutral expression, six upper face AU and 10 lower face AU) are recognized whether they occur alone or in combinations. The system has achieved average recognition rates of 96.4 percent (95.4 percent if neutral expressions are excluded) for upper face AU and 96.7 percent (95.6 percent with neutral expressions excluded) for lower face AU. The generalizability of the system has been tested by using independent image databases collected and FACS-coded for ground-truth by different research teams

##Recognizing facial expression: machine learning and application to spontaneous behavior

* Bartlett, M.S.;   Littlewort, G.;   Frank, M.;   Lainscsek, C.;   Fasel, I.;   Movellan, J.;   
* Cited by 141
* Computer Vision and Pattern Recognition, 2005. CVPR 2005. IEEE Computer Society Conference on 
* ieee
* [http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=1467492](link)

###Abstract
We present a systematic comparison of machine learning methods applied to the problem of fully automatic recognition of facial expressions. We report results on a series of experiments comparing recognition engines, including AdaBoost, support vector machines, linear discriminant analysis. We also explored feature selection techniques, including the use of AdaBoost for feature selection prior to classification by SVM or LDA. Best results were obtained by selecting a subset of Gabor filters using AdaBoost followed by classification with support vector machines. The system operates in real-time, and obtained 93% correct generalization to novel subjects for a 7-way forced choice on the Cohn-Kanade expression dataset. The outputs of the classifiers change smoothly as a function of time and thus can be used to measure facial expression dynamics. We applied the system to to fully automated recognition of facial actions (FACS). The present system classifies 17 action units, whether they occur singly or in combination with other actions, with a mean accuracy of 94.8%. We present preliminary results for applying this system to spontaneous facial expressions.

##Recognizing facial expressions in image sequences using local parameterized models of image motion

* Michael J. Black and Yaser Yacoob
* Cited by 373
* International Journal of Computer Vision, Volume 25, 1997
* springer
* [http://www.springerlink.com/content/u001314h33161447/](link)

###Abstract
This paper explores the use of local parametrized models of image motion for recovering and recognizing the non-rigid and articulated motion of human faces. Parametric flow models (for example affine) are popular for estimating motion in rigid scenes. We observe that within local regions in space and time, such models not only accurately model non-rigid facial motions but also provide a concise description of the motion in terms of a small number of parameters. These parameters are intuitively related to the motion of facial features during facial expressions and we show how expressions such as anger, happiness, surprise, fear, disgust, and sadness can be recognized from the local parametric motions in the presence of significant head motion. The motion tracking and expression recognition approach performed with high accuracy in extensive laboratory experiments involving 40 subjects as well as in television and movie sequences.

##Recognizing human facial expressions from long image sequences using optical flow

* Yacoob, Y.;   Davis, L.S.;   
* Cited by 301
* Pattern Analysis and Machine Intelligence, IEEE Transactions on, Volume 18, 1996
* ieee
* [http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=506414](link)

###Abstract
An approach to the analysis and representation of facial dynamics for recognition of facial expressions from image sequences is presented. The algorithms utilize optical flow computation to identify the direction of rigid and nonrigid motions that are caused by human facial expressions. A mid-level symbolic representation motivated by psychological considerations is developed. Recognition of six facial expressions, as well as eye blinking, is demonstrated on a large set of image sequences