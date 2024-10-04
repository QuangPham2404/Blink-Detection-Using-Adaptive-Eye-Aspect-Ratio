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

#the blinkEAR_list captured for calibration and the counter during calibration
p1p4 = []
p2p6 = []
p3p5 = []
calibration_count = 0

#initiate blink count
blink_count = 0

#load the tools
mp_face_mesh = mp.solutions.face_mesh

#setting up display window
win_name = "blink counter with mediapipe"
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)


#function to update the MEARThesh as the program runs in real time
def updated_MEARThresh(p1p4, p2p6, p3p5):
    average_p1p4 = float((float(dist.euclidean(mesh_points[33], mesh_points[133])) + float(dist.euclidean(mesh_points[263], mesh_points[362]))) / 2)
    average_p2p6 = float((float(dist.euclidean(mesh_points[160], mesh_points[144])) + float(dist.euclidean(mesh_points[385], mesh_points[380]))) / 2)
    average_p3p5 = float((float(dist.euclidean(mesh_points[158], mesh_points[153])) + float(dist.euclidean(mesh_points[387], mesh_points[373]))) / 2)
    p1p4Max = max(p1p4)
    p1p4Min = min(p1p4)
    p2p6Max = max(p2p6)
    p2p6Min = min(p2p6)
    p3p5Max = max(p3p5)
    p3p5Min = min(p3p5)
    if average_p1p4 > p1p4Max:
        p1p4Max = average_p1p4
    elif average_p1p4 < p1p4Min:
        p1p4Min = average_p1p4
    if average_p2p6 > p2p6Max:
        p2p6Max = average_p2p6
    elif average_p2p6 < p2p6Min:
        p2p6Min = average_p2p6
    if average_p3p5 > p3p5Max:
        p3p5Max = average_p3p5
    elif average_p3p5 < p3p5Min:
        p3p5Min = average_p3p5 
    #calculate the modified EAR threshold
    EARClosed = (p2p6Min+p3p5Min)/(2*p1p4Max)
    EAROpen = (p2p6Max+p3p5Max)/(2*p1p4Min)
    MEARThresh = (EARClosed+EAROpen)/2
    return MEARThresh


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
                    denomenator += float(dist.euclidean(mesh_points[33], mesh_points[133]))
                    return float((numerator)/(2*denomenator))
                
                def calculate_right_eye_EAR():
                    numerator = 0
                    denomenator = 0
                    numerator += float(dist.euclidean(mesh_points[387], mesh_points[373]))
                    numerator += float(dist.euclidean(mesh_points[385], mesh_points[380]))
                    denomenator += float(dist.euclidean(mesh_points[263], mesh_points[362]))
                    return float((numerator)/(2*denomenator))
                
                left_eye_EAR = calculate_left_eye_EAR()
                right_eye_EAR = calculate_right_eye_EAR()
                averaged_EAR = float(left_eye_EAR+right_eye_EAR)/2

                #display the averaged_EAR
                text = f'EAR: {averaged_EAR}'
                cv2.putText(frame, text, (300, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)


                #start the EAR threshold calibration process
                if calibration_in_progress:
                    text = "Calibration in progress"
                    cv2.putText(frame, text, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
                    text = f"calibration count: {calibration_count}"
                    cv2.putText(frame, text, (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
                    
                    #detect key pressed
                    key = cv2.waitKey(1) & 0xFF  # Capture the key pressed (if any)
                    
                    if key == ord("1"):
                        if not key_1_pressed:  # First press
                            key_1_pressed = True
                        else:
                            key_1_pressed = False

                    # Append EAR values while key is pressed (i.e., part of blink detection)
                    if key_1_pressed:
                        p1p4.append(float((float(dist.euclidean(mesh_points[33], mesh_points[133])) + float(dist.euclidean(mesh_points[263], mesh_points[362]))) / 2))
                        p2p6.append(float((float(dist.euclidean(mesh_points[160], mesh_points[144])) + float(dist.euclidean(mesh_points[385], mesh_points[380]))) / 2))
                        p3p5.append(float((float(dist.euclidean(mesh_points[158], mesh_points[153])) + float(dist.euclidean(mesh_points[387], mesh_points[373]))) / 2))

                    text = f"key 1 pressed once: {key_1_pressed}"
                    cv2.putText(frame, text, (400, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)

                    # Check if the key was pressed and then released (i.e., a full blink)
                    if not key_1_pressed and p1p4 and p2p6 and p3p5:
                        calibration_count += 1

                    #the user is required to blink 1 times during the calibration process
                    if calibration_count == 1:
                        calibration_in_progress = False
                        text = "Calibration completed"
                        cv2.putText(frame, text, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
                        p1p4Max = max(p1p4)
                        p1p4Min = min(p1p4)
                        p2p6Max = max(p2p6)
                        p2p6Min = min(p2p6)
                        p3p5Max = max(p3p5)
                        p3p5Min = min(p3p5)
                        #calculate the modified EAR threshold
                        EARClosed = (p2p6Min+p3p5Min)/(2*p1p4Max)
                        EAROpen = (p2p6Max+p3p5Max)/(2*p1p4Min)
                        MEARThresh = (EARClosed+EAROpen)/2
                        print(MEARThresh)
                else:
                    #setting the EAR_THRESH to the initial EARThresh retrieved after the calibration process
                    EAR_THRESH = MEARThresh
                    #if averaged_EAR falls bellow EAR_THRESH, the frame_count start, counting the frames that go past while the eye is "closed". 
                    # After average_EAR rise above EAR_THRESH again, if the frame_count falls below the FRAME_THRESH blink_counter += 1
                    fps = video_stream.get(cv2.CAP_PROP_FPS)
                    FRAME_THRESH = fps*BLINK_TIME
                    if averaged_EAR < EAR_THRESH:
                        frame_count_started = True
                    if frame_count_started:
                        frame_count += 1
                    if frame_count_started and averaged_EAR >= EAR_THRESH:
                        frame_count_started = False
                        if frame_count <= FRAME_THRESH:
                            blink_count += 1
                            text = "Blink"
                            cv2.putText(frame, text, (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
                        frame_count = 0
                    # update MEARThresh in real time
                    MEARThresh = updated_MEARThresh(p1p4, p2p6, p3p5)
                    print(MEARThresh)

                    #display blink count
                    text = f'Blink count: {blink_count}'
                    cv2.putText(frame, text, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
            
            #display the video stream
            cv2.imshow(win_name, frame)
            # Exit the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

video_stream.release()
cv2.destroyAllWindows()