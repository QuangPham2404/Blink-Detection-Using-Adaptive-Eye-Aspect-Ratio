'''import cv2 as cv
import numpy as np
import mediapipe as mp
import math
import time

#create display window
win_name = "blink counter with mediapipe"
cv.namedWindow(win_name, cv.WINDOW_NORMAL)

frame_counter =0
CEF_COUNTER =0
TOTAL_BLINKS =0
# constants

#Minimum number of frame that the eye shall be closed in order to be count as a blink
CLOSED_EYES_FRAME =1
FONTS =cv.FONT_HERSHEY_COMPLEX

mp_face_mesh = mp.solutions.face_mesh #load face mesh from mediapipe library
mesh_coord = np.zeros(500,dtype = np.object_) #create a 500 element list
LEFT_EYE =[ 362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385,384, 398 ]
RIGHT_EYE=[ 33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161 , 246 ]

LEFT_IRIS = [474,475,476,477]
RIGHT_IRIS = [469,470,471,472]

#Horizontal : Vertical ratio
def blinkRatio(img, landmarks, right_indices, left_indices):
    # Right eyes
    # horizontal line
    r_horizontal_right = landmarks[right_indices[0]]
    r_horizontal__left = landmarks[right_indices[8]]
    # vertical line
    r_vertical_top = landmarks[right_indices[12]]
    r_vertical_bottom = landmarks[right_indices[4]]

    # LEFT_EYE
    # horizontal line
    l_horizontal_right = landmarks[left_indices[0]]
    l_horizontal_left = landmarks[left_indices[8]]

    # vertical line
    l_vertical_top = landmarks[left_indices[12]]
    l_vertical_bottom = landmarks[left_indices[4]]

    rhDistance = euclidean_distance(r_horizontal_right, r_horizontal__left)
    rvDistance = euclidean_distance(r_vertical_top, r_vertical_bottom)

    lvDistance = euclidean_distance(l_vertical_top, l_vertical_bottom)
    lhDistance = euclidean_distance(l_horizontal_right, l_horizontal_left)
    if lvDistance == 0:
        lvDistance += 0.01
    if rvDistance == 0:
        rvDistance += 0.01
    reRatio = rhDistance/rvDistance
    leRatio = lhDistance/lvDistance

    ratio = (reRatio+leRatio)/2
    return ratio

def landmarksDetection(meshmap, img, results, draw=False):
    img_height, img_width= img.shape[:2]
    for idx in LEFT_EYE + RIGHT_EYE + LEFT_IRIS + RIGHT_IRIS:
        point = results.multi_face_landmarks[0].landmark[idx]
        meshmap[idx] = (int(point.x * img_width), int(point.y * img_height))
    # array[(x,y), (x,y)....]

    if draw :
        [cv.circle(img, p, 2, (0,255,0), -1) for p in mesh_coord]

    # returning the list of tuples for each landmarks
    return meshmap

def euclidean_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return distance

def iris_position(iris_center, right_point, left_point):
    center_to_right = euclidean_distance(iris_center, right_point)
    total = euclidean_distance(right_point, left_point)
    ratio = center_to_right / total
    iris_position = ""
    if ratio <= 0.42:
        iris_position = "right"
    elif ratio <= 0.57:
        iris_position = "center"
    else:
        iris_position = "left"
    return iris_position, ratio

def frameProcess(frame, cvt_code):
    frame = cv.resize(frame, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)
    frame_height, frame_width= frame.shape[:2]
    output_frame = cv.cvtColor(frame, cvt_code)
    return frame_height, frame_width, output_frame

cap = cv.VideoCapture(0)
with mp_face_mesh.FaceMesh(
    max_num_faces = 1,
    refine_landmarks = True,
    min_detection_confidence = 0.5,
    min_tracking_confidence = 0.5
) as face_mesh:
    start = time.time()
    while True:
        frame_counter += 1
        ret,frame = cap.read()
        if not ret:
            break
        #Process the image
        img_h, img_w, rgb = frameProcess(frame, cv.COLOR_BGR2RGB)
        #improve performance
        frame.flags.writeable = True
        results = face_mesh.process(rgb)

        if results.multi_face_landmarks:
            #Detection
            mesh_points = landmarksDetection(mesh_coord, frame, results, False)
            ratio = blinkRatio(frame, mesh_points, RIGHT_EYE, LEFT_EYE)

            if ratio > 5.5:
                CEF_COUNTER +=1
                cv.putText(frame, 'Blink', (200, 50), FONTS, 1.3, (255, 255, 0), 2)
            else:
                if CEF_COUNTER>CLOSED_EYES_FRAME:
                    TOTAL_BLINKS +=1
                    CEF_COUNTER =0
            cv.putText(frame, f'Total Blinks: {TOTAL_BLINKS}', (100, 150), FONTS, 0.6, (0, 255, 0), 2)
            (l_cx, l_cy), l_radius = cv.minEnclosingCircle(mesh_points[LEFT_IRIS])
            (r_cx, r_cy), r_radius = cv.minEnclosingCircle(mesh_points[RIGHT_IRIS])
            center_left = np.array([l_cx, l_cy], dtype = np.int32)
            center_right = np.array([r_cx, r_cy], dtype = np.int32)
            cv.circle(frame, center_left, int(l_radius), (255, 0, 255), 1, cv.LINE_AA)
            cv.circle(frame, center_right, int(r_radius), (255, 0, 255), 1, cv.LINE_AA)
            cv.polylines(frame,  [np.array([mesh_points[p] for p in LEFT_EYE ], dtype=np.int32)], True, (0,255,0), 1, cv.LINE_AA)
            cv.polylines(frame,  [np.array([mesh_points[p] for p in RIGHT_EYE ], dtype=np.int32)], True, (0,255,0), 1, cv.LINE_AA)
        #FPS calculation
        end = time.time()-start
        fps = frame_counter/end
        print(fps)
        cv.imshow(win_name, frame)
        key = cv.waitKey(2)
        if key==ord('q') or key ==ord('Q'):
            break
cap.release()
cv.destroyAllWindows()'''


