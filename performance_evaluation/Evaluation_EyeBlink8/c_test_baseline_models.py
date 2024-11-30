import mediapipe as mp
import cv2
import numpy as np
from scipy.spatial import distance as dist #this library allows us to calculate the euclcidean distance between two points based on their x y coords
import time


# Load dataset videos' path
EAR_paths = [
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\RealWorldBlink_mp4\bao_output_video2.mp4",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\RealWorldBlink_mp4\nhien_output_video2.mp4",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\RealWorldBlink_mp4\quang_output_video1.mp4",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\RealWorldBlink_mp4\fadahd_output_video.mp4",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\RealWorldBlink_mp4\minh_output_video1.mp4",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\RealWorldBlink_mp4\famohm_output_video1.mp4",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\RealWorldBlink_mp4\huy_output_video.mp4"]


#load the EAR paths
EAR_paths = [
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\1\26122013_223310_cam.avi",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\2\26122013_224532_cam.avi",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\3\26122013_230103_cam.avi",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\4\26122013_230654_cam.avi",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\8\27122013_151644_cam.avi",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\9\27122013_152435_cam.avi",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\10\27122013_153916_cam.avi",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\11\27122013_154548_cam.avi"]


#function to deploy the blink detection alogrithm on a video and a designated calibrated inital_EARThresh
def test_EyeBlink8(video_path, initial_EARThresh):
    #coordinates list of left eye and right eye landmarks
    LEFT_EYE =[ 362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398 ]
    RIGHT_EYE=[ 33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161 , 246 ]
    LEFT_EYE_CORNERS = [263, 362]
    RIGHT_EYE_CORNERS = [33, 133]
    EAR_THRESH = 0 #the threshold will be defined using the calibration process

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
                    EAR_THRESH = initial_EARThresh
                    
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
                    averaged_EAR = round(float(left_eye_EAR+right_eye_EAR)/2, 4)

                    
                    #setting the EAR_THRESH to the initial EARThresh retrieved after the calibration process
                    if averaged_EAR < EAR_THRESH:
                        blink_sequence_frame_indexes.append(frame_index)
                        blink_sequence_frame_indexes_list.append(blink_sequence_frame_indexes.copy())
                        blink_sequence_frame_indexes = []
                        blink_count += 1
                    '''elif averaged_EAR > EAR_THRESH and blink_sequence_frame_indexes:
                        blink_sequence_frame_indexes_list.append(blink_sequence_frame_indexes.copy())
                        blink_sequence_frame_indexes = []'''

                frame_index += 1

    video_stream.release()
    cv2.destroyAllWindows()

    return blink_count, blink_sequence_frame_indexes_list


#use the test_EyeBlink8 function to deploy the blink detection algorithm to assess its performance.
#Need to retrieve the blink_count, blink sequences frame index.
EAR_thresh = [0.18, 0.2, 0.3]
for index, video_path in enumerate(EAR_paths):
    for EARthresh in EAR_thresh:
        print(f"processing video{index+1} with EARthresh {EARthresh}")
        blink_count, blink_sequence_frame_indexes_list = test_EyeBlink8(video_path, EARthresh)
        with open(f"svm_result_{EARthresh}_{index+1}.txt", "w") as file:
            file.write(str(blink_count) + "\n")
            for lst in blink_sequence_frame_indexes_list:
                file.write(str(lst) + "\n")