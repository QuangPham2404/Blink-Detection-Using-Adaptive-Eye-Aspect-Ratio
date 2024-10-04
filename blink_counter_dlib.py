# import the necessary packages
from imutils import face_utils
from scipy.spatial import distance as dist #this allows us to calulate the Euclidean distance between 2 point (not x1-x2!!!)
import numpy as np
import imutils
import dlib
import cv2
import time

def calculate_EAR(eye): #eye is a nested list of coords
    numerator_1 = float(dist.euclidean(eye[1], eye[5])) #remember to subtract index by 1
    numerator_2 = float(dist.euclidean(eye[2], eye[4]))
    denomenator = float(dist.euclidean(eye[0], eye[3]))
    EAR = float((numerator_1 + numerator_2)/(2*denomenator))
    return EAR

# initialize dlib's face detector (HOG-based) and then create the facial landmark predictor
detector = dlib.get_frontal_face_detector()  # initialize the face detector, able to detect faces in frame
predictor = dlib.shape_predictor(r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\testing\shape_predictor_68_face_landmarks.dat")  # initialize landmark predictor, able to predict locations of the 68 landmarks on the identified face using the detector

# create display window
win_name = "Facial landmark detection"
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)  # NORMAL allow resizing of display window

# take video feed from webcam as source
video_stream = cv2.VideoCapture(0)  # 0 to use webcam

#initiate blink_counter and the threshold to determine blinking
blink_count = 0
frame_count = 0
EAR_THRESH = 0.2 #DIFFERENT PEOPLE HAVE DIFFERENT THRESHOLD
BLINK_TIME = 0.25
frame_count_started = False

# get the frames from video feed
while True:
    ret, frame = video_stream.read()  # read 1 frame from video feed at a time
    if not ret:
        break  # if there is an interruption in reading the frame from video feed, terminate loop

    # converting frame to grayscale
    '''frame = imutils.resize(frame, width=500)'''
    frame = cv2.flip(frame, 1)  # flip the frame horizontally because if not then you have the "mirror effect" when recording the video feed from webcam
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray, 0)  # use detector to find faces (plural) in the frame, return an object containing [[(top_left_x, top_left_y), (bottom_right_x, bottom_right_y)], ...same if there is more faces]
    '''print(rects)'''

    # loop over the face detections
    for index, face in enumerate(faces):
        # determine the facial landmarks for the face region, then convert the facial landmark (x, y)-coordinates to a 2D 2x68 NumPy array
        landmarks_coords = predictor(gray, face)
        landmarks_coords = face_utils.shape_to_np(landmarks_coords) #now we have an array containing the coords of facial landmarks

        #extracting the coordinates of left eye and right eye
        (lstart, lend) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"] #lstart is the first INDEX of the landmarks of the left eye MINUS 1, lEnd is the last
        (rstart, rend) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
        left_eye = landmarks_coords[lstart:lend] #this returns the nested list of all the coordinates of the left eye [[x_1, y_1],...]
        right_eye = landmarks_coords[rstart:rend]
        left_EAR = calculate_EAR(left_eye) #variable type is float
        right_EAR = calculate_EAR(right_eye)
        #as suggested in the paper, for accuracy, we calculate the average of the 2 EAR ratios
        EAR = float((left_EAR + right_EAR)/2)
        #show EAR on screen
        text = f'EAR: {EAR}'
        cv2.putText(frame, text, (300, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)

        fps = video_stream.get(cv2.CAP_PROP_FPS)
        FRAME_THRESH = fps*BLINK_TIME
        if left_EAR < EAR_THRESH and right_EAR < EAR_THRESH:
            print(EAR)
            frame_count_started = True
        if frame_count_started:
            frame_count += 1
        if frame_count_started and left_EAR >= EAR_THRESH and right_EAR >= EAR_THRESH:
            frame_count_started = False
            if frame_count <= FRAME_THRESH:
                blink_count += 1
                text = "Blink"
                cv2.putText(frame, text, (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
            frame_count = 0

        text = f'Blink count: {blink_count}'
        cv2.putText(frame, text, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
        
    # show the output image with the face detections + facial landmarks
    cv2.imshow(win_name, frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # if 'q' is pressed terminate window
        break

# release the capture object
video_stream.release()

# close all OpenCV windows
cv2.destroyAllWindows()