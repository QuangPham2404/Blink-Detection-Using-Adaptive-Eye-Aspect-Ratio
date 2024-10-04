import mediapipe as mp
import cv2
import numpy as np
from scipy.spatial import distance as dist #this library allows us to calculate the euclcidean distance between two points based on their x y coords
import time
import os

#load calibration videos
#helper function to load the file paths from a directory and store them in a list
def get_all_file_paths(directory):
    """
    Retrieve all file paths in a folder and its subfolders.

    Parameters:
    directory (str): The path of the directory to search.

    Returns:
    list: A list containing the full paths of all the files in the folder.
    """
    file_paths = []  # List to store all file paths

    # Walk through all subdirectories and files
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Create the full file path and append it to the list
            full_path = os.path.join(root, file)
            file_paths.append(full_path)
    
    return file_paths

#create the file paths lists
calibration_videos = []
EyeBlink8_video0 = get_all_file_paths(r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8\individual_EyeBlink8\EyeBlink8_0")
EyeBlink8_video1 = get_all_file_paths(r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8\individual_EyeBlink8\EyeBlink8_1")
EyeBlink8_video2 = get_all_file_paths(r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8\individual_EyeBlink8\EyeBlink8_2")
EyeBlink8_video3 = get_all_file_paths(r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8\individual_EyeBlink8\EyeBlink8_3")
EyeBlink8_video4 = get_all_file_paths(r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8\individual_EyeBlink8\EyeBlink8_4")
EyeBlink8_video5 = get_all_file_paths(r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8\individual_EyeBlink8\EyeBlink8_5")
EyeBlink8_video6 = get_all_file_paths(r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8\individual_EyeBlink8\EyeBlink8_6")
EyeBlink8_video7 = get_all_file_paths(r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8\individual_EyeBlink8\EyeBlink8_7")

calibration_videos.append(EyeBlink8_video0)
calibration_videos.append(EyeBlink8_video1)
calibration_videos.append(EyeBlink8_video2)
calibration_videos.append(EyeBlink8_video3)
calibration_videos.append(EyeBlink8_video4)
calibration_videos.append(EyeBlink8_video5)
calibration_videos.append(EyeBlink8_video6)
calibration_videos.append(EyeBlink8_video7)


#function to get the calibrated intial EAR value of each video in the dataset
def get_calibrated_EAR(video_path):
    #coordinates list of left eye and right eye landmarks
    LEFT_EYE =[ 362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398]
    RIGHT_EYE=[ 33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161 , 246]
    LEFT_EYE_CORNERS = [263, 362]
    RIGHT_EYE_CORNERS = [33, 133]
    EAR_THRESH = 0 #the threshold will be defined using the calibration process
    BLINK_TIME = 0.4
    moving_sum = 0

    #the blinkEAR_list captured for calibration and the counter during calibration
    EAR_values = [] #this list is used to apply the moving average filter
    smoothen_values = [] #this list is used to store the moving filter

    #load the tools
    mp_face_mesh = mp.solutions.face_mesh

    #create the tool
    with mp_face_mesh.FaceMesh(
        max_num_faces = 1,
        refine_landmarks = True,
        min_detection_confidence = 0.5,
        min_tracking_confidence = 0.5) as face_mesh:
            #load video from video path
            video_stream = cv2.VideoCapture(video_path)

            #process frames one frame at a time
            while video_stream.isOpened():
                success, frame = video_stream.read()
                frame = cv2.flip(frame, 1) #flip the frame for selfie mode

                #display error message if stream is interupted
                if not success:
                    print("Video stream interupted")
                    break

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
                        return float((numerator)/(2*denomenator))
                    
                    left_eye_EAR = calculate_left_eye_EAR()
                    right_eye_EAR = calculate_right_eye_EAR()
                    averaged_EAR = float(left_eye_EAR+right_eye_EAR)/2

                    #apply moving average filter with a width of 5 to smoothen the data
                    filter_width = 2
                    # If the number of values in the list is less than filter width, append the EAR value
                    if len(EAR_values) < filter_width:
                        EAR_values.append(averaged_EAR)
                        moving_sum += averaged_EAR  # Add to moving sum
                        # Compute the average based on the current number of values
                        smoothen_value = moving_sum / len(EAR_values)
                    else:
                        # Maintain sliding window
                        oldest_value = EAR_values.pop(0)  # Remove the oldest value
                        moving_sum = moving_sum - oldest_value + averaged_EAR  # Update moving sum
                        EAR_values.append(averaged_EAR)
                        # Compute the moving average
                        smoothen_value = round(moving_sum / filter_width,4)
                    #store the calculated smoothen value in the smoothen values list for retrieving the calibrated initial EAR threshold.
                    smoothen_values.append(smoothen_value)

    #repeat again until the end of the videos                
    video_stream.release()
    cv2.destroyAllWindows()

    #after retrieving the EAR list, find the lowest EAR value, and set the value next to it as the calibrated intiial EAR thresh.
    min_EAR = min(smoothen_values)
    try:
        calibrated_initial_EAR_value = smoothen_values[smoothen_values.index(min_EAR)+1]
    except IndexError:
        calibrated_initial_EAR_value = min_EAR
    return calibrated_initial_EAR_value


#get the calibrated intial EAr threshold for each video and store them in an text file
calibrated_EARs = []
calibrated_initial_EARThresh_list = [] 
for videos_list in calibration_videos:
    for video in videos_list:
        calibrated_EARs.append(get_calibrated_EAR(video))
    #after find the calibration EAR of each video, identify the largest and set that as the calibrated initial EAR threshold for that video
    calibrated_initial_EARThresh = max(calibrated_EARs)
    calibrated_initial_EARThresh_list.append(calibrated_initial_EARThresh)
    #empty the calibrated_EAR list for the next calibration videos of the next video in the dataset
    calibrated_EARs = []


# Write the calibrated EAR values into a text file
with open("calibrated_EARs.txt", "w") as file:
    for ear in calibrated_initial_EARThresh_list:
        file.write(f"{ear}\n")