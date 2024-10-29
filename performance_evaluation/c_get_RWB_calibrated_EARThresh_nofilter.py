'''
Program to conduct calibration and retrieve calibrated initial EARThresh for evalutation
'''

import mediapipe as mp
import cv2
import numpy as np
from scipy.spatial import distance as dist #this library allows us to calculate the euclcidean distance between two points based on their x y coords
import time


#coordinates list of left eye and right eye landmarks
LEFT_EYE =[ 362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398 ]
RIGHT_EYE=[ 33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161 , 246 ]
LEFT_EYE_CORNERS = [263, 362]
RIGHT_EYE_CORNERS = [33, 133]
EAR_THRESH = 0 #the threshold will be defined using the calibration process
BLINK_TIME = 0.4
frame_count = 0
frame_count_started = False
key_1_pressed = False
calibration_in_progress = True
moving_sum = 0

#the blinkEAR_list captured for calibration and the counter during calibration
EAR_values = []
EAR_values_smoothen = []
blinkEARs = []
blinkEARs_list = []
blink_sequence_EARs = []
calibration_blink_count = 0
blink_window_size = 1
blink_sequence = []

#initiate blink count
blink_count = 0

#load the tools
mp_face_mesh = mp.solutions.face_mesh

#setting up display window
win_name = "blink counter with mediapipe"
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

#create the tool
with mp_face_mesh.FaceMesh(
    max_num_faces = 1,
    refine_landmarks = True,
    min_detection_confidence = 0.5,
    min_tracking_confidence = 0.5) as face_mesh:
        #take video stream from web cam
        video_stream = cv2.VideoCapture(0)

        #process frames one frame at a time
        while video_stream.isOpened():
            success, frame = video_stream.read()
            frame = cv2.flip(frame, 1) #flip the frame for selfie mode

            #display error message if stream is interupted
            if not success:
                print("Video stream interupted")

            #detect key pressed
            key = cv2.waitKey(1) & 0xFF  # Capture the key pressed (if any)

            '''#set writable flag of frame to false to prevent unwanted modification
            frame.flags.writeable = False'''
            #switch frame from BGR to RGB for processing with mediapipe
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            #get resutls from face mesh, the result is an "object" that contained normalized cooridnates of the detected landmarks
            results  = face_mesh.process(frame) 

            #check if there are any detected FaceLandmarkerResult
            if results.multi_face_landmarks:
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                #convert results to 2D np array for easy accessing and modification. The normalized coords in results are also converted into pixel coords.
                #retrieve the height and width of frame for coords conversion
                img_h, img_w = frame.shape[:2]
                mesh_points = np.array([np.multiply([p.x, p.y], [img_w, img_h]).astype(int) for p in results.multi_face_landmarks[0].landmark])

                #helper function to calculate EAR of an eye
                def calculate_left_eye_EAR():
                    numerator = 0
                    denomenator = 0
                    numerator += float(dist.euclidean(mesh_points[160], mesh_points[144]))
                    numerator += float(dist.euclidean(mesh_points[158], mesh_points[153]))
                    numerator += float(dist.euclidean(mesh_points[159], mesh_points[145]))
                    numerator += float(dist.euclidean(mesh_points[161], mesh_points[163]))
                    numerator += float(dist.euclidean(mesh_points[157], mesh_points[154]))
                    denomenator += float(dist.euclidean(mesh_points[33], mesh_points[133]))
                    return float((numerator)/(5*denomenator))
                
                def calculate_right_eye_EAR():
                    numerator = 0
                    denomenator = 0
                    numerator += float(dist.euclidean(mesh_points[387], mesh_points[373]))
                    numerator += float(dist.euclidean(mesh_points[385], mesh_points[380]))
                    numerator += float(dist.euclidean(mesh_points[386], mesh_points[374]))
                    numerator += float(dist.euclidean(mesh_points[384], mesh_points[381]))
                    numerator += float(dist.euclidean(mesh_points[388], mesh_points[390]))
                    denomenator += float(dist.euclidean(mesh_points[263], mesh_points[362]))
                    return float((numerator)/(5*denomenator))
                
                left_eye_EAR = calculate_left_eye_EAR()
                right_eye_EAR = calculate_right_eye_EAR()
                averaged_EAR = round(float(left_eye_EAR+right_eye_EAR)/2,4)

                #start the EAR threshold calibration process
                text = "Calibration in progress"
                cv2.putText(frame, text, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
                text = f"calibration blink count: {calibration_blink_count}"
                cv2.putText(frame, text, (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)

                # Function to handle the calibration sequence instructions
                def display_blink_instructions(frame, state, start_time=None):
                    current_time = time.time()
                    
                    if state == 1:
                        # After pressing "1", wait for 1 second
                        if current_time - start_time < 1:
                            text = "pls wait 1 s"
                        elif current_time - start_time < 3:
                            text = "blink, pls wait 2s"
                        else:
                            text = "pls press 1 to end the sequence"
                        cv2.putText(frame, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                    return frame
                
                if key == ord("1"):
                    if not key_1_pressed:  # First press
                        key_1_pressed = True
                        start_time = time.time()  # Mark the start time when "1" is pressed
                    else:
                        key_1_pressed = False
                elif key == ord("q"):
                    break

                # Append EAR values while key is pressed (i.e., part of blink detection)
                if key_1_pressed:
                    frame = display_blink_instructions(frame, 1, start_time)
                    blinkEARs.append(averaged_EAR)

                text = f"key 1 pressed once: {key_1_pressed}"
                cv2.putText(frame, text, (400, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)

                # Check if the key was pressed and then released (i.e., a full blink)
                if not key_1_pressed and len(blinkEARs) != 0:
                    calibration_blink_count += 1
                    blinkEARs_list.append(blinkEARs.copy())  # Store the blink EAR sequence
                    blinkEARs = []  # Reset for the next blink

                #the user is required to blink 10 times during the calibration process
                if calibration_blink_count == 5:
                    text = "Calibration completed"
                    cv2.putText(frame, text, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
                    for blinkEARs in blinkEARs_list:
                        #find the lowest average EAR value in the group --> this highly indicates the middle of a blink in process
                        lowest_blink_EAR = min(blinkEARs)
                        '''blink_sequence_EARs.append(lowest_blink_EAR)'''
                        #retrieve the average EAR values of +-[blink_window_size] of the lowest EAR value
                        '''i = (-1)*blink_window_size'''
                        i = 0
                        while i <= blink_window_size:
                            try:
                                blink_sequence_EARs.append(blinkEARs[blinkEARs.index(lowest_blink_EAR)+i])
                            except IndexError:
                                pass
                            i += 1
                    initial_EARThresh = min(blink_sequence_EARs) #switch from max to min
                    print(initial_EARThresh)
                    break

            #display the video stream
            cv2.imshow(win_name, frame)
            # Exit the loop if 'q' is pressed
            if key == ord('q'):
                break

video_stream.release()
cv2.destroyAllWindows()