import mediapipe as mp
import cv2
import numpy as np
from scipy.spatial import distance as dist #this library allows us to calculate the euclcidean distance between two points based on their x y coords
import time
import matplotlib.pyplot as plt

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

# Function to initialize the plot (call once at the beginning)
def init_ear_plot():
    plt.ion()  # Enable interactive mode for real-time plotting
    fig, ax = plt.subplots()
    
    ax.set_xlabel('Frame Number')
    ax.set_ylabel('EAR Value')
    ax.set_title('Real-time EAR Value vs Frame Number')
    line, = ax.plot([], [], 'b-', label='EAR')
    
    ax.set_ylim(0.05, 0.5)  # Set reasonable limits for the EAR value (adjust based on your data)
    ax.set_xlim(0, 10)  # Start with an arbitrary x-limit; it will update dynamically

    return fig, ax, line  # Return the figure, axis, and line objects for updating later

# Function to update the plot with new EAR values
def update_ear_plot(frame_num, ear_value, frame_numbers, ear_values, ax, line):
    frame_numbers.append(frame_num)
    ear_values.append(ear_value)
    
    # Keep only the last N points to avoid memory issues
    N = 100  # Adjust N based on how many points you want to keep
    if len(frame_numbers) > N:
        frame_numbers.pop(0)
        ear_values.pop(0)

    line.set_xdata(frame_numbers)
    line.set_ydata(ear_values)
    ax.set_xlim(max(0, frame_num - N), frame_num + 1)
    ax.figure.canvas.draw()
    ax.figure.canvas.flush_events()
    plt.pause(0.001)

# Initialize the plot once before the loop
fig, ax, line = init_ear_plot()

# Initialize empty lists to store frame numbers and EAR values
frame_indexes = []
blink_EAR_values = []

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
        frame_index = 0

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
                    smoothen_value = moving_sum / filter_width

                #display the averaged_EAR
                text = f'EAR: {smoothen_value}'
                cv2.putText(frame, text, (300, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)

                #if averaged_EAR falls bellow EAR_THRESH, the frame_count start, counting the frames that go past while the eye is "closed". 
                # After average_EAR rise above EAR_THRESH again, if the frame_count falls below the FRAME_THRESH blink_counter += 1
                fps = video_stream.get(cv2.CAP_PROP_FPS)
                FRAME_THRESH = fps*BLINK_TIME
                print(smoothen_value)
                if smoothen_value < EAR_THRESH:
                    frame_count_started = True
                if frame_count_started:
                    frame_count += 1
                if frame_count_started and smoothen_value >= EAR_THRESH:
                    frame_count_started = False
                    if frame_count <= FRAME_THRESH:
                        blink_count += 1
                        text = "Blink"
                        cv2.putText(frame, text, (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
                    frame_count = 0

                #display blink count
                text = f'Blink count: {blink_count}'
                cv2.putText(frame, text, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)

            # Update the EAR plot with the new frame and EAR value
            update_ear_plot(frame_index, smoothen_value, frame_indexes, blink_EAR_values, ax, line)
            
            #increase frame_index by 1 after each frame
            frame_index += 1
            
            #display the video stream
            cv2.imshow(win_name, frame)
            # Exit the loop if 'q' is pressed
            if cv2.waitKey(2) == ord('q'):
                break

video_stream.release()
cv2.destroyAllWindows()
