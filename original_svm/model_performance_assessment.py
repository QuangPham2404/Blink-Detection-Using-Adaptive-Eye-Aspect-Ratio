import mediapipe as mp
import cv2
import numpy as np
from scipy.spatial import distance as dist #this library allows us to calculate the euclcidean distance between two points based on their x y coords
import time

paths = [
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\1\26122013_223310_cam.avi",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\2\26122013_224532_cam.avi",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\3\26122013_230103_cam.avi",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\4\26122013_230654_cam.avi",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\8\27122013_151644_cam.avi",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\9\27122013_152435_cam.avi",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\10\27122013_153916_cam.avi",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\11\27122013_154548_cam.avi",
]


for path in paths:
    #coordinates list of left eye and right eye landmarks
    LEFT_EYE =[ 362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398 ]
    RIGHT_EYE=[ 33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161 , 246 ]
    LEFT_EYE_CORNERS = [263, 362]
    RIGHT_EYE_CORNERS = [33, 133]
    EAR_THRESH = 1.72
    BLINK_TIME = 0.4
    frame_count = 0
    frame_count_started = False
    frame_index = 0
    model_results = []

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
            #take video stream from web cam
            video_stream = cv2.VideoCapture(path)

            total_frames = int(video_stream.get(cv2.CAP_PROP_FRAME_COUNT))

            #process frames one frame at a time
            while video_stream.isOpened():
                success, frame = video_stream.read()
                frame = cv2.flip(frame, 1) #flip the frame for selfie mode

                #display error message if stream is interupted
                if not success:
                    print("Video stream interupted")

                #switch frame from BGR to RGB for processing with mediapipe
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                #get resutls from face mesh, the result is an "object" that contained normalized cooridnates of the detected landmarks
                results  = face_mesh.process(frame) 

                #check if there are any detected FaceLandmarkerResult
                if results.multi_face_landmarks:
                    #convert results to 2D np array for easy accessing and modification. The normalized coords in results are also converted into pixel coords.
                    #retrieve the height and width of frame for coords conversion
                    img_h, img_w = frame.shape[:2]
                    mesh_points = np.array([np.multiply([p.x, p.y], [img_w, img_h]).astype(int) for p in results.multi_face_landmarks[0].landmark])

                    #helper function to calculate EAR of an eye
                    def calculate_left_eye_EAR():
                        numerator = 0
                        denomenator = 0
                        numerator += float(dist.euclidean(mesh_points[159], mesh_points[145]))
                        numerator += float(dist.euclidean(mesh_points[158], mesh_points[153]))
                        numerator += float(dist.euclidean(mesh_points[157], mesh_points[154]))
                        numerator += float(dist.euclidean(mesh_points[173], mesh_points[155]))
                        numerator += float(dist.euclidean(mesh_points[160], mesh_points[144]))
                        numerator += float(dist.euclidean(mesh_points[161], mesh_points[163]))
                        numerator += float(dist.euclidean(mesh_points[246], mesh_points[7]))
                        denomenator += float(dist.euclidean(mesh_points[33], mesh_points[133]))
                        return float((numerator + numerator)/(2*denomenator))
                    
                    def calculate_right_eye_EAR():
                        numerator = 0
                        denomenator = 0
                        numerator += float(dist.euclidean(mesh_points[386], mesh_points[374]))
                        numerator += float(dist.euclidean(mesh_points[387], mesh_points[373]))
                        numerator += float(dist.euclidean(mesh_points[288], mesh_points[390]))
                        numerator += float(dist.euclidean(mesh_points[466], mesh_points[249]))
                        numerator += float(dist.euclidean(mesh_points[385], mesh_points[380]))
                        numerator += float(dist.euclidean(mesh_points[384], mesh_points[381]))
                        numerator += float(dist.euclidean(mesh_points[398], mesh_points[382]))
                        denomenator += float(dist.euclidean(mesh_points[263], mesh_points[362]))
                        return float((numerator + numerator)/(2*denomenator))
                    
                    left_eye_EAR = calculate_left_eye_EAR()
                    right_eye_EAR = calculate_right_eye_EAR()
                    averaged_EAR = float(left_eye_EAR+right_eye_EAR)/2

                    #if averaged_EAR falls bellow EAR_THRESH, the frame_count start, counting the frames that go past while the eye is "closed". 
                    # After average_EAR rise above EAR_THRESH again, if the frame_count falls below the FRAME_THRESH blink_counter += 1
                    model_results_of_path = np.zeros(total_frames)
                    fps = video_stream.get(cv2.CAP_PROP_FPS)
                    FRAME_THRESH = fps*BLINK_TIME
                    if averaged_EAR < EAR_THRESH:
                        frame_count_started = True
                    if frame_count_started:
                        frame_count += 1
                    if frame_count_started and averaged_EAR >= EAR_THRESH:
                        frame_count_started = False
                        if frame_count <= FRAME_THRESH:
                            model_results_of_path[frame_index] = 1
                        frame_count = 0
                frame_index += 1
            model_results.append(model_results_of_path)

    video_stream.release()
    cv2.destroyAllWindows()

print(model_results)