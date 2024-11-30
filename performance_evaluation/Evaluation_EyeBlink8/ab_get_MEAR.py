import mediapipe as mp
import cv2
import numpy as np
from scipy.spatial import distance as dist #this library allows us to calculate the euclcidean distance between two points based on their x y coords
import time

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


def get_MEARThresh(video_path):
    MEARThresh = 0

    # Coordinates for left and right eyes
    LEFT_EYE_CORNERS = [263, 362]
    RIGHT_EYE_CORNERS = [33, 133]
    VERTICAL_POINTS = [[160, 144], [385, 380], [158, 153], [387, 373]]
    
    p1p4 = []
    p2p6 = []
    p3p5 = []

    # Initialize FaceMesh
    mp_face_mesh = mp.solutions.face_mesh
    with mp_face_mesh.FaceMesh(
        max_num_faces=1,
        refine_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5,
    ) as face_mesh:
        video_stream = cv2.VideoCapture(video_path)
        while video_stream.isOpened():
            success, frame = video_stream.read()
            if not success:
                print(f"Video stream interrupted for {video_path}")
                break

            frame = cv2.flip(frame, 1)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = face_mesh.process(frame)

            if results.multi_face_landmarks:
                mesh_points = np.array([
                    np.multiply([p.x, p.y], [frame.shape[1], frame.shape[0]]).astype(int)
                    for p in results.multi_face_landmarks[0].landmark
                ])

                try:
                    p1p4.append(float((dist.euclidean(mesh_points[LEFT_EYE_CORNERS[0]], mesh_points[LEFT_EYE_CORNERS[1]]) +
                                       dist.euclidean(mesh_points[RIGHT_EYE_CORNERS[0]], mesh_points[RIGHT_EYE_CORNERS[1]])) / 2))
                    p2p6.append(float((dist.euclidean(mesh_points[VERTICAL_POINTS[0][0]], mesh_points[VERTICAL_POINTS[0][1]]) +
                                       dist.euclidean(mesh_points[VERTICAL_POINTS[1][0]], mesh_points[VERTICAL_POINTS[1][1]])) / 2))
                    p3p5.append(float((dist.euclidean(mesh_points[VERTICAL_POINTS[2][0]], mesh_points[VERTICAL_POINTS[2][1]]) +
                                       dist.euclidean(mesh_points[VERTICAL_POINTS[3][0]], mesh_points[VERTICAL_POINTS[3][1]])) / 2))
                except IndexError:
                    print("Required landmarks not detected. Skipping frame.")

    video_stream.release()
    cv2.destroyAllWindows()

    if not p1p4 or not p2p6 or not p3p5:
        print(f"Insufficient data collected for {video_path}")
        return None

    # Calculate MEAR Threshold
    p1p4Max, p1p4Min = max(p1p4), min(p1p4)
    p2p6Max, p2p6Min = max(p2p6), min(p2p6)
    p3p5Max, p3p5Min = max(p3p5), min(p3p5)

    if p1p4Max == 0 or p1p4Min == 0:
        print(f"Zero division issue in {video_path}")
        return None

    EARClosed = (p2p6Min + p3p5Min) / (2 * p1p4Max)
    EAROpen = (p2p6Max + p3p5Max) / (2 * p1p4Min)
    MEARThresh = (EARClosed + EAROpen) / 2

    return MEARThresh


MEARThreshes = []
for path in EAR_paths:
    MEARThresh = get_MEARThresh(path)
    if MEARThresh is not None:
        MEARThreshes.append(MEARThresh)

output_path = r"ab_calibratied_MEARs.txt"
with open(output_path, "w") as file:
    for MEAR in MEARThreshes:
        file.write(f"{MEAR}\n")

print(f"MEAR thresholds saved to {output_path}")
