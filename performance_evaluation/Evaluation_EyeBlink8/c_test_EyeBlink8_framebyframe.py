import mediapipe as mp
import cv2
import numpy as np
from scipy.spatial import distance as dist #this library allows us to calculate the euclcidean distance between two points based on their x y coords
import time

#load the EAR paths
EAR_paths = [
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\1\26122013_223310_cam.avi",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\2\26122013_224532_cam.avi",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\3\26122013_230103_cam.avi",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\4\26122013_230654_cam.avi",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\8\27122013_151644_cam.avi",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\9\27122013_152435_cam.avi",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\10\27122013_153916_cam.avi",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\11\27122013_154548_cam.avi",
]


#load the calibrated intital EAR Thresholds
def read_values_from_file(file_path):
    values = []
    with open(file_path, 'r') as file:
        # Read each line and convert it to a float before appending it to the list
        for line in file:
            value = float(line.strip())  # Remove any extra whitespace or newline characters
            values.append(value)
    return values

file_path = r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8\ab_calibratied_EARs.txt"
calibrated_initial_EARThresh = read_values_from_file(file_path)
print(calibrated_initial_EARThresh)


#function to deploy the blink detection alogrithm on a video and a designated calibrated inital_EARThresh
def test_EyeBlink8(video_path, initial_EARThresh):
    test_results = []
    #coordinates list of left eye and right eye landmarks
    LEFT_EYE =[ 362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398 ]
    RIGHT_EYE=[ 33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161 , 246 ]
    LEFT_EYE_CORNERS = [263, 362]
    RIGHT_EYE_CORNERS = [33, 133]
    EAR_THRESH = 0 #the threshold will be defined using the calibration process
    BLINK_TIME = 0.4
    frame_count = 0
    frame_count_started = False
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

    blink_sequence_frame_indexes_list = []
    frame_index = 0

    #initiate blink count
    blink_count = 0

    #load the tools
    mp_face_mesh = mp.solutions.face_mesh

    #create the tool
    with mp_face_mesh.FaceMesh(
        max_num_faces = 1,
        refine_landmarks = True,
        min_detection_confidence = 0.5,
        min_tracking_confidence = 0.5) as face_mesh:
            #take video from the video path
            video_stream = cv2.VideoCapture(video_path)

            blink_sequence_frame_indexes = []

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
                        return float((numerator)/(5*denomenator))
                    
                    left_eye_EAR = calculate_left_eye_EAR()
                    right_eye_EAR = calculate_right_eye_EAR()
                    averaged_EAR = float(left_eye_EAR+right_eye_EAR)/2

                    #apply moving average filter with a width of 5 to smoothen the data
                    filter_width = 4
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

                    
                    #setting the EAR_THRESH to the initial EARThresh retrieved after the calibration process
                    EAR_THRESH = initial_EARThresh
                    #if averaged_EAR falls bellow EAR_THRESH, the frame_count start, counting the frames that go past while the eye is "closed". 
                    # After average_EAR rise above EAR_THRESH again, if the frame_count falls below the FRAME_THRESH blink_counter += 1
                    fps = video_stream.get(cv2.CAP_PROP_FPS)
                    FRAME_THRESH = fps*BLINK_TIME
                    if smoothen_value < EAR_THRESH:
                        frame_count_started = True
                        test_results.append(1)
                    else:
                        test_results.append(0)
                    if frame_count_started:
                        frame_count += 1
                        blink_sequence.append(smoothen_value)
                        blink_sequence_frame_indexes.append(frame_index)
                    if frame_count_started and smoothen_value >= EAR_THRESH:
                        frame_count_started = False
                        if frame_count <= FRAME_THRESH:
                            blink_count += 1
                            blink_sequence_frame_indexes_list.append(blink_sequence_frame_indexes.copy())
                            blink_sequence_frame_indexes = []
                            lowest_in_blink_sequence = min(blink_sequence)
                            highest_in_blink_sequence = max(blink_sequence)
                            #updated_EARThresh = round((blink_sequence[blink_sequence.index(lowest_in_blink_sequence)+1]+(lowest_in_blink_sequence)*2)/3, 4)
                            updated_EARThresh = round((highest_in_blink_sequence+(lowest_in_blink_sequence))/2, 4)
                            #updated_EARThresh = lowest_in_blink_sequence
                            #updated_EARThresh =blink_sequence[blink_sequence.index(lowest_in_blink_sequence)+1]
                            '''if updated_EARThresh > EAR_THRESH:
                                EAR_THRESH = updated_EARThresh
                                print(f"updated EARThresh: {EAR_THRESH}")'''
                        else:
                            blink_sequence_frame_indexes = []
                        frame_count = 0

                frame_index += 1

    video_stream.release()
    cv2.destroyAllWindows()

    return test_results


#use the test_EyeBlink8 function to deploy the blink detection algorithm to assess its performance.
#Need to retrieve the blink_count, blink sequences frame index.
for index, video_path in enumerate(EAR_paths):
    inital_EARThresh = calibrated_initial_EARThresh[index]
    print(f"processing video{index}")
    results = test_EyeBlink8(video_path, inital_EARThresh)
    with open(f"result_{index+1}_fbyf.txt", "w") as file:
        for lst in results:
            file.write(str(lst) + "\n")