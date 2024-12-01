**Project overview**

This repository contains every program used for my research project, "Blink detection using Adaptive Eye Aspect Ratio." The project contains 3 Support Vector Machine (SVM) models for blink detection and 6 non-machine learning blink detection algorithms. The repository also contains a folder that stores programs used to create a custom evaluation dataset called "RealWorldBlink" and run the evaluation process to retrieve the accuracy metrics of each model.

**Project details**

**1. Blink detection models**

**_a. Support Vector Machines (SVM) models:_** This project contains 3 SVM models for blink detection, these are previously developed in another project.

- The "_orginal_svm_" is created following the proposal of Soukupova T. & Cech J. 2016 paper "Eye blink detection using facial landmarks." The SVM model is trained on the publicly available EyeBlink8 dataset created by Drutarovsky T. & Fogelton A. in their 2015 paper "Eye Blink Detection Using Variance of Motion Vectors." The Eye Aspect Ratio is calculated using 3 eye landmark coordinate pairs detected by Google's MediaPipe Face Landmark Detector. The model has 0.98 Accuracy and good performance in other metrics, including F1, Recall, and Precision. This SVM model is previously created in another project called "Embedded System for Computer Vision Relief."

- The "_new_svm_7landmarksEAR_" is an update of first model. Instead of using only 3 pairs of eye landmark coordinates to calculate the Eye Aspect Ratio (EAR) value, I used 7 pairs. The SVM model is trained on the publicly available EyeBlink8 dataset. The SVM has 0.95 accuracy but lower F1, Recall, and Precision score compared to the first one.

- The "_new_svm_maf_and_extracoords_" is another update of the first model. For this model, we used 5 pairs of eye landmark coordinates to calculate the EAR (an adjustment from using 7 pairs to minimize calculation errors) and applied a Moving Average Filter with a width of 2 to achieve stablized EAR values. This model is trained on EyeBlink8, and it yielded 0.98 accuracy and similar performance in other metrics compared to the first model. However, it has a slightly better score when it comes to classifying positive blinks (class 1).

- _Update 12/01/2024 - "new_svm_extended_dataset":_ The previous models exhibits a bias towards the positive class (class 1) due to the imbalance in the training dataset (EyeBlink8). To mitigate this, we added a filter when selecting the negative samples (class 0) such that only negatives samples at least 5 frames before of after a positive sample are selected. Furthermore, we added a data augumentation including chaging the resolution, adding noise, etc to explicitly for the positivie samples. These actions is to decrease the number of negative samples and increase the number of positive samples, which in turn alleviate the imbalance in the dataset and improve the performance for class 1 classification.

**_b. Non-machine learning blink detection algorithms:_** This project contains 6 non-machine learning algorithms for blink detection.

- The "_blink_counter_EARThresh_" is an update of an algorithm proposed by Soukupova T. & Cech J. 2016 paper "Eye blink detection using facial landmarks." In the paper, the algorithm detects blink by calculating the EAR in real time and comparing it with a fixed EAR threshold of 0.2. The model in this project is similar, but a blink duration threshold of 12 frames is added to differentiate between blinks and other facial expressions such as yawning and smiling.

- The "_blink_counter_dlib_" is similar to the first algorithm; however, this one uses dlib's facial landmark detector to detect eye landmark coordinates rather than Google's MediaPipe Face Landmark Detector. The aim of this algorithm is to assess whether dlib is more suitable for this project than MediaPipe. Based on the experiments conducted, MediaPipe proved to be more robust and accurate.

- The "_blink_counter_MEARThresh_" is created following Dewi C. et al.'s 2022 paper "Adjusting eye aspect ratio for strong eye blink detection based on facial landmarks." This algorithm added a calibration process, employing a formula called "Modified EAR" to calculate the EAR threshold specified to each individual rather than a fixed one. Blink detection is carried out by comparing the real-time EAR values with the EAR threshold. Dewi C. et al. proved that this algorithm is superior in performance compared to the one proposed by Soukupova T. & Cech J.

- The "_blink_counter_3DEAR_" is an update of the first algorithm. Based on Kraft D. et al 2022 paper "Camera-based blink detection using 3d-landmarks", this algorithm incopporates the z-coordinate when calculating the EAR value. The aim is to address the problem that EAR might not be accurate with different head poses. The experiment in the paper by Kraft D. et al. shows that it does indeed improve the accuracy compared to the algorithm by Soukupova T. & Cech J.

- The "_blink_counter_AEAR_nofilter_" is an update of the first algorithm. Acknowledging the fact that a fixed EAR threshold will not be accurate for different people with different facial structures, a calibration process is added. The calibration process must be carried out manually by each user. They are prompted to blink 5 times in intervals of about 3 seconds. The EAR values are collected during the process and are used to calculate the initial EAR threshold. The threshold is automatically updated continuously when the program is deployed.

- The "_blink_counter_AEAR_filter_" is an update of the "blink_counter_AEAR_nofilter." Hence the name, the latter uses a Moving Average Filter with the width of 2 to calculate more stabilized EAR values.

**_2. Evaluation process:_** 

This project also includes programs to retrieve the performance metrics, including Precision, Recall, F1-score, and Accuracy of each model. There's a program to create the custom evaluation video dataset "RealWorldBlink"; a program to process the videos in the dataset; a program to carry out the calibration process; and a program to deploy each model on the evaluation dataset and retrieve the True Postitive (TP), False Postitive (FP), True Negative (TN), and False Negative (FN). After that, there is a program to calculate the performance metrics based on the previously collected TP, FP, TN, FN. These programs are stored in the folder "performance_evaluation."

_Update 01/12/2024:_ The blink detection algorithms are also tested on the public EyeBlink8 dataset. The codes for this procedure is in the "Evaluation_EyeBlink8" folder within the "Performance_evaluation" folder.

**_3. Project progress update:_** 

The blink detection models and algorithms are completed. I am currently completing the evluation process (80% completed), and I plan to record the official results of this project in an academic research paper, "Blink detection using Adaptive Eye Aspect Ratio." The project, including the paper, will be completed by this November (Nov 2024). Although the codes for the blink detection models and algorithms are working properly, the codes themselves are missing proper formatting and pseudocodes to improve readability. This will also be addressed in the near future.